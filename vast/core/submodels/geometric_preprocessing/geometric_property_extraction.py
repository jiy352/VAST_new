import csdl
import numpy as np
from lsdo_modules.module_csdl.module_csdl import ModuleCSDL

# TODO: compute local Reynolds number in some other file

class GeometricPropertyExtraction(csdl.Model):
    """
    Compute various geometric properties for VLM analysis.

    parameters
    ----------
    bound_vtx_coords[num_nodes,num_pts_chord, num_pts_span, 3] : csdl array
        Array defining the nodal coordinates of the lifting surface.
    mesh[num_nodes, num_pts_chord, num_pts_span, 3] : csdl array
        Array defining the nodal coordinates of the lifting surface.
    Returns
    -------
    1. f'{surface_name}_collocation_points':[num_nodes, num_pts_chord-1, num_pts_span-1, 3] : csdl array
        collocation points for the horseshoe vortices, found along the 3/4 chord.
    2. f'{surface_name}_panel_areas' [num_nodes, (num_pts_chord-1), (num_pts_span-1)]: csdl array
        The panel areas.
    4. f'{surface_name}_force_evaluation_pts'
    3. 'bound_vecs_all_surfaces': [num_nodes,system_size,3]: bound vectors of all lifting surfaces
    
    """

    def initialize(self):
        self.parameters.declare('surface_names', types=list)
        self.parameters.declare('surface_shapes', types=list)

    def define(self):
        surface_names = self.parameters['surface_names']
        surface_shapes = self.parameters['surface_shapes']

        mesh_list = []  # list of mesh for each surface
        
        for surface_name, surface_shape in zip(surface_names, surface_shapes):
            bound_vtx_shape = surface_shape
            bound_vtx_coords = self.declare_variable(f'{surface_name}_bound_vtx_coords', shape=bound_vtx_shape)
            collocation_points = self.compute_collocation_points(bound_vtx_coords, bound_vtx_shape)
            self.register_output(f'{surface_name}_collocation_points', collocation_points)

            panel_areas = self.compute_panel_areas(bound_vtx_coords)
            self.register_output(f'{surface_name}_panel_areas', panel_areas)

            mesh = self.declare_variable(surface_name , shape=surface_shape)
            force_evaluation_pts = self.mesh_to_evaluation_points(mesh)
            self.register_output(f'{surface_name}_force_evaluation_pts', force_evaluation_pts)

            mesh_list.append(mesh)

        # Compute the bound vectors of all lifting surfaces
        # 'bound_vecs_all_surfaces' shape is (num_nodes, system_size, 3)
        self.compute_bound_vectors(mesh_list)
        # bound vector has been created in the compute_bound_vectors function

    def compute_collocation_points(self, bound_vtx_coords, shape):
        '''
        collocation points for the horseshoe vortices, found along the 3/4 chord.
        The collocation points are found by taking the average of the four bound vertices of each panel.
        The shape of the collocation points is (num_nodes, num_pts_chord-1, num_pts_span-1, 3)
        because this is the number of panels in the chordwise and spanwise directions.
        Parameters:
        - bound_vtx_coords: csdl.Array
            The bound vortex coordinates of the lifting surface.

        Returns:
        - Collocation points: csdl.Array
        '''
        shape = bound_vtx_coords.shape
        num_nodes = bound_vtx_coords.shape[0]
        num_pts_chord = shape[1]
        num_pts_span = shape[2]
        # coll_pts_coords = def_mesh[:, 0:num_pts_chord -1, :, :] * .25 + def_mesh[:, 1:num_pts_chord, :, :] * 0.75
        collocation_points = 0.25 * (bound_vtx_coords[:,0:num_pts_chord-1, 0:num_pts_span-1, :] +\
                                        bound_vtx_coords[:,0:num_pts_chord-1, 1:num_pts_span, :] +\
                                        bound_vtx_coords[:,1:, 0:num_pts_span-1, :]+\
                                        bound_vtx_coords[:,1:, 1:, :])
        return collocation_points      


    def compute_panel_areas(self, bound_vtx_coords):
        """
        Compute the areas of panels defined by bound vortex coordinates.

        Parameters:
        - bound_vtx_coords: csdl.Array
            The bound vortex coordinates of the lifting surface.

        Returns:
        - Panel areas: csdl.Array 
        """
        # compute the two diagonals of the panel:
        i = bound_vtx_coords[:, :-1, 1:,  :] - bound_vtx_coords[:, 1:, :-1, :]
        j = bound_vtx_coords[:, :-1, :-1, :] - bound_vtx_coords[:, 1:, 1:,  :]
        # compute the panel area:
        normals = csdl.cross(i, j, axis=3)
        s_panels = (csdl.sum(normals**2, axes=(3, )))**0.5 * 0.5
        return s_panels
    
    def mesh_to_evaluation_points(self, mesh, eval_pts_option='auto', eval_pts_location=0.25):
        """
        Compute force evaluation points based on mesh data.

        Parameters:
        - surface_name (str): Name of the surface.
        - surface_shape (tuple): Shape of the mesh for the surface.

        Returns:
        - Evaluation points for the wake and bound vortices: csdl.Array
        """
        if eval_pts_option == 'auto':
            eval_pts_coords = (
                    (1 - eval_pts_location) * 0.5 * mesh[:, 0:-1, 0:-1, :] + 
                    (1 - eval_pts_location) * 0.5 * mesh[:, 0:-1, 1:, :] +
                    eval_pts_location * 0.5 * mesh[:, 1:, 0:-1, :] +
                    eval_pts_location * 0.5 * mesh[:, 1:, 1:, :])

        return eval_pts_coords
    
    def compute_bound_vectors(self, mesh_list):
        """
        Compute the bound vectors of all lifting surfaces.

        This method aggregates the bound vectors from each mesh in the mesh_list,
        calculating the vector differences to determine the bound vectors for each panel,
        and then concatenating these vectors to form a complete set for all surfaces.

        Parameters:
        - mesh_list: List[csdl.Array]
            A list of CSDL arrays representing the mesh for each lifting surface.

        Returns:
        - The concatenated bound vectors for all lifting surfaces: csdl.Array
        """
        system_size = sum((mesh.shape[1] - 1) * (mesh.shape[2] - 1) for mesh in mesh_list)
        num_nodes = mesh_list[0].shape[0]

        bound_vecs_all = self.create_output('bound_vecs_all_surfaces', shape=(num_nodes, system_size, 3))
        start = 0
        for i in range(len(mesh_list)):
            # load name of the geometry mesh, number of points in chord and spanwise direction
            mesh = mesh_list[i]
            surface_name = mesh.name
            num_pts_chord = mesh.shape[1]
            num_pts_span = mesh.shape[2]

            delta = (num_pts_chord - 1) * (num_pts_span - 1)
            # TODO: check this negative sign
            bound_vecs_current_surface = -csdl.reshape(
                (0.75 * mesh[:, 0:-1, 0:-1, :] + 0.25 * mesh[:, 1:, 0:-1, :] -
                 0.75 * mesh[:, 0:-1, 1:, :] -0.25 * mesh[:, 1:, 1:, :]),
                new_shape=(num_nodes, (num_pts_chord - 1) * (num_pts_span - 1), 3))
            # self.register_output(f'{surface_name}_bound_vecs', bound_vecs_current_surface)
            bound_vecs_all[:, start:start + delta, :] = bound_vecs_current_surface
            start += delta

if __name__=='__main__':
    from vast.utils.generate_rectangular_mesh import generate_rectangular_mesh
    from python_csdl_backend import Simulator
