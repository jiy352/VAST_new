import numpy as np
import pytest
import csdl
from python_csdl_backend import Simulator
from vast.utils.generate_rectangular_mesh import generate_rectangular_mesh  # function to generate a rectangular mesh
from vast.core.submodels.geometric_submodels.geometric_property_extraction import GeometricPropertyExtraction  # Adjust the import path according to your project structure



@pytest.fixture
def setup_mesh_to_vortex_mesh():
    # Setup for two surfaces with different shapes
    surface_names = ['wing', 'htail']
    surface_shapes = [(2, 4, 3, 3), (2, 5, 2, 3)]  # num_nodes, n_chord, n_span for each surface
    mesh_unit = 'm'
    parameters = {
        'surface_names': surface_names,
        'surface_shapes': surface_shapes,
        # 'mesh_unit': mesh_unit,
        # 'delta_t': 0,
        # 'problem_type': 'fixed_wake',
        # 'compressible': False,
        # 'Ma': None
    }
    return GeometricPropertyExtraction(**parameters)



# pytest -m unit_test -p no:warnings
@pytest.mark.unit_test
def test_geometry_property_extraction(setup_mesh_to_vortex_mesh):
    geo_extraction = setup_mesh_to_vortex_mesh
    model = csdl.Model()
    parameters = geo_extraction.parameters
    mesh_np_array_list = []
    for i in range(len(parameters['surface_names'])):
        surface_name = parameters['surface_names'][i]
        surface_shape = parameters['surface_shapes'][i]
        num_nodes, n_chord, n_span, _ = surface_shape
        
        # Generate input meshes for wing and htail
        mesh_np_array = generate_rectangular_mesh(n_chord, n_span, num_nodes=num_nodes)

        # create a csdl variable for the bound vortex coordinates
        expected_bound_vtx_coords = np.zeros((num_nodes, n_chord, n_span, 3))
        expected_bound_vtx_coords[:, 0:-1, :, :] = mesh_np_array[:, 0:-1, :, :] * .75 + mesh_np_array[:, 1:, :, :] * 0.25
        expected_bound_vtx_coords[:, -1, :, :]   = mesh_np_array[:, -1, :, :] + 0.25 * (mesh_np_array[:, -1, :, :] - mesh_np_array[:, -2, :, :])
    
        # create a csdl variable for the input mesh
        mesh = geo_extraction.create_input(surface_name, mesh_np_array)
        bound_vtx_coords = geo_extraction.create_input(f'{surface_name}_bound_vtx_coords', expected_bound_vtx_coords)
        mesh_np_array_list.append(mesh_np_array)

    # add the geo_extraction to the whole model
    model.add(geo_extraction,"GeometricPropertyExtraction")
    # add the model to the simulator and run it
    sim = Simulator(model)
    sim.run()

    system_size = 0
    bound_vec_list = []
    # Verify bound_vtx_coords for each surface
    for i in range(len(parameters['surface_names'])):
        surface_name = parameters['surface_names'][i]
        surface_shape = parameters['surface_shapes'][i]
        num_nodes, n_chord, n_span, _ = surface_shape
        mesh_np_array = mesh_np_array_list[i]
        
        bound_vtx_coords = sim[f'{surface_name}_bound_vtx_coords']
        
        # Extract the outputs from simulation
        collocation_points = sim[f'{surface_name}_collocation_pts']
        panel_areas = sim[f'{surface_name}_panel_areas']
        force_evaluation_pts = sim[f'{surface_name}_force_evaluation_pts']

        expected_collocation_points = np.zeros((num_nodes, n_chord-1, n_span-1, 3))
        expected_collocation_points = 0.25 * (bound_vtx_coords[:,0:-1, 0:-1, :] + bound_vtx_coords[:,1:, 1:, :])+\
                                      0.25 * (bound_vtx_coords[:,0:-1, 1:, :] + bound_vtx_coords[:,1:, 0:-1, :])
        np.testing.assert_almost_equal(collocation_points, expected_collocation_points, decimal=5, 
                                       err_msg=f"Collocation points incorrect for {surface_name}")
    
        expected_panel_areas = np.zeros((num_nodes, n_chord-1, n_span-1))
        expected_panel_areas = 0.5 * np.linalg.norm(np.cross(bound_vtx_coords[:,0:-1, 0:-1, :] - bound_vtx_coords[:,1:, 0:-1, :], 
                                                            bound_vtx_coords[:,0:-1, 0:-1, :] - bound_vtx_coords[:,0:-1, 1:, :]), axis=-1) +\
                               0.5 * np.linalg.norm(np.cross(bound_vtx_coords[:,1:, 1:, :] - bound_vtx_coords[:,1:, 0:-1, :], 
                                                            bound_vtx_coords[:,1:, 1:, :] - bound_vtx_coords[:,0:-1, 1:, :]), axis=-1)
        np.testing.assert_almost_equal(panel_areas, expected_panel_areas, decimal=5,
                                        err_msg=f"Panel areas incorrect for {surface_name}")
        
        expected_force_evaluation_pts = np.zeros((num_nodes, n_chord-1, n_span-1, 3))
        eval_pts_location = 0.25
        expected_force_evaluation_pts =  (
                    (1 - eval_pts_location) * 0.5 * mesh_np_array[:, 0:-1, 0:-1, :] + 
                    (1 - eval_pts_location) * 0.5 * mesh_np_array[:, 0:-1, 1:, :] +
                    eval_pts_location * 0.5 * mesh_np_array[:, 1:, 0:-1, :] +
                    eval_pts_location * 0.5 * mesh_np_array[:, 1:, 1:, :])
        
        np.testing.assert_almost_equal(force_evaluation_pts, expected_force_evaluation_pts, decimal=5,
                                       err_msg=f"Force evaluation points incorrect for {surface_name}")
        
        expected_bound_vecs_current = -(
                (0.75 * mesh_np_array[:, 0:-1, 0:-1, :] + 0.25 * mesh_np_array[:, 1:, 0:-1, :] -
                 0.75 * mesh_np_array[:, 0:-1, 1:, :] -0.25 * mesh_np_array[:, 1:, 1:, :]).reshape(num_nodes, (n_chord - 1) * (n_span - 1), 3))
        
        
        system_size += (n_chord - 1) * (n_span - 1)
        bound_vec_list.append(expected_bound_vecs_current)

    bound_vecs_all_surfaces = np.zeros((num_nodes, system_size, 3))
    start = 0
    for i in range(len(parameters['surface_names'])):
        surface_name = parameters['surface_names'][i]
        surface_shape = parameters['surface_shapes'][i]
        num_nodes, n_chord, n_span, _ = surface_shape
        num_panel = (n_chord - 1) * (n_span - 1)
        bound_vecs_all_surfaces[:, start: start+num_panel, :] = bound_vec_list[i]
        start += num_panel

    np.testing.assert_almost_equal(sim['bound_vecs_all_surfaces'], bound_vecs_all_surfaces, decimal=5,
                                      err_msg="Bound vectors incorrect")
