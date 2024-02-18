import numpy as np

import csdl
from python_csdl_backend import Simulator
# from vast.utils.generate_rectangular_mesh import generate_rectangular_mesh
from vast.core.submodels.geometric_submodels.mesh_to_vortex_mesh import MeshToVortexMesh
from vast.core.submodels.geometric_submodels.compute_normals import ComputeNormals
from vast.core.submodels.geometric_submodels.geometric_property_extraction import GeometricPropertyExtraction
from vast.core.submodels.aerodynamic_coeffs_submodels.sub_aic_biot_savarts import SubAicBiotSavarts

from vast.core.submodels.aerodynamic_coeffs_submodels.projection_gpt import Projection
from vast.core.submodels.wake_submodels.generate_fixed_wake import GenerateFixedWake
from vast.core.submodels.velocity_submodels import kinematic_velocity_model
from VAST.utils.generate_mesh import *


class VLMFixedWakeSystem(csdl.Model):

    def initialize(self):
        self.parameters.declare('surface_names', types=list)
        self.parameters.declare('surface_shapes', types=list)
        self.parameters.declare('mesh_unit', types=str)
        self.parameters.declare('problem_type', types=str)

        self.parameters.declare('num_wake_pts', default=2)
        self.parameters.declare('delta_t', default=1.)

        self.parameters.declare('compressible', types=bool, default=False)
        self.parameters.declare('Ma', types=float, default=None)

    def define(self):

        # add vortex mesh model to compute the vortex mesh from the input mesh
        self.add_mesh_to_vortex_mesh()
        # add frame_vel computation model given the aircraft states, or pass if frame_vel is given
        self.add_frame_vel_computation()
        # add compute normals model to compute the normal vectors of the input mesh
        self.add_compute_lifting_surface_normals()
        # add geometric property extraction model to compute the geometric properties of the input mesh
        # this includes the collocation points, the panel area, the force_evaluation_pts of each surface
        # and the concatenated bound vector of all lifting surfaces
        self.add_geometric_property_extraction()

        # add the model to compute the kinematic velocity, this is the undisturbed velocity of the flow
        self.add_kinematic_velocity_model()

        # project the kinematic velocity to the get the rhs of the equation
        self.add_project_kinematic_velocity()

        # add the model to compute the aerodynamic coefficients
        self.bound_vortex_coords_names = [surface_name + '_bound_vtx_coords' for surface_name in surface_names]
        self.bound_collocation_pts_names = [surface_name + '_collocation_pts' for surface_name in surface_names]
        self.bound_collocation_pts_shapes = [(num_nodes, surface_shape[1]-1, surface_shape[2]-1, 3) for surface_shape in surface_shapes]
        self.add_bound_bound_aerodynamic_coefficients()

        
        # project the aic to the normal direction
        # self.add_project_aic_to_normal_direction()

        # add the model to compute the wake coordinates
        # self.add_generate_fixed_wake()

        # compute the wake aic
        # self.add_compute_wake_aic()
        # project the wake aic to the normal direction
        # self.add_project_wake_aic_to_normal_direction()

        # get the lhs A matrix
        # self.add_compute_lhs_matrix()

        # solve the linear system
        # self.add_solve_linear_system()

    
    def add_mesh_to_vortex_mesh(self):
        # create a mesh to vortex mesh model 
        # that computes the vortex mesh from the input mesh
        m2vm_parameters = {
            'surface_names': self.parameters['surface_names'],
            'surface_shapes': self.parameters['surface_shapes'],
            'mesh_unit': self.parameters['mesh_unit'],
            'delta_t': self.parameters['delta_t'],
            'problem_type': self.parameters['problem_type'],
            'compressible': self.parameters['compressible'],
            'Ma': self.parameters['Ma']
        }

        m2vm_model = MeshToVortexMesh(**m2vm_parameters)
        self.add(m2vm_model, 'MeshToVortexMesh')

    def add_frame_vel_computation(self):
        # pass for now as the frame velocity is given, need to add here a model from 
        # aircraft states to frame velocity in VLM
        pass

    def add_compute_lifting_surface_normals(self):
        # add compute normals model to compute the normal vectors of the input mesh
        self.bound_surface_normal_names = [surface_name + '_normals' for surface_name in surface_names]
        lifting_surface_normals_parameters = {
            'surfaces_to_eval_normals': self.parameters['surface_names'],
            'normal_names': self.bound_surface_normal_names,
            'surfaces_to_eval_normal_shapes': self.parameters['surface_shapes']
        }
        compute_normals = ComputeNormals(**lifting_surface_normals_parameters)
        self.add(compute_normals, 'ComputeLiftingSurfaceNormals')

    def add_geometric_property_extraction(self):
        # add geometric property extraction model to compute the geometric properties of the input mesh
        # this includes the collocation points, the panel area, the force_evaluation_pts of each surface
        # and the concatenated bound vector of all lifting surfaces
        geoprop_parameters = {
            'surface_names': self.parameters['surface_names'],
            'surface_shapes': self.parameters['surface_shapes']
        }
        geoprop = GeometricPropertyExtraction(**geoprop_parameters)
        self.add(geoprop, 'GeometricPropertyExtraction')

    def add_kinematic_velocity_model(self):
        # add the model to compute the kinematic velocity, this is the undisturbed velocity of the flow
        # expand the frame velocity to get the kinematic velocity
        kinematic_velocity_model_parameters = {
            'surface_names': self.parameters['surface_names'],
            'surface_shapes': self.parameters['surface_shapes']
        }
        kinematic_velocity_model = kinematic_velocity_model(**kinematic_velocity_model_parameters)

    def add_project_kinematic_velocity(self):
        # project the kinematic velocity to the get the rhs of the equation
        surface_shapes = self.parameters['surface_shapes']
        self.bound_normal_shapes = [(num_nodes, surface_shape[1]-1, surface_shape[2]-1, 3) for surface_shape in surface_shapes]
        self.kinematic_vel_names = [surface_name + '_kinematic_vel' for surface_name in surface_names]
        self.kinematic_vel_shapes = [(num_nodes, (surface_shape[1]-1)* (surface_shape[2]-1), 3) for surface_shape in surface_shapes]
        projection = Projection(
            input_var_names=self.kinematic_vel_names,
            normal_names=self.bound_surface_normal_names,
            output_var_name='rhs',
            input_var_shapes=self.kinematic_vel_shapes,
            normal_shapes=self.bound_normal_shapes)

        self.add(projection, 'Projection_rhs')

    def add_bound_bound_aerodynamic_coefficients(self):
        # add the model to compute the aerodynamic coefficients

        aic_model = SubAicBiotSavarts(
            eval_pt_names=self.bound_collocation_pts_names,
            eval_pt_shapes=self.bound_collocation_pts_shapes,
            vortex_coords_names=self.bound_vortex_coords_names,
            vortex_coords_shapes=self.parameters['surface_shapes'],
            vc=True,
            output_names=['aic'])

        self.add(aic_model, 'SubAicBiotSavarts')

        # TODO: assemble AIC form aic-sub


