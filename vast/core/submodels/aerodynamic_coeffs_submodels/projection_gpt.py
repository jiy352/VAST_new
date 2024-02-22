import csdl

class Projection(csdl.Model):
    """
    A model for computing the projection of velocities onto normals, used for solving the flow tangency condition.

    Attributes
    ----------
    velocities : csdl.Array
        Array of velocities with shape (num_nodes, num_vel, 3). num_vel = (nx-1)*(ny-1).
    normals : csdl.Array
        Array of normals with shape (num_nodes, nx-1, ny-1, 3).

    Returns
    -------
    csdl.Array
        The projected norm of the velocities.
    """
    def initialize(self):
        self.parameters.declare('input_var_names', types=list)
        self.parameters.declare('normal_names', types=list)
        self.parameters.declare('output_var_name', types=str)
        self.parameters.declare('input_var_shapes', types=list)
        self.parameters.declare('normal_shapes', types=list)

    def define(self):
        inputs = self.parameters['input_var_names']
        normals = self.parameters['normal_names']
        output_name = self.parameters['output_var_name']
        input_shapes = self.parameters['input_var_shapes']
        normal_shapes = self.parameters['normal_shapes']
        num_nodes = normal_shapes[0][0]

        if len(input_shapes[0]) == 3:
            # project kinematic vel, or any other velcoity with shape (num_nodes, num_vel, 3)
            output_shape = self.calculate_output_shape_3D(input_shapes, num_nodes)
        elif len(input_shapes[0]) == 4:
            # project aic, or any other velocity with shape (num_nodes, num_vel_eval, num_vel_induce, 3)
            output_shape = self.calculate_output_shape_4D(input_shapes, num_nodes)

        if len(input_shapes[0]) == 3:
            # this is for projection of kinematic vel for multiple lifting surfaces
            self.project_velocities(inputs, normals, output_name, input_shapes, normal_shapes, num_nodes, output_shape)
        elif  len(input_shapes[0]) == 4:
            # projection for the whole AIC matrix
            self.project_aic(inputs[0], normal_shapes, output_name, input_shapes[0], num_nodes)

    def calculate_output_shape_3D(self, input_shapes, num_nodes):
        return (num_nodes, sum(shape[1] for shape in input_shapes))

    def calculate_output_shape_4D(self, input_shapes, num_nodes):
        return (num_nodes, sum(shape[1] + shape[2] for shape in input_shapes))

    def project_velocities(self, input_names, normal_names, output_name, input_shapes, normal_shapes, num_nodes, output_shape):
        output_vel = self.create_output(output_name, shape=output_shape)
        start = 0
        for input_name, normal_name, input_shape, normal_shape in zip(input_names, normal_names, input_shapes, normal_shapes):
            input_vel, normals_reshaped = self.prepare_variables(input_name, normal_name, input_shape, normal_shape, num_nodes)
            if len(input_shape) == 3:
                self.perform_projection_3D(input_vel, normals_reshaped, output_vel, start)
            elif len(input_shape) == 4:
                self.raise_dimension_error(input_name, normal_name, output_name)
            start += normals_reshaped.shape[1]

    def project_aic(self, input_name, normal_shapes, output_name, input_shape, num_nodes):
        normal_concatenated, start = self.concatenate_normals(normal_shapes, num_nodes, output_name)
        if len(input_shape) == 4:
            self.perform_projection_4D(input_name, normal_concatenated, output_name, input_shape)

    def prepare_variables(self, input_name, normal_name, input_shape, normal_shape, num_nodes):
        input_vel = self.declare_variable(input_name, shape=input_shape)
        normals = self.declare_variable(normal_name, shape=normal_shape)
        normals_reshaped = csdl.reshape(normals, new_shape=(num_nodes, normals.shape[1] * normals.shape[2], 3))
        return input_vel, normals_reshaped

    def perform_projection_3D(self, input_vel, normals_reshaped, output_vel, start):
        # velocity_projections = csdl.einsum(input_vel, normals_reshaped, subscripts='ijk,ijk->ij', partial_format='sparse')
        velocity_projections = csdl.sum(input_vel * normals_reshaped, axes=(2,))
        delta = velocity_projections.shape[1]
        output_vel[:, start:start + delta] = velocity_projections

    def perform_projection_4D(self, input_name, normal_concatenated, output_name, input_shape):
        input_vel = self.declare_variable(input_name, shape=input_shape)
        # velocity_projections = csdl.custom(input_vel, normal_concatenated, op=EinsumLijkLikLij(
        #     in_name_1=input_name, in_name_2='normal_concatenated' + '_' + output_name, in_shape=input_shape, out_name=output_name))
        shape = (normal_concatenated.shape[0],normal_concatenated.shape[1], input_vel.shape[2], normal_concatenated.shape[2])
        normal_concatenated_expand = csdl.expand(normal_concatenated, shape=shape, indices='ijk->ijlk')
        # print('normal_concatenated', normal_concatenated.shape)
        # print(normal_concatenated_expand.shape)
        # print(input_vel.shape)

        velocity_projections = csdl.sum(input_vel * normal_concatenated_expand, axes=(3,))
        self.register_output(output_name, velocity_projections)

    def concatenate_normals(self, normal_shapes, num_nodes, output_name):
        normal_concatenated_shape = (num_nodes,) + (sum(i[1] * i[2] for i in normal_shapes),) + (3,)
        normal_concatenated = self.create_output('normal_concatenated' + '_' + output_name, shape=normal_concatenated_shape)
        start = 0
        for i in range(len(normal_shapes)):
            normal_name = self.parameters['normal_names'][i]
            normal_shape = normal_shapes[i]
            normals = self.declare_variable(normal_name, shape=normal_shape)
            normals_reshaped = csdl.reshape(normals, new_shape=(num_nodes, normal_shape[1] * normal_shape[2], 3))
            delta = normals_reshaped.shape[1]
            normal_concatenated[:, start:start + delta, :] = normals_reshaped
            start += delta
        return normal_concatenated, start

    def raise_dimension_error(self, input_name, normal_name, output_name):
        print('Implementation error: the dimension of kinematic velocity should be 3')
        print(input_name, normal_name, output_name)
        exit()



if __name__ == "__main__":
    import time
    import timeit
    from vast.core.submodels.aerodynamic_coeffs_submodels.sub_aic_biot_savarts import SubAicBiotSavarts
    from vast.core.submodels.geometric_submodels.compute_normals import ComputeNormals
    # from vast.core.submodels.aerodynamic_coeffs_submodels.projection import Projection
    import csdl

    ts = time.time()
    from python_csdl_backend import Simulator
    import numpy as onp
    def generate_simple_mesh(nx, ny):
        mesh = onp.zeros((nx, ny, 3))
        mesh[:, :, 0] = onp.outer(onp.arange(nx), onp.ones(ny))
        mesh[:, :, 1] = onp.outer(onp.arange(ny), onp.ones(nx)).T
        mesh[:, :, 2] = 0.
        return mesh

    nc = 10
    ns = 11

    eval_pt_names = ['coll_pts']
    vortex_coords_names = ['vtx_pts']
    # eval_pt_shapes = [(nx, ny, 3)]
    # vortex_coords_shapes = [(nx, ny, 3)]

    eval_pt_shapes = [(1, nc-1, ns-1, 3)]
    vortex_coords_shapes = [(1, nc, ns, 3)]

    output_names = ['aic']

    model_1 = csdl.Model()


    vor_val = generate_simple_mesh(nc, ns).reshape(1, nc, ns, 3)
    col_val = 0.25 * (vor_val[:,:-1, :-1, :] + vor_val[:,:-1, 1:, :] +
                        vor_val[:,1:, :-1, :] + vor_val[:,1:, 1:, :])
    # col_val = generate_simple_mesh(nx, ny)

    vor = model_1.create_input('vtx_pts', val=vor_val)
    col = model_1.create_input('coll_pts', val=col_val)


    # compute normals
    model_1.add(ComputeNormals(
        surfaces_to_eval_normals=vortex_coords_names,
        normal_names=['vtx_pts'+'_normals'],
        surfaces_to_eval_normal_shapes=[vor.shape],
    ),
                name='ComputeNormal')

    # test if multiple ops work
    submodel=SubAicBiotSavarts( eval_pt_names=eval_pt_names,
                                eval_pt_shapes=eval_pt_shapes,
                                vortex_coords_names=vortex_coords_names,
                                vortex_coords_shapes=vortex_coords_shapes,
                                output_names=output_names,
                                symmetry=True,
                                vc=True)
    model_1.add(submodel,'SubAicBiotSavarts')

    submodel = Projection(
        input_var_names=output_names,
        normal_names=['vtx_pts'+'_normals'],
        output_var_name='aic_projection',
        input_var_shapes=[(1, (nc-1)*(ns-1),(nc-1)*(ns-1), 3)],
        normal_shapes=[(1, nc-1, ns-1, 3)]
    )


    model_1.add(submodel,'Projection')

    #####################
    # finshed adding model
    ####################
    sim = Simulator(model_1,display_scripts=True)
    print('time', time.time() - ts)
    sim.run()