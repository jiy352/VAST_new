import csdl
# from VAST.utils.custom_einsums import EinsumKijKijKi, EinsumLijkLikLij

class Projection(csdl.Model):
    """
    Compute the normal velocities used to solve the 
    flow tangency condition.

    parameters
    ----------
    velocities[num_nodes,num_vel, 3] : csdl array
        the velocities. num_vel = (nx-1)*(ny-1)
    normals[num_nodes,nx-1,ny-1, 3] : csdl array
        the normals.
    Returns
    -------
    projected velocities: 
    (always just return a single csdl variable no matter how many input variables)
    csdl array
        The projected norm of the velocities
    """
    def initialize(self):
        self.parameters.declare('input_var_names', types=list)
        self.parameters.declare('normal_names', types=list)

        self.parameters.declare('output_var_name', types=str)
        self.parameters.declare('input_var_shapes', types=list)
        self.parameters.declare('normal_shapes', types=list)

    def define(self):
        input_var_names = self.parameters['input_var_names']
        normal_names = self.parameters['normal_names']
        output_var_name = self.parameters['output_var_name']

        input_var_shapes = self.parameters['input_var_shapes']
        normal_shapes = self.parameters['normal_shapes']

        num_nodes = normal_shapes[0][0]

        # there should only be one concatenated output
        # for both kinematic vel and aic

        input_vel_shape_sum = 0

        # project kinematic vel
        if len(input_var_shapes[0]) == 3:
            output_shape = (num_nodes, sum((i[1]) for i in input_var_shapes))
        # project aic
        elif len(input_var_shapes[0]) == 4:
            output_shape = (num_nodes, +((sum(
                (i[1]) for i in input_var_shapes)) + (sum(
                    (i[2]) for i in input_var_shapes))))

        start = 0
        if len(input_var_names) > 1:
            # this if for projection of kinematic vel
            output_vel = self.create_output(output_var_name,
                                            shape=output_shape)

            for i in range(len(input_var_names)):

                # input_names
                input_vel_name = input_var_names[i]
                normal_name = normal_names[i]

                # input_shapes
                input_vel_shape = input_var_shapes[i]
                normal_shape = normal_shapes[i]

                # declare_inputs
                input_vel = self.declare_variable(input_vel_name,
                                                  shape=input_vel_shape)

                normals = self.declare_variable(normal_name,
                                                shape=normal_shape)
                # print('normals shape', normals.shape)
                normals_reshaped = csdl.reshape(
                    normals,
                    new_shape=(num_nodes, normals.shape[1] * normals.shape[2],
                               3))

                if len(input_vel_shape) == 3:
                    velocity_projections = csdl.einsum(
                        input_vel,
                        normals_reshaped,
                        subscripts='ijk,ijk->ij',
                        partial_format='sparse',
                    )
                elif len(input_vel_shape) == 4:
                    print(
                        'Implementation error the dim of kinematic vel should be 3'
                    )
                    print(input_vel_name, normal_name, output_var_name)
                    exit()

                delta = velocity_projections.shape[1]

                output_vel[:, start:start + delta] = velocity_projections
                start += delta

        elif len(input_var_names) == 1:
            # this if for projection of the whole aic matrix
            input_vel_name = input_var_names[0]
            input_vel_shape = input_var_shapes[0]
            # we need to concatenate the normal vectors
            # into a whole vec to project the assembled aic matrix

            normal_concatenated_shape = (num_nodes, ) + (sum(
                (i[1] * i[2]) for i in normal_shapes), ) + (3, )

            normal_concatenated = self.create_output(
                'normal_concatenated' + '_' + output_var_name,
                shape=normal_concatenated_shape)

            for i in range(len(normal_names)):

                # input_names

                normal_name = normal_names[i]

                # input_shapes

                normal_shape = normal_shapes[i]

                # declare_inputs
                input_vel = self.declare_variable(input_vel_name,
                                                  shape=input_vel_shape)

                normals = self.declare_variable(normal_name,
                                                shape=normal_shape)

                normals_reshaped = csdl.reshape(
                    normals,
                    new_shape=(num_nodes, normals.shape[1] * normals.shape[2],
                               3))
                if len(input_vel_shape) == 3:
                    # velocity_projections = csdl.custom(
                    #     input_vel,
                    #     normals_reshaped,
                    #     op=EinsumKijKijKi(in_name_1=input_vel_name,
                    #                       in_name_2=normals_reshaped.name,
                    #                       in_shape=input_vel.shape,
                    #                       out_name=output_var_name))
                    velocity_projections = csdl.einsum('kij,kij->ki',
                                                       input_vel,
                                                       normals_reshaped)
                    self.register_output(output_var_name, velocity_projections)
                delta = normals_reshaped.shape[1]
                normal_concatenated[:,
                                    start:start + delta, :] = normals_reshaped

                start += delta

            if len(input_vel_shape) == 4:


                # velocity_projections = csdl.custom(
                #     input_vel,
                #     normal_concatenated,
                #     op=EinsumLijkLikLij(in_name_1=input_vel_name,
                #                         in_name_2='normal_concatenated' + '_' +
                #                         output_var_name,
                #                         in_shape=input_vel.shape,
                #                         out_name=output_var_name))
                velocity_projections = csdl.einsum('lijk,lik->lij',
                                                   input_vel,
                                                   normal_concatenated)

                self.register_output(output_var_name, velocity_projections)