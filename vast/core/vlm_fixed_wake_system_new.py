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
from vast.core.submodels.velocity_submodels.kinematic_velocity import kinematicVelocityModel


class VLMFixedWakeSystem(csdl.Model):
    '''
    VLM Fixed Wake System
    '''
    def initialize(self):
        self.parameters.declare('surface_names', types=list)
        self.parameters.declare('surface_shapes', types=list)
        self.parameters.declare('mesh_unit', types=str)
        self.parameters.declare('problem_type', types=str)

        self.parameters.declare('num_wake_pts', default=2)
        self.parameters.declare('delta_t', default=1.)

        self.parameters.declare('compressible', types=bool, default=False)
        self.parameters.declare('Ma', types=float, default=None)

        self.parameters.declare('output_var_names', types=list, default=['forces', 'moments'])

    def define(self):
        # add compute vlm inputs: vortex mesh and frame velocity
        self.add_compute_vlm_inputs()
        # add pre-processing models: compute normals, geometric property extraction, and kinematic velocity
        self.add_pre_processing_models()
        # add the model to compute the RHS of the equation (projected kinematic velocity)
        self.add_compute_rhs()
        # add the model to compute the LHS A matrix, 
        # - projected aerodynamic coefficients induced by the bound vortex, and the wake
        self.add_compute_lhs_A()
        # add the model to solve the linear system
        self.add_solve_system()
        # add the model to compute the forces and moments
        # self.add_compute_forces_moments()
    def add_compute_vlm_inputs(self):
        # add vortex mesh model to compute the vortex mesh from the input mesh
        self.add_mesh_to_vortex_mesh()
        # add frame_vel computation model given the aircraft states, or pass if frame_vel is given
        self.add_frame_vel_computation()

    def add_pre_processing_models(self):
        # add compute normals model to compute the normal vectors of the input mesh
        self.add_compute_lifting_surface_normals()
        # add geometric property extraction model to compute the geometric properties of the input mesh
        # this includes the collocation points, the panel area, the force_evaluation_pts of each surface
        # and the concatenated bound vector of all lifting surfaces
        self.add_geometric_property_extraction()

    def add_compute_rhs(self): 
        # add the model to compute the kinematic velocity, this is the undisturbed velocity of the flow
        self.add_kinematic_velocity_model()

        # project the kinematic velocity to the get the rhs of the equation
        self.add_project_kinematic_velocity()

    def add_compute_lhs_A(self):

        # add the model to compute the sub aerodynamic coefficients
        # and then, assemble the AIC from the sub aic
        surface_shapes = self.parameters['surface_shapes']
        surface_names = self.parameters['surface_names']
        num_nodes = surface_shapes[0][0]
        self.bound_collocation_pts_names = [f"{name}_collocation_pts" for name in surface_names for _ in range(len(surface_names))]
        self.bound_collocation_pts_shapes = [(num_nodes, nx - 1, ny - 1, 3) for num_nodes, nx, ny, _ in surface_shapes for _ in range(len(surface_names))]
        
        self.bound_vortex_coords_names = [surface_name + '_bound_vtx_coords' for surface_name in surface_names] * len(surface_names)
        self.vortex_coords_shapes = surface_shapes * len(surface_names)
        # self.op_aic_names is in the format of bound_surface_name + vortex_surface_name + '_aic_sub'
        self.op_aic_names = [f"{bound_surface_name}_{vortex_surface_name}_aic_sub" for bound_surface_name in surface_names for vortex_surface_name in surface_names]

        print('op_aic_names',self.op_aic_names)

        self.add_bound_bound_aerodynamic_coefficients()



        # project the aic to the normal direction
        self.add_project_aic_to_normal_direction()

        # add the model to compute the wake coordinates
        self.add_generate_fixed_wake()

        # compute the wake aic
        self.add_compute_wake_aic()
        # project the wake aic to the normal direction
        self.add_project_wake_aic_to_normal_direction()

        # get the lhs A matrix
        self.add_compute_lhs_matrix()

    def add_solve_system(self):
        # solve the linear system
        aic_shape = self.compute_bound_aic_shape()
        lhs_A = self.declare_variable('MTX', shape=(aic_shape[:-1]))
        rhs = self.declare_variable('rhs', shape=aic_shape[:-2])
        self.add_solve_linear_system(lhs_A, rhs)

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
        surface_names = self.parameters['surface_names']
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
        kinematic_velocity_model = kinematicVelocityModel(**kinematic_velocity_model_parameters)
        self.add(kinematic_velocity_model, 'KinematicVelocity')

    def add_project_kinematic_velocity(self):
        # project the kinematic velocity to the get the rhs of the equation
        surface_shapes = self.parameters['surface_shapes']
        surface_names = self.parameters['surface_names']
        num_nodes = surface_shapes[0][0]
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
            vortex_coords_shapes=self.vortex_coords_shapes,
            vc=True,
            output_names=self.op_aic_names)

        self.add(aic_model, 'SubAicBiotSavarts')

        # TODO: assemble AIC form aic-sub
        self.aic_name = 'bound_aic'
        bound_aic_shape = self.compute_bound_aic_shape()
        self.add_assemble_aic(aic_sub_names=self.op_aic_names, sub_aic_shapes=self.sub_aic_shapes)

    def add_assemble_aic(self, aic_sub_names, sub_aic_shapes):

        surface_names = self.parameters['surface_names']
        
        # create a csdl variable for the bound aic
        bound_aic_shape = self.compute_bound_aic_shape()
        bound_aic = self.create_output(self.aic_name, shape=bound_aic_shape)

        start_i = 0
        start_j = 0
        print('sub_aic_shapes',sub_aic_shapes)

        for i in range(len(surface_names)): 
            for j in range(len(surface_names)):
                # number of aic_sub_names
                idx = i * len(surface_names) + j
                aic_sub = self.declare_variable(aic_sub_names[idx], shape=sub_aic_shapes[idx])
                delta_i = sub_aic_shapes[idx][1]
                delta_j = sub_aic_shapes[idx][2]
                print('i,j',i,j)
                print('start_i,start_j',start_i,start_j)
                print('delta_i,delta_j',delta_i,delta_j)
                print('start_j',start_j)
                print('delta_j',delta_j)
                print('start_i+delta_i,start_j+delta_j',start_i+delta_i,start_j+delta_j)
                bound_aic[:, start_i:start_i+delta_i, start_j:start_j+delta_j, :] = aic_sub
                start_j += delta_j
            start_i += delta_i
            start_j = 0
    
            




    def add_project_aic_to_normal_direction(self):
        # project the aic to the normal direction
        bound_aic_shape = [self.compute_bound_aic_shape()]
        print('bound_aic_shape',bound_aic_shape)
        aic_projected_model = Projection(
            input_var_names=[self.aic_name] ,
            normal_names=self.bound_surface_normal_names,
            output_var_name='lhs_A_matrix',
            input_var_shapes=bound_aic_shape,
            normal_shapes=self.bound_normal_shapes)
        
        self.add(aic_projected_model, 'ProjectionLHSA')

    def compute_bound_aic_shape(self):
        # compute the shape of the lhs A matrix
        # The idea is to compute the shape of the total assembled AIC from the sub aic
        # Here is a for loop psudo-code of the same code:
        # aic_shape_row = aic_shape_col = 0
        # for i in range(len(bd_coll_pts_shapes)):
        #     aic_shape_row += (bd_coll_pts_shapes[i][1] *
        #                       bd_coll_pts_shapes[i][2])
        #     aic_shape_col += ((bd_coll_pts_shapes[i][1]) *
        #                       (bd_coll_pts_shapes[i][2]))



        surface_shapes = self.parameters['surface_shapes']
        num_nodes = surface_shapes[0][0]
        compute_size = lambda shape: (shape[1]-1) * (shape[2]-1)
        total_size = sum(map(compute_size, surface_shapes))

        self.sub_aic_shapes = []
        for i in range(len(self.bound_collocation_pts_shapes)):
            sub_aic_shapes_row = self.bound_collocation_pts_shapes[i][1] * self.bound_collocation_pts_shapes[i][2]

            sub_aic_shapes_col = (self.vortex_coords_shapes[i][1]-1) * (self.vortex_coords_shapes[i][2]-1)
            self.sub_aic_shapes.append((num_nodes, sub_aic_shapes_row, sub_aic_shapes_col, 3))

        return (num_nodes, total_size, total_size, 3)
    
    def add_generate_fixed_wake(self):
        # add the model to compute the wake coordinates
        wake_model = GenerateFixedWake(
            surface_names=self.parameters['surface_names'],
            surface_shapes=self.parameters['surface_shapes'],
            n_wake_pts_chord = self.parameters['num_wake_pts'],
            delta_t = self.parameters['delta_t'],
        )
        self.add(wake_model, 'GenerateFixedWake')
    
    def add_compute_wake_aic(self):
        # compute the shape of the wake aic
        surface_names = self.parameters['surface_names']
        surface_shapes = self.parameters['surface_shapes']
        num_nodes = surface_shapes[0][0]

        surface_shapes = self.parameters['surface_shapes']
        wake_coords_names = [surface_name + '_wake_coords' for surface_name in surface_names]
        wake_coords_shapes = [(num_nodes, self.parameters['num_wake_pts'], surface_shape[2], 3) for surface_shape in surface_shapes]
        # self.wake_aic_names = [surface_name + '_wake_aic' for surface_name in surface_names]
        wake_aic_model = SubAicBiotSavarts(
            eval_pt_names=self.bound_collocation_pts_names,
            eval_pt_shapes=self.bound_collocation_pts_shapes,
            vortex_coords_names=wake_coords_names,
            vortex_coords_shapes=wake_coords_shapes,
            output_names=['wake_aic'])
        self.add(wake_aic_model, 'WakeSubAicBiotSavarts')

    def add_project_wake_aic_to_normal_direction(self):
        # num_nodes = self.parameters['surface_shapes'][0][0]
        # project the wake aic to the normal direction
        input_var_shapes = self.compute_wake_aic_shape()
        # [(num_nodes, (nc-1)* (ns-1), (n_wake_pts_chord-1)* (ns-1), 3)]
        
        wake_aic_projected_model = Projection(
            input_var_names=['wake_aic'],
            normal_names=self.bound_surface_normal_names,
            output_var_name='wake_aic_projection',
            input_var_shapes=input_var_shapes,
            normal_shapes=self.bound_normal_shapes)
        self.add(wake_aic_projected_model, 'ProjectionWakeAic')

    def compute_wake_aic_shape(self):
        # compute the shape of the wake aic
        surface_shapes = self.parameters['surface_shapes']
        num_nodes = surface_shapes[0][0]
        n_wake_pts_chord = self.parameters['num_wake_pts']
        wake_aic_shape = [(num_nodes, (surface_shape[1]-1)* (surface_shape[2]-1), (n_wake_pts_chord-1)* (surface_shape[2]-1), 3) for surface_shape in surface_shapes]
        return wake_aic_shape
    
    def add_compute_lhs_matrix(self):
        # get the lhs A matrix
        surface_shapes = self.parameters['surface_shapes']
        num_nodes = surface_shapes[0][0]
        wake_aic_projection_shape = self.compute_wake_aic_shape()[0][:-1]
        M = self.declare_variable('wake_aic_projection', shape=wake_aic_projection_shape)
        M_mat = M*1.0
        self.register_output('M_mat', M_mat)
        from vast.utils.custom_explicit_mat_sprsmat import Explicit, compute_spars
        sprs = compute_spars(surface_shapes)

        print('wake_aic_projection_shape',wake_aic_projection_shape)

        M_reshaped = csdl.custom(M_mat,op=Explicit(
                                                num_nodes=num_nodes,
                                                sprs=sprs,
                                                num_bd_panel=wake_aic_projection_shape[1],
                                                num_wake_panel=wake_aic_projection_shape[2],
                                            ))
        self.register_output('M_reshaped', M_reshaped)
        aic_projection = self.declare_variable('lhs_A_matrix', shape=(self.compute_bound_aic_shape()[:-1]))
        MTX = aic_projection + csdl.reshape(M_reshaped, aic_projection.shape)

        self.register_output('MTX', MTX)
    
    def add_solve_linear_system(self, lhs_A, rhs):
        # solve the linear system
        from csdl.solvers.linear.direct import DirectSolver
        num_nodes = self.parameters['surface_shapes'][0][0]
        num_panels = self.compute_bound_aic_shape()[1]

        circulation_strength = self.create_output('circulation_strength', shape=(num_nodes, num_panels))

        for i in range(num_nodes):
            A = csdl.reshape(lhs_A[i,:,:], (num_panels, num_panels))
            rhs_i = csdl.reshape(rhs[i,:], (num_panels, ))
            # model.register_output('A', A)
            # model.register_output('rhs_i', rhs_i)
            sol = csdl.solve(A, -rhs_i, solver = DirectSolver())

            circulation_strength[i,:] = csdl.reshape(sol, circulation_strength[i,:].shape)


if __name__ == "__main__":
    import csdl
    from python_csdl_backend import Simulator
    from VAST.utils.generate_mesh import *

    # define mesh as the input to the model
    nc = 3
    ns = 11
    num_nodes = 2
    surface_shapes = [(num_nodes, nc, ns, 3)]
    surface_names = ['surface']
    n_wake_pts_chord=2

    # create a simple rectangular mesh
    mesh_dict = {
        "num_y": ns, "num_x": nc, "wing_type": "rect", "symmetry": False, "span": 10.0,
        "chord": 1, "span_cos_sppacing": 1.0, "chord_cos_sacing": 1.0,
    }
    # Generate mesh of a rectangular wing
    mesh = generate_mesh(mesh_dict)
    surface_mesh = [np.einsum('i,jkl->ijkl', np.ones((num_nodes)), mesh)]
    # Here, the mesh is checked to be the same as ex_1vlm_simulation_rec_wing.py in VAST 0.1.0

    # define frame velocity
    angle_of_attack_degree = np.array([5, -5])  # deg
    v_inf = 248.136 # m/s

    angle_of_attack_rad = np.deg2rad(angle_of_attack_degree)
    frame_vel_numpy = np.zeros((num_nodes, 3))
    frame_vel_numpy[:, 0] = -v_inf * np.cos(angle_of_attack_rad)
    frame_vel_numpy[:, 2] = -v_inf * np.sin(angle_of_attack_rad)


    # create a model
    model = csdl.Model()

    # create a csdl variable for the input mesh
    for surface_name, surface_mesh in zip(surface_names, surface_mesh):
        input_mesh = model.create_input(surface_name, surface_mesh)

    # create input for the frame velocity
    frame_vel = model.create_input('frame_vel', frame_vel_numpy)
    vlm_fixed_wake_model = VLMFixedWakeSystem(
        surface_names=surface_names,
        surface_shapes=surface_shapes,
        mesh_unit='m',
        problem_type='fixed_wake',
        num_wake_pts=2,
        delta_t=100.,
        compressible=False,
        Ma=None
    )
    model.add(vlm_fixed_wake_model, 'VLMFixedWakeSystem')
    sim = Simulator(model,display_scripts=True)
    sim.run()
