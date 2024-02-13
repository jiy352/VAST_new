import numpy as np
import pytest
import csdl
from python_csdl_backend import Simulator
# Ensure the import path is correct for your project structure
from vast.utils.generate_rectangular_mesh import generate_rectangular_mesh
from vast.core.submodels.aerodynamic_coeffs_submodels.sub_aic_biot_savarts import SubAicBiotSavarts

@pytest.fixture
def setup_sub_aic_biot_savarts():
    # Define parameters for the test
    num_nodes = 1
    n_chord_eval = 3
    n_span_eval = 3
    n_chord_vortex = 4
    n_span_vortex = 5

    eval_pts_mesh = generate_rectangular_mesh(n_chord_eval, n_span_eval, num_nodes=num_nodes)
    vortex_coords_mesh = generate_rectangular_mesh(n_chord_vortex, n_span_vortex, num_nodes=num_nodes) + np.random.rand(num_nodes, n_chord_vortex, n_span_vortex, 3)

    eval_pt_names = ['eval_pts']
    vortex_coords_names = ['vortex_coords']
    output_names = ['aic']
    eval_pt_shapes = [(num_nodes, n_chord_eval, n_span_eval, 3)]
    vortex_coords_shapes = [(num_nodes, n_chord_vortex, n_span_vortex, 3)]

    parameters = {
        'eval_pt_names': eval_pt_names,
        'eval_pt_shapes': eval_pt_shapes,
        'vortex_coords_names': vortex_coords_names,
        'vortex_coords_shapes': vortex_coords_shapes,
        'output_names': output_names,
        'vc': True,
        'eps': 5e-4,
        'symmetry': False
    }

    sab = SubAicBiotSavarts(**parameters)

    return sab, eval_pts_mesh, vortex_coords_mesh

@pytest.mark.unit_test
def test_aic_computation(setup_sub_aic_biot_savarts):
    sab, eval_pts_mesh, vortex_coords_mesh = setup_sub_aic_biot_savarts
    model = csdl.Model()

    # Create CSDL variables for the input meshes
    model.create_input(sab.parameters['eval_pt_names'][0], val=eval_pts_mesh)
    model.create_input(sab.parameters['vortex_coords_names'][0], val=vortex_coords_mesh)

    # Add the SubAicBiotSavarts model to the overall model
    model.add(sab, "SubAicBiotSavartsModel")

    # Run the simulation
    sim = Simulator(model)
    sim.run()
    np.testing.assert_warns(UserWarning, sim.check_partials, compact_print=True)
    '''
    # Fetch the computed AIC
    aic_computed = sim[sab.parameters['output_names'][0]]

    # Define the expected AIC based on your specific use case
    aic_expected = np.zeros_like(aic_computed)  # Placeholder for actual expected AIC values

    # Verify the AIC computation
    np.testing.assert_almost_equal(aic_computed, aic_expected, decimal=5,
                                   err_msg="Test AIC computation has not been implemented.")
    '''