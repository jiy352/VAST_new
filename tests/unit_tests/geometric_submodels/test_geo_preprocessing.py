import numpy as np
import pytest
from vast.core.submodels.geometric_preprocessing.mesh_to_vortex_mesh import MeshToVortexMesh  # Adjust the import path according to your project structure


@pytest.fixture
def setup_mesh_to_vortex_mesh():
    # Setup for two surfaces with different shapes
    surface_names = ['wing', 'htail']
    surface_shapes = [(2, 4, 3), (2, 5, 2)]  # num_nodes, n_chord, n_span for each surface
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

def test_bound_mesh_value(setup_mesh_to_vortex_mesh):
    m2vm = setup_mesh_to_vortex_mesh
    # Generate input meshes for wing and htail
    wing_mesh = generate_rectangular_mesh(4, 3, num_nodes=2)
    htail_mesh = generate_rectangular_mesh(5, 2, num_nodes=2)
    
    # Assuming a method to set the input meshes exists
    m2vm.set_input_mesh('wing', wing_mesh)
    m2vm.set_input_mesh('htail', htail_mesh)

    # Trigger the computation or define logic to simulate the conversion
    m2vm.compute()  # Hypothetical method to trigger computation
    
    # Verify bound_vtx_coords for each surface
    for surface_name, shape in zip(['wing', 'htail'], [(2, 4, 3), (2, 5, 2)]):
        num_nodes, n_chord, n_span = shape
        bound_vtx_coords = m2vm.get_output(f'{surface_name}_bound_vtx_coords')  # Hypothetical method to get output
        
        # Check the quarter chord offset logic for the bound vortex coordinates
        # For simplicity, this example checks only the shift and does not fully validate all values
        expected_last_chord_offset = 0.25 * (bound_vtx_coords[:, n_chord-2, :, :] - bound_vtx_coords[:, n_chord-3, :, :])
        actual_last_chord_offset = bound_vtx_coords[:, n_chord-1, :, :] - bound_vtx_coords[:, n_chord-2, :, :]
        np.testing.assert_almost_equal(actual_last_chord_offset, expected_last_chord_offset, decimal=5, 
                                       err_msg=f"Bound vortex coords quarter chord offset incorrect for {surface_name}")

# Note: You would need to adjust the implementation details (like `set_input_mesh`, `compute`, `get_output`) 
# according to your actual class methods.