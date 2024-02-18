import csdl

class kinematicVelocityModel(csdl.Model):
    """
    Compute the kinematic velocity.

    Parameters
    ----------
    frame_vel : numpy array
        The frame velocity of the flow.

    Returns
    -------
    kinematic_vel[nx-1, ny-1, 3] : numpy array
        The kinematic velocity of the flow.
    """
    def initialize(self):
        self.parameters.declare('surface_names', types=list)
        self.parameters.declare('surface_shapes', types=np.ndarray)

    def define(self):
        num_nodes = self.parameters['surface_shapes'][0][0]

        frame_vel = self.declare_variable('frame_vel', shape=(num_nodes, 3))
        for surface_name, surface_shape in zip(surface_names, surface_shapes):
            num_pts_chord = surface_shape[1]
            num_pts_span = surface_shape[2]

            kinematic_vel = -csdl.expand(frame_vel, (num_nodes, (num_pts_chord-1)* (num_pts_span-1), 3), 'ik->ijk')
            # register the kinematic velocity
            self.register_output(surface_name + '_kinematic_vel', kinematic_vel)