import numpy as np
import pytest
import csdl
from python_csdl_backend import Simulator
from vast.utils.generate_rectangular_mesh import generate_rectangular_mesh  # function to generate a rectangular mesh
from vast.core.submodels.geometric_submodels.mesh_to_vortex_mesh import MeshToVortexMesh  

@pytest.fixture
def setup_mesh_to_vortex_mesh():
    # Setup for two surfaces with different shapes
    surface_names = ['wing', 'htail']
    surface_shapes = [(2, 4, 3, 3), (2, 5, 2, 3)]  # num_nodes, n_chord, n_span for each surface
    mesh_unit = 'm'
    parameters = {
        'surface_names': surface_names,
        'surface_shapes': surface_shapes,
        'mesh_unit': mesh_unit,
        'delta_t': 0,
        'problem_type': 'fixed_wake',
        'compressible': False,
        'Ma': None
    }
    return MeshToVortexMesh(**parameters)

# pytest -m unit_test -p no:warnings
@pytest.mark.unit_test
def test_bound_mesh_value(setup_mesh_to_vortex_mesh):
    m2vm = setup_mesh_to_vortex_mesh
    model = csdl.Model()
    parameters = m2vm.parameters
    mesh_np_array_list = []
    for i in range(len(parameters['surface_names'])):
        surface_name = parameters['surface_names'][i]
        surface_shape = parameters['surface_shapes'][i]
        num_nodes, n_chord, n_span, _ = surface_shape
        
        # Generate input meshes for wing and htail
        mesh_np_array = generate_rectangular_mesh(n_chord, n_span, num_nodes=num_nodes)
        mesh_np_array_list.append(mesh_np_array)
    
        # create a csdl variable for the input mesh
        mesh = m2vm.create_input(surface_name, mesh_np_array)

    # add the m2vm to the whole model
    model.add(m2vm,"MeshToVortexMesh")
    # add the model to the simulator and run it
    sim = Simulator(model)
    sim.run()


    # Verify bound_vtx_coords for each surface
    for i in range(len(parameters['surface_names'])):
        surface_name = parameters['surface_names'][i]
        surface_shape = parameters['surface_shapes'][i]
        num_nodes, n_chord, n_span, _ = surface_shape
        mesh_np_array = mesh_np_array_list[i]
        
        bound_vtx_coords = sim[f'{surface_name}_bound_vtx_coords']
        
        # Check the quarter chord offset logic for the bound vortex coordinates
        # For simplicity, this example checks only the shift and does not fully validate all values
        expected_bound_vtx_coords = np.zeros((num_nodes, n_chord, n_span, 3))
        expected_bound_vtx_coords[:, 0:-1, :, :] = mesh_np_array[:, 0:-1, :, :] * .75 + mesh_np_array[:, 1:, :, :] * 0.25
        expected_bound_vtx_coords[:, -1, :, :]   = mesh_np_array[:, -1, :, :] + 0.25 * (mesh_np_array[:, -1, :, :] - mesh_np_array[:, -2, :, :])
        np.testing.assert_almost_equal(bound_vtx_coords, expected_bound_vtx_coords, decimal=5, 
                                       err_msg=f"Bound vortex coords quarter chord offset incorrect for {surface_name}")

