import csdl


class ComputeNormals(csdl.Model):
    """
    Compute normals.

    parameters
    ----------
    surfaces_to_eval_normals[nx, ny, 3] : numpy array
        Array defining the coordiantes of the lifting surface to evaluate the normals.

    Attributes
    ----------
    surfaces_to_eval_normals : list
        List of arrays defining the coordinates of the lifting surface to evaluate the normals.
    normals_names : list
        List of names for the normals to be computed.
    surfaces_to_eval_normal_shapes : list
        List of shapes corresponding to each surface in `surfaces_to_eval_normals`.

    Returns
    -------
    normals[nx-1, ny-1, 3] : numpy array
        The normals of each vortex panel
    """
    def initialize(self):
        self.parameters.declare('surfaces_to_eval_normals', types=list)
        self.parameters.declare('normals_names', types=list)

        self.parameters.declare('surfaces_to_eval_normal_shapes', types=list)

    def define(self):
        surfaces = self.parameters['surfaces_to_eval_normals']
        normals_names = self.parameters['normals_names']
        shapes = self.parameters['surfaces_to_eval_normal_shapes']

        for i, surface_name in enumerate(surfaces):
            normals_name = normals_names[i]
            shape = shapes[i]
            self.compute_normals(surface_name, normals_name, shape)

    def compute_normals(self, surface_name, normals_name, shape):
        """
        Compute and register normals for a given surface.

        Parameters
        ----------
        surface_name : str
            Name of the surface variable.
        normals_name : str
            Name for the output normals.
        shape : tuple
            Shape of the surface array.
        """
        # declare_inputs
        surface_coords = self.declare_variable(surface_name, shape=shape)
        # i an j vectors are the diagonals of the panels
        i_vector = surface_coords[:, :-1, 1:, :] - surface_coords[:, 1:, :-1, :]
        j_vector = surface_coords[:, :-1, :-1, :] - surface_coords[:, 1:, 1:, :]
        normals = csdl.cross(i_vector, j_vector, axis=3)
        norms = (csdl.sum(normals**2, axes=(3, )))**0.5
        norms_expanded = csdl.expand(norms, norms.shape + (3, ), 'ijk->ijkl')
        normals_normalized = normals / norms_expanded
        self.register_output(normals_name, normals_normalized)

if __name__ == "__main__":
    import numpy as np
    import python_csdl_backend
    def generate_simple_mesh(nx, ny, n_wake_pts_chord=None):
        if n_wake_pts_chord == None:
            mesh = np.zeros((nx, ny, 3))
            mesh[:, :, 0] = np.outer(np.arange(nx), np.ones(ny))
            mesh[:, :, 1] = np.outer(np.arange(ny), np.ones(nx)).T
            mesh[:, :, 2] = 0.
        else:
            mesh = np.zeros((n_wake_pts_chord, nx, ny, 3))
            for i in range(n_wake_pts_chord):
                mesh[i, :, :, 0] = np.outer(np.arange(nx), np.ones(ny))
                mesh[i, :, :, 1] = np.outer(np.arange(ny), np.ones(nx)).T
                mesh[i, :, :, 2] = 0.
        return mesh

    num_nodes = 3
    vortex_coords_names = ['v1', 'v2']
    normals_names = ['n1', 'n2']
    vortex_coords_shapes = [(num_nodes, 2, 3, 3), (num_nodes, 3, 4, 3)]

    model_1 = csdl.Model()
    v1_val = generate_simple_mesh(2, 3, num_nodes)
    v2_val = generate_simple_mesh(3, 4, num_nodes)

    v1 = model_1.create_input('v1', val=v1_val)
    v2 = model_1.create_input('v2', val=v2_val)
    model_1.add(ComputeNormals(
        surfaces_to_eval_normals=vortex_coords_names,
        normals_names=normals_names,
        surfaces_to_eval_normal_shapes=vortex_coords_shapes,
    ),
                name='ComputeNormal')
    sim = python_csdl_backend.Simulator(model_1)
    # sim.visualize_implementation()
    sim.run()
