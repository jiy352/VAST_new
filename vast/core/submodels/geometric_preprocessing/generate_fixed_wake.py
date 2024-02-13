import csdl
import numpy as np

class WakeCoords(csdl.Model):
    """
    compute wake vortex coords given the vortex coords

    parameters
    ----------
    frame_vel[num_nodes,3] : csdl array
        inertia frame vel
    bd_vtx_coords[num_nodes,num_pts_chord, num_pts_span, 3] : csdl array
    bound vortices points

    Returns
    -------
    1. wake_coords[num_nodes, 2, num_pts_span-1, 3] : csdl array
        wake vortex coordianates    
    """
    def initialize(self):
        self.parameters.declare('surface_names', types=list)
        self.parameters.declare('surface_shapes', types=list)
        self.parameters.declare('n_wake_pts_chord')
        self.parameters.declare('delta_t')
        self.parameters.declare('TE_idx', default='last')

    def define(self):
        # add_input
        surface_names = self.parameters['surface_names']
        surface_shapes = self.parameters['surface_shapes']
        num_nodes = surface_shapes[0][0]
        n_wake_pts_chord = self.parameters['n_wake_pts_chord']  # number of wake nodes in streamwise direction
        delta_t = self.parameters['delta_t']
        TE_idx = self.parameters['TE_idx']

        wake_coords_names = [x + '_wake_coords' for x in surface_names]

        frame_vel = self.declare_variable('frame_vel', shape=(num_nodes, 3))

        for i in range(len(surface_names)):
            surface_name = surface_names[i]
            surface_shape = surface_shapes[i]
            bd_vtx_coords_shape = surface_shape
            bd_vtx_coords_name = surface_name + '_bd_vtx_coords'

            num_pts_chord = surface_shape[1]
            num_pts_span = surface_shape[2]

            bd_vtx_coords = self.declare_variable(bd_vtx_coords_name,
                                                  shape=bd_vtx_coords_shape)
            if TE_idx == 'first':
                TE = bd_vtx_coords[:, 0, :, :]
            elif TE_idx == 'last':
                TE = bd_vtx_coords[:, num_pts_chord - 1, :, :]

            TE_reshaped = csdl.reshape(TE, (num_nodes, num_pts_span, 3))
            TE_reshaped_expand = csdl.expand(
                TE_reshaped, (num_nodes, n_wake_pts_chord, num_pts_span, 3),
                'ijk->iljk')

            factor_var = np.einsum('i,jkl->jikl',
                                   np.arange(n_wake_pts_chord) * delta_t,
                                   np.ones((num_nodes, num_pts_span, 3)))
            factor = self.create_input(surface_name + '_factor',
                                       val=factor_var)
            #! TODO:! fix this for rotating surfaces
            # - should be fine actually just to align the wake w/ free stream
            delta_x = csdl.expand(-frame_vel,
                                  (num_nodes, n_wake_pts_chord, num_pts_span,
                                   3), 'il->ijkl') * factor
            wake_coords = TE_reshaped_expand + delta_x

            self.register_output(wake_coords_names[i], wake_coords)