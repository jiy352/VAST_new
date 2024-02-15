import csdl
import numpy as np
from lsdo_modules.module_csdl.module_csdl import ModuleCSDL

class MeshToVortexMesh(ModuleCSDL):
    """
    Convert a mesh coordianates for the lifting surfaces to a vortex mesh.
    The leading segment of the vortex ring is placed on the panel’s quarter chord line. 
    The vortex ring is shifted a quarter chord length.
    Please check the book "Low-Speed Aerodynamics" by Katz and Plotkin,
    page 420 subsession a. Choice of Singularity Element for more details.
    

    parameters
    ----------
    input_mesh_pts[num_nodes, n_chord, n_span 3] : csdl array
        variable name in csdl: <mesh_name> 
        Array defining the nodal coordinates of the lifting surface.
    
    returns
    ----------
    bound_vtx_coords[num_nodes, n_chord, n_span 3] : csdl array
        variable name in csdl: <mesh_name> + "_bound_vtx_coords" (e.g. wing_bound_vtx_coords)
        Array defining the nodal coordinates of the bound vortex mesh (shifted quarter chord).
    """

    def initialize(self):
        self.parameters.declare('surface_names', types=list)  # a list of surface names, e.g. ['wing', 'htail']
        self.parameters.declare('surface_shapes', types=list) # a list of surface shapes, e.g. [(num_nodes, n_chord_wing, n_span_wing), (num_nodes, n_chord_htail, n_span_htail)]
        # if the mesh is 'ft' in unit, we internally convert it to m
        self.parameters.declare('mesh_unit', default='m')
        # related to the starting wake for dynamic simulations
        self.parameters.declare('delta_t',default=0)
        self.parameters.declare('problem_type',default='fixed_wake')
        # properties for compressible flow
        self.parameters.declare('compressible',default=False)
        self.parameters.declare('Ma',default=None)

    def define(self):
        # load options
        surface_names = self.parameters['surface_names']
        surface_shapes = self.parameters['surface_shapes']
        mesh_unit = self.parameters['mesh_unit']
        num_nodes = surface_shapes[0][0] # here we assume all surfaces have the num_nodes
        # number of nodes: in fixed wake vlm, this is the number of aircraft/lifting surface states
        # that you want to solve in a vectorized manner,
        # e.g. angle of attach for 5, 10, 15 degrees, then num_nodes = 3

        delta_t = self.parameters['delta_t']
        problem_type = self.parameters['problem_type']
        compressible = self.parameters['compressible']
        Ma = self.parameters['Ma']       

        for i in range(len(surface_names)):
            # load name of the geometry mesh, number of points in chord and spanwise direction
            surface_name = surface_names[i]
            surface_shape = surface_shapes[i]

            num_pts_chord = surface_shape[1]
            num_pts_span = surface_shape[2]

            # get names of the output:
            bd_vtx_coords_name = surface_name + '_bound_vtx_coords'

            # add_input
            # declare the input variable lifting surface mesh,
            # this should come from CADDEE geometry if connected,
            # or up to the user to create an input if using the solver alone.

            if mesh_unit == 'm':
                mesh = self.register_module_input(surface_name, shape=surface_shape, promotes=True)
            elif mesh_unit == 'ft':
                mesh_ft = self.register_module_input(surface_name, shape=surface_shape, promotes=True)
                ft_to_m = 0.3048 # ft to m
                mesh = mesh_ft * ft_to_m
            
            if compressible:
                beta = (1-Ma**2)**0.5
                mesh_compressible = self.create_output(surface_name+'_compressible',shape=surface_shapes[i])
                mesh_compressible[:, :, :, 0] = mesh[:, :, :, 0] 
                mesh_compressible[:, :, :, 1] = mesh[:, :, :, 1] * beta
                mesh_compressible[:, :, :, 2] = mesh[:, :, :, 2] * beta

            #######################################
            # create the output: 1. bound_vtx_coords
            #######################################
            bound_vtx_coords = self.create_output(bd_vtx_coords_name, shape=(mesh.shape))
            # the 0th until the second last one chordwise is (0.75*leading lines of the vortex +0.25*leading lines of the vortex - shift 1/4 chordwise)
            bound_vtx_coords[:, 0:num_pts_chord-1, :, :] = mesh[:, 0:num_pts_chord - 1, :, :] * .75 + mesh[:, 1:num_pts_chord, :, :] * 0.25
            # the last one chordwise is 1/4 chord offset from the last chordwise panel
            if problem_type == 'fixed_wake':
                bound_vtx_coords[:, num_pts_chord-1, :, :] = mesh[:, num_pts_chord - 1, :, :] + 0.25 * (mesh[:, num_pts_chord - 1, :, :] - mesh[:, num_pts_chord -2, :, :])
                # in BYU lab VortexLattice.ji, the last one chordwise bd_vtx is the same as the TE panel, but in the book "Low-Speed Aerodynamics" by Katz and Plotkin, 
                # page 420 subsession a. Choice of Singularity Element, the last one chordwise bd_vtx is 1/4 chord offset from the last chordwise panel

            elif problem_type == 'prescribed_wake':
                # TODO: this needs to be updated for the dynamic simulations
                frame_vel = self.declare_variable('frame_vel', shape=(num_nodes, 3))
                w = self.declare_variable('w', shape=(num_nodes, 1))
                fs  = self.create_output('fs', shape=(num_nodes, 3))
                fs[:,0] = -frame_vel[:,0]
                fs[:,1] = -frame_vel[:,1]
                fs[:,2] = w

                eta = 0.25
                add_starting_wake = csdl.expand(fs*eta*delta_t,(num_nodes,1,num_pts_span,3),'il->ijkl')

                bound_vtx_coords[:, num_pts_chord -1, :, :] = mesh[:, num_pts_chord - 1, :, :] + add_starting_wake

                # bound_vtx_coords[:, num_pts_chord -
                #             1, :, :] = mesh[:, num_pts_chord -
                #                                 1, :, :] + 0.25 * (
                #                                     mesh[:, num_pts_chord -
                #                                             1, :, :] -
                #                                     mesh[:, num_pts_chord -
                #                                             2, :, :])

if __name__=='__main__':
    from vast.utils.generate_rectangular_mesh import generate_rectangular_mesh
    from python_csdl_backend import Simulator
    

    # generate a rectangular mesh
    num_nodes = 3
    nx = 10
    ny = 5
    mesh = generate_rectangular_mesh(nx, ny, num_nodes)

    model = csdl.Model()
    model.create_input('wing', mesh) # create a csdl variable for the input mesh
    parameters = {
        'surface_names': ['wing'],
        'surface_shapes': [(num_nodes, nx, ny, 3)],
        'mesh_unit': 'm',
        'delta_t': 0,
        'problem_type': 'fixed_wake',
        'compressible': False,
        'Ma': None
    }
    m2vm = MeshToVortexMesh(**parameters) # mesh 2 vortex mesh
    model.add(m2vm,'mesh_to_vortex_mesh')


    # add the model to the simulator and run it
    sim = Simulator(model)
    sim.run()

    # visualize the bound_vtx_coords
    import pyvista as pv

    bound_vtx_coords = sim['wing_bound_vtx_coords']
    x = bound_vtx_coords[0, :, :, 0] # just take the first node
    y = bound_vtx_coords[0, :, :, 1]
    z = bound_vtx_coords[0, :, :, 2]

    mesh_x = mesh[0, :, :, 0] # just take the first node
    mesh_y = mesh[0, :, :, 1]
    mesh_z = mesh[0, :, :, 2]

    # create a structured grid
    grid = pv.StructuredGrid(x, y, z)
    mesh_grid = pv.StructuredGrid(mesh_x, mesh_y, mesh_z)
    # plot and show grid only
    plotter = pv.Plotter()
    plotter.add_mesh(grid, color="blue", opacity=0.5, show_edges=True)
    plotter.add_mesh(mesh_grid, color="grey", opacity=0.3, show_edges=True)
    plotter.add_axes_at_origin(labels_off=True, line_width=5)
    plotter.show()

    
    