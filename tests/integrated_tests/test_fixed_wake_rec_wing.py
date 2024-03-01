import pytest
import csdl
import numpy as np
from python_csdl_backend import Simulator
from vast.core.vlm_fixed_wake_system_new import VLMFixedWakeSystem  # Ensure this import matches your project structure
from VAST.utils.generate_mesh import *


@pytest.fixture
def setup_vlm_fixed_wake_simulation():
    # Setup for two surfaces with different shapes
    surface_names = ['wing',]
    nc = 3
    ns = 11
    num_nodes = 2    
    surface_shapes = [(num_nodes, nc, ns, 3)] # num_nodes, n_chord, n_span for each surface
    mesh_unit = 'm'

    parameters = {
        'surface_names': surface_names,
        'surface_shapes': surface_shapes,
        'mesh_unit': mesh_unit,
        'problem_type': 'fixed_wake',
        'num_wake_pts': 2,
        'delta_t': 100.,
        'compressible': False,
        'Ma': None
    }

    mesh_dict = {
        "num_y": ns, "num_x": nc, "wing_type": "rect", "symmetry": False, "span": 10.0,
        "chord": 1, "span_cos_sppacing": 1.0, "chord_cos_sacing": 1.0,
    }

    # Generate mesh
    mesh = generate_mesh(mesh_dict)
    surface_mesh = [np.einsum('i,jkl->ijkl', np.ones((num_nodes)), mesh)]

    return parameters, surface_mesh

def test_vlm_fixed_wake_simulation(setup_vlm_fixed_wake_simulation):
    # extract inputs
    parameters, surface_mesh = setup_vlm_fixed_wake_simulation
    
    surface_names = parameters['surface_names']
    surface_shapes = parameters['surface_shapes']
    mesh_unit = parameters['mesh_unit']
    problem_type = parameters['problem_type']
    num_wake_pts = parameters['num_wake_pts']
    delta_t = parameters['delta_t']
    compressible = parameters['compressible']
    Ma = parameters['Ma']

    num_nodes = surface_shapes[0][0]
    

    # # Define mesh
    # mesh_dict = {
    #     "num_y": ns, "num_x": nc, "wing_type": "rect", "symmetry": False, "span": 10.0,
    #     "chord": 1, "span_cos_sppacing": 1.0, "chord_cos_sacing": 1.0,
    # }

    # # Generate mesh
    # mesh = generate_mesh(mesh_dict)
    # surface_mesh = [np.einsum('i,jkl->ijkl', np.ones((num_nodes)), mesh)]
    
    # Define frame velocity
    angle_of_attack_degree = np.array([5, -5])
    v_inf = 248.136
    angle_of_attack_rad = np.deg2rad(angle_of_attack_degree)
    frame_vel_numpy = np.zeros((num_nodes, 3))
    frame_vel_numpy[:, 0] = -v_inf * np.cos(angle_of_attack_rad)
    frame_vel_numpy[:, 2] = -v_inf * np.sin(angle_of_attack_rad)

    # Create and configure the model
    model = csdl.Model()
    for surface_name, surface_mesh in zip(surface_names, surface_mesh):
        model.create_input(surface_name, surface_mesh)
    frame_vel = model.create_input('frame_vel', frame_vel_numpy)
    model.add(VLMFixedWakeSystem(
        surface_names=surface_names,
        surface_shapes=surface_shapes,
        mesh_unit=mesh_unit,
        problem_type=problem_type,
        num_wake_pts=num_wake_pts,
        delta_t=delta_t,
        compressible=compressible,
        Ma=Ma
    ), 'VLMFixedWakeSystem')

    # Run the simulation
    sim = Simulator(model)
    sim.run()
    
    # Assertions
    # Here you should add assertions based on what you expect from your simulation.
    # For example:
    # assert sim.results['some_output'] == expected_value
    # This is a placeholder as you'll need to replace it with actual checks relevant to your simulation.
