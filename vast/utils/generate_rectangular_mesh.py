
import numpy as np

def generate_rectangular_mesh(nx, ny, num_nodes=None):
    if num_nodes is None:
        mesh = np.zeros((nx, ny, 3))
        mesh[:, :, 0] = np.outer(np.arange(nx), np.ones(ny))
        mesh[:, :, 1] = np.outer(np.ones(nx), np.arange(ny))
        mesh[:, :, 2] = 0.
    else:
        mesh = np.zeros((num_nodes, nx, ny, 3))
        for i in range(num_nodes):
            mesh[i, :, :, 0] = np.outer(np.arange(nx), np.ones(ny))
            mesh[i, :, :, 1] = np.outer(np.ones(nx), np.arange(ny))
            mesh[i, :, :, 2] = 0.
    return mesh


