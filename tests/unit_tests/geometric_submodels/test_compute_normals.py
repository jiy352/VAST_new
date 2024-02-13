import numpy as np
import pytest
import csdl
from python_csdl_backend import Simulator
from vast.utils.generate_rectangular_mesh import generate_rectangular_mesh  # function to generate a rectangular mesh
from vast.core.submodels.geometric_preprocessing.compute_normals import ComputeNormals 


def generate_test_surface(nx, ny):
    """
    Generate a simple rectangular mesh for testing.
    """
    x = np.linspace(0, 1, nx)
    y = np.linspace(0, 1, ny)
    xv, yv = np.meshgrid(x, y)
    # Generate simple z values to create a tilted plane
    zv = xv * 0.1 + yv * np.random.rand(1)
    return np.stack((xv, yv, zv), axis=-1)

@pytest.fixture
def setup_normals_computation():
    nx, ny = 4, 5  # Define mesh dimensions
    nx_1, ny_1 = 3, 4  # Define mesh dimensions
    surface_mesh = generate_test_surface(nx, ny).reshape(1, nx, ny, 3)
    surface_mesh_1 = generate_test_surface(nx_1, ny_1).reshape(1, nx_1, ny_1, 3)
    surface_meshes = [surface_mesh, surface_mesh_1]
    surface_names = ['test_surface', 'test_surface_1']
    normals_names = ['test_normals', 'test_normals_1']
    parameters = {
        'surfaces_to_eval_normals': surface_names,
        'normals_names': normals_names,
        'surfaces_to_eval_normal_shapes': [(1, nx, ny, 3), (1, nx_1, ny_1, 3),]
    }
    return ComputeNormals(**parameters), surface_names, surface_meshes, normals_names

@pytest.mark.unit_test
def test_compute_normals(setup_normals_computation):
    compute_normals, surface_names, surface_meshes, normals_names = setup_normals_computation

    model = csdl.Model()
    for i in range(len(surface_names)):
        surface_name = surface_names[i]
        surface_mesh = surface_meshes[i]
        model.create_input(surface_name, surface_mesh)  # create a csdl variable for the input mesh
    model.add(compute_normals, "ComputeNormals")

    # Create a simulator and run it
    sim = Simulator(model)
    # Manually set the input surface mesh
    sim.run()
    # Verify the computed normals
    for i in range(len(surface_names)):
        surface_name = surface_names[i]
        normals_name = normals_names[i]
        surface_mesh = surface_meshes[i]
        normals = sim[normals_name]

        # Verify the computed normals
        for i in range(normals.shape[0]):
            for j in range(normals.shape[1]):
                # Verify the computed normals are perpendicular to the surface
                assert np.isclose(np.dot(normals[0, i, j, :], surface_mesh[0, i, j, :]), 0)
                # Verify the computed normals are unit vectors
                assert np.isclose(np.linalg.norm(normals[0, i, j, :]), 1)