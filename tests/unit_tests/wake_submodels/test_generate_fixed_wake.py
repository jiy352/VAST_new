import numpy as np
import pytest
import csdl
from python_csdl_backend import Simulator
from vast.core.submodels.wake_submodels.generate_fixed_wake import GenerateFixedWake  # Adjust this import to your project structure

def generate_simple_mesh(num_nodes, num_pts_chord, num_pts_span, offset=0):
    """
    Generates a simple mesh for testing.
    """
    mesh = np.zeros((num_nodes, num_pts_chord, num_pts_span, 3))
    for i in range(num_nodes):
        mesh[i, :, :, 0] = np.outer(np.arange(num_pts_chord), np.ones(num_pts_span))
        mesh[i, :, :, 1] = np.outer(np.ones(num_pts_chord), np.arange(num_pts_span)) + offset
        mesh[i, :, :, 2] = 0.
    return mesh

@pytest.fixture
def setup_model():
    """
    Setup fixture for testing GenerateFixedWake.
    """
    n_wake_pts_chord = 10
    num_pts_chord = 3
    num_pts_span = 4
    num_nodes = 2
    delta_t = 0.1
    surface_names = ['wing_1', 'wing_2']
    surface_shapes = [
        (num_nodes, num_pts_chord, num_pts_span, 3),
        (num_nodes, num_pts_chord + 1, num_pts_span + 1, 3)
    ]

    wing_1_mesh = generate_simple_mesh(num_nodes, num_pts_chord, num_pts_span)
    wing_2_mesh = generate_simple_mesh(num_nodes, num_pts_chord + 1, num_pts_span + 1, offset=10)
    frame_vel = np.array([[-1, 0, -0.2], [-1, 0, 0.2]])

    return {
        'surface_names': surface_names,
        'surface_shapes': surface_shapes,
        'n_wake_pts_chord': n_wake_pts_chord,
        'delta_t': delta_t,
        'wing_1_mesh': wing_1_mesh,
        'wing_2_mesh': wing_2_mesh,
        'frame_vel': frame_vel
    }

@pytest.mark.unit_test
@pytest.mark.parametrize('surface_idx', [0, 1])
def test_generate_fixed_wake(setup_model, surface_idx):
    """
    Test GenerateFixedWake model.
    """
    params = setup_model
    model = csdl.Model()

    # Inputs
    model.create_input('frame_vel', val=params['frame_vel'])
    model.create_input(f'{params["surface_names"][surface_idx]}_bd_vtx_coords', val=params[f'wing_{surface_idx + 1}_mesh'])

    # Model
    model.add(GenerateFixedWake(
        surface_names=params['surface_names'],
        surface_shapes=params['surface_shapes'],
        n_wake_pts_chord=params['n_wake_pts_chord'],
        delta_t=params['delta_t'],
    ), name='WakeCoords')

    # Simulation
    sim = Simulator(model)
    sim.run()

    # Assertions
    frame_vel = params['frame_vel']
    delta_t = params['delta_t']
    n_wake_pts_chord = params['n_wake_pts_chord']

    # Expected behavior: Wake extends from TE in the direction opposite to frame velocity
    # For simplicity, consider the x-direction velocity and its effect on the x-coordinate of wake points
    for surface_name in params['surface_names']:
        for num_nodes in range(params['surface_shapes'][surface_idx][0]):
            for i in range(1, n_wake_pts_chord):
                wake_coords = sim[surface_name + '_wake_coords']
                expected_distance_vector = -frame_vel[num_nodes, :] * delta_t * i  # Assuming uniform frame_vel for all nodes here
                # Check the coordinate offset for the first wake point from the TE for all spanwise points
                actual_x_offset = wake_coords[num_nodes, i, :, :] - wake_coords[num_nodes, 0, :, :]
                assert np.allclose(actual_x_offset, expected_distance_vector, atol=1e-3), f"Incorrect x-offset for wake point {i}"
