import csdl
import numpy as np
# from VAST.utils.custom_array_indexing import MatrixIndexing
# from VAST.utils.custom_find_zeros_replace_eps import ReplaceZeros
# from VAST.utils.custom_einsums import EinsumKijKijKi
# from VAST.utils.custom_expands import ExpandIjkIjlk
# from VAST.utils.custom_expands import ExpandIjkIljk

class SubAicBiotSavarts(csdl.Model):
    """
    Compute AIC.

    parameters
    ----------
    eval_pts[num_nodes,nc, ns, 3] : numpy array
        Array defining the nodal coordinates of the lifting surface that the 
        AIC matrix is computed on.
    vortex_coords[num_nodes,nc_v, ns_v, 3] : numpy array
        Array defining the nodal coordinates of background mesh that induces
        the AIC.

    Returns
    -------
    AIC[nc*ns*(nc_v-1)*(ns_v-1), nc*ns*(nc_v-1)*(ns_v-1), 3] : numpy array
        Aerodynamic influence coeffients (can be interprete as induced
        velocities given circulations=1)
    2023-06-13: 
        need to check the node order and the bound vector against OAS
    """
    def initialize(self):
        # evaluation points names and shapes
        self.parameters.declare('eval_pt_names', types=list)
        self.parameters.declare('eval_pt_shapes', types=list)
        # induced background mesh names and shapes
        self.parameters.declare('vortex_coords_names', types=list)
        self.parameters.declare('vortex_coords_shapes', types=list)
        # output aic names
        self.parameters.declare('output_names', types=list)
        # whether to enable the fixed vortex core model
        self.parameters.declare('vc', default=False)
        self.parameters.declare('eps', default=5e-4)

        self.parameters.declare('circulation_names', default=None)
        self.parameters.declare('symmetry',default=False)
        # note this symmetry is only for the half wing case, where the wing is centered
        # at the y axis, and the x axis is the symmetry axis

    def define(self):

        vc = self.parameters['vc']
        eps = self.parameters['eps']
        symmetry = self.parameters['symmetry']

        for eval_pt_name, vortex_coords_name, output_name, eval_pt_shape, vortex_coords_shape in zip(
                self.parameters['eval_pt_names'],
                self.parameters['vortex_coords_names'],
                self.parameters['output_names'],
                self.parameters['eval_pt_shapes'],
                self.parameters['vortex_coords_shapes']):


            # declare_inputs
            eval_pts = self.declare_variable(eval_pt_name, shape=eval_pt_shape)
            vortex_coords = self.declare_variable(vortex_coords_name, shape=vortex_coords_shape)


            # Compute corner points of vortex panels
            A, B, C, D = self._define_panel_points(vortex_coords)
            points = [A, B, C, D]

            # # Compute induced velocities for panel sides
            aic_sub = self._compute_panel_induced_velocities(eval_pts, points, eval_pt_shape, eval_pt_name,vortex_coords_name, vortex_coords_shape, output_name)

            # reshape aic sub to num_nodes, eval_pt_shapes[1]*eval_pt_shapes[2],(vortex_coords_shapes[1]-1)*(vortex_coords_shapes[2]-1) , 3
            # print('the shape of aic_sub is', eval_pt_shapes , vortex_coords_shapes)
            aic_sub_reshaped = csdl.reshape(aic_sub, 
                            new_shape=(eval_pt_shape[0], eval_pt_shape[1]*eval_pt_shape[2], (vortex_coords_shape[1]-1)*(vortex_coords_shape[2]-1), 3))
            

            self.register_output(output_name, aic_sub_reshaped)


    def _define_panel_points(self, vortex_coords):
        # define panel points
        #                  C -----> D
        # ---v_inf-(x)-->  ^        |
        #                  |        v
        #                  B <----- A
        A = vortex_coords[:,   1:, :-1 , :]
        B = vortex_coords[:, :-1 , :-1 , :]
        C = vortex_coords[:, :-1 ,   1:, :]
        D = vortex_coords[:,   1:,   1:, :]
        return A, B, C, D            

    def _compute_panel_induced_velocities(self, eval_pts, points, eval_pt_shape, eval_pt_name, vortex_coords_name, vortex_coords_shape, output_name):
        symmetry = self.parameters['symmetry']
        ny = eval_pt_shape[2]
        A, B, C, D = points
        # Apply symmetry if needed
        if symmetry:
            eval_pts = eval_pts[:,:,:ny//2,:]

        induced_velocities = []
        self.r_A, self.r_A_norm = self.__compute_expand_vecs(eval_pts, A, vortex_coords_shape,eval_pt_name,vortex_coords_name,output_name,'A')
        self.r_B, self.r_B_norm = self.__compute_expand_vecs(eval_pts, B, vortex_coords_shape,eval_pt_name,vortex_coords_name,output_name,'B')
        self.r_C, self.r_C_norm = self.__compute_expand_vecs(eval_pts, C, vortex_coords_shape,eval_pt_name,vortex_coords_name,output_name,'C')
        self.r_D, self.r_D_norm = self.__compute_expand_vecs(eval_pts, D, vortex_coords_shape,eval_pt_name,vortex_coords_name,output_name,'D')
        v_ab = self._induced_vel_line(self.r_A, self.r_B, self.r_A_norm, self.r_B_norm,'AB')
        v_bc = self._induced_vel_line(self.r_B, self.r_C, self.r_B_norm, self.r_C_norm,'BC')
        v_cd = self._induced_vel_line(self.r_C, self.r_D, self.r_C_norm, self.r_D_norm,'CD')
        v_da = self._induced_vel_line(self.r_D, self.r_A, self.r_D_norm, self.r_A_norm,'DA')
        

        total_induced_velocity = sum((v_ab, v_bc, v_cd, v_da))
        # Apply symmetry transformation if needed
        if symmetry:
            total_induced_velocity =  csdl.custom(total_induced_velocity, op = SymmetryFlip(in_name=total_induced_velocity.name, 
                                                                                            eval_pt_shape=eval_pt_shape, vortex_coords_shape=vortex_coords_shape, out_name=output_name+'_flattened'))
        return total_induced_velocity


    def __compute_expand_vecs(self, eval_pts, p_1, vortex_coords_shape, eval_pt_name, vortex_coords_name, output_name, point_name):

        vc = self.parameters['vc']
        num_nodes = eval_pts.shape[0]
        name = eval_pt_name + vortex_coords_name + output_name + point_name

        # 1 -> 2 eval_pts(num_pts_x,num_pts_y, 3)
        # v_induced_line shape=(num_panel_x*num_panel_y, num_panel_x, num_panel_y, 3)
        num_repeat_eval = p_1.shape[1] * p_1.shape[2]
        num_repeat_p = eval_pts.shape[1] * eval_pts.shape[2]

        eval_pts_expand = csdl.reshape(
            csdl.expand(
                csdl.reshape(eval_pts,
                             new_shape=(num_nodes, (eval_pts.shape[1] *
                                                    eval_pts.shape[2]), 3)),
                (num_nodes, eval_pts.shape[1] * eval_pts.shape[2],
                 num_repeat_eval, 3),
                'lij->likj',
            ),
            new_shape=(num_nodes,
                       eval_pts.shape[1] * eval_pts.shape[2] * num_repeat_eval,
                       3))

        p_1_expand = csdl.reshape(\
            csdl.expand(
                csdl.reshape(p_1,
                         new_shape=(num_nodes, (p_1.shape[1] * p_1.shape[2]),
                                    3)),
            (num_nodes, num_repeat_p, p_1.shape[1] * p_1.shape[2], 3),
            'lij->lkij'),
                        new_shape=(num_nodes,
                                    p_1.shape[1] *p_1.shape[2] * num_repeat_p,
                                    3))

        r1 = eval_pts_expand - p_1_expand
        r1_norm = csdl.sum(r1**2, axes=(2,))**0.5
        return r1, r1_norm


    def _induced_vel_line(self, r_1, r_2, r_1_norm, r_2_norm,line_name):

        vc = self.parameters['vc']
        # print('vc is--------------------', vc)

        num_nodes = r_1.shape[0]

        # 1 -> 2 eval_pts(num_pts_x,num_pts_y, 3)

        # the denominator of the induced velocity equation
        # shape = (num_nodes,num_panel_x*num_panel_y, num_panel_x* num_panel_y, 3)
        one_over_den = 1 / (np.pi * 4) * csdl.cross(r_1, r_2, axis=2)

        if vc == False:
            dor_r1_r2 = csdl.sum(r_1*r_2,axes=(2,))
            num = (1/(r_1_norm * r_2_norm + dor_r1_r2)) * (1/r_1_norm + 1/r_2_norm)
            # print('the shape of num is', num.shape)
            num_expand = csdl.expand(num, (num_nodes, num.shape[1], 3), 'ij->ijl')
            v_induced_line = num_expand * one_over_den
        else:
            new_vc=False
            if new_vc:
                core_size = 0.05
                dor_r1_r2 = csdl.sum(r_1*r_2,axes=(2,))
                r1s = r_1_norm**2
                r2s = r_2_norm**2
                eps_s = core_size**2

                f1 = ( (r1s - dor_r1_r2)/((r1s + eps_s + 1e-10)**0.5) + (r2s - dor_r1_r2)/((r2s + eps_s + 1e-10) **0.5) )/(r1s*r2s - dor_r1_r2**2 + eps_s*(r1s + r2s - 2*r_1_norm*r_2_norm) + 1e-10)
                f2 = one_over_den
                v_induced_line = csdl.expand(f1,(f2.shape),'ij->ijk') * f2 
                # self.print_var(v_induced_line)


            else:
                # this should be moved out instead of being in here, this is only used for dynamic case to compute the wake induced velocity indead
                dor_r1_r2 = csdl.sum(r_1*r_2,axes=(2,))
                dino = (r_1_norm * r_2_norm + dor_r1_r2)
                # deal with (r_1_norm * r_2_norm + dor_r1_r2) first
                # dino_non_singular = csdl.custom(dino, op=ReplaceZeros(in_name=dino.name,
                #                                                       in_shape=dino.shape,
                #                                                       out_name=dino.name + '_non_singular'))
                dino_non_singular = dino + 1e-4

                # num = (1/dino_non_singular) * (1/r_1_norm + 1/r_2_norm)
                num = (1/dino_non_singular) * (1/(r_1_norm+1e-3) + 1/(r_2_norm+1e-3))
                
                # print('the name of num is', num.name)
                self.register_output('num'+num.name, num)
                # print('the name of num is', num.name)
                # print('the shape of num is', num.shape)
                num_expand = csdl.expand(num, (num_nodes, num.shape[1], 3), 'ij->ijl')
                v_induced_line = num_expand * one_over_den

        return v_induced_line


class SymmetryFlip(csdl.CustomExplicitOperation):
    """
    Compute the whole AIC matrix given half of it

    parameters
    ----------
    <aic_half_names>[nc*ns*(nc_v-1)*(ns_v-1)* nc*ns*(nc_v-1)*(ns_v-1)/2, 3] : numpy array
        Array defining the nodal coordinates of the lifting surface that the 
        AIC matrix is computed on.

    Returns
    -------
    <aic_names>[nc*ns*(nc_v-1)*(ns_v-1), nc*ns*(nc_v-1)*(ns_v-1), 3] : numpy array
        Aerodynamic influence coeffients (can be interprete as induced
        velocities given circulations=1)
    """    
    def initialize(self):
        self.parameters.declare('in_name', types=str)
        self.parameters.declare('eval_pt_shape', types=tuple)
        self.parameters.declare('vortex_coords_shape', types=tuple)
        self.parameters.declare('out_name', types=str)
    def define(self):
        eval_pt_shape =self.eval_pt_shape= self.parameters['eval_pt_shape']
        vortex_coords_shape =self.vortex_coords_shape =  self.parameters['vortex_coords_shape']
        shape = eval_pt_shape[1]*eval_pt_shape[2]*(vortex_coords_shape[1]-1)*(vortex_coords_shape[2]-1)
        num_nodes = eval_pt_shape[0]
        self.add_input(self.parameters['in_name'],shape=(num_nodes,int(shape/2),3))
        self.add_output(self.parameters['out_name'],shape=(num_nodes,int(shape),3))

        self.full_aic_func = self.__get_full_aic
        row_indices  = np.arange(int(num_nodes*shape*3))
        col_ind_temp = np.arange(int(num_nodes*shape/2*3)).reshape(num_nodes,eval_pt_shape[1],int(eval_pt_shape[2]/2),int(vortex_coords_shape[1]-1),int(vortex_coords_shape[2]-1),3)
        
        col_ind_flip = np.flip(col_ind_temp,axis=(2,4))
        col_indices = np.concatenate((col_ind_temp,col_ind_flip),axis=2).flatten()
        self.declare_derivatives(self.parameters['out_name'], self.parameters['in_name'],rows=row_indices,cols=col_indices,val=np.ones(row_indices.size))

    def compute(self, inputs, outputs):
        outputs[self.parameters['out_name']] = self.full_aic_func(inputs[self.parameters['in_name']]).reshape(1,-1,3)

    def __get_full_aic(self,half_aic):
        nx_panel = self.eval_pt_shape[1]
        ny_panel = self.eval_pt_shape[2] 
        nx_panel_ind = self.vortex_coords_shape[1] - 1
        ny_panel_ind = self.vortex_coords_shape[2] - 1 
        num_nodes = self.eval_pt_shape[0]
        half_reshaped = half_aic.reshape(num_nodes,nx_panel,int(ny_panel/2),nx_panel_ind, ny_panel_ind, 3)
        # half_aic.reshape(nx_panel,int(ny_panel/2),nx_panel_ind, ny_panel_ind, 3)
        other_half_aic = np.flip(half_reshaped, (2,4))
        full_aic = np.concatenate((half_reshaped, other_half_aic), axis=2).reshape(num_nodes,-1,3)
        return full_aic


if __name__ == "__main__":
    '''
    # import timeit
    # from python_csdl_backend import Simulator
    # import numpy as onp
    # AIC_half_val = onp.random.rand(1, 32, 3)
    # eval_pt_shape = (1,2,4)
    # vortex_coords_shape = (1,3,5)
    # m = csdl.Model()
    # AIC_half = m.declare_variable('AIC_half', val = AIC_half_val)
    # output_name = 'AIC'
    # AIC = csdl.custom(AIC_half, op = SymmetryFlip(in_name=AIC_half.name, eval_pt_shape=eval_pt_shape, vortex_coords_shape=vortex_coords_shape, out_name=output_name))
    # m.register_output(output_name, AIC)
    # sim = Simulator(m)
    # sim.run()
    '''

    
    import time
    import timeit
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

    # test if multiple ops work
    submodel=SubAicBiotSavarts(eval_pt_names=eval_pt_names,
                               vortex_coords_names=vortex_coords_names,
                               eval_pt_shapes=eval_pt_shapes,
                               vortex_coords_shapes=vortex_coords_shapes,
                               output_names=output_names,
                               symmetry=True,
                               vc=True)
    aic = model_1.declare_variable('aic', shape=(1, (nc-1)*(ns-1)*(nc-1)*(ns-1), 3))


    model_1.add(submodel,'submodel')

    #####################
    # finshed adding model
    ####################
    sim = Simulator(model_1)
    print('time', time.time() - ts)
    sim.run()
    print('time', time.time() - ts)
    # sim.compute_totals(of='aic',wrt='vtx_pts')
    # print('time', time.time() - ts)
    # sim.compute_totals(of='aic',wrt='vtx_pts')
    # print('time', time.time() - ts)
    # sim.compute_totals(of='aic',wrt='vtx_pts')
    # print('time', time.time() - ts)
    # sim.compute_totals(of='aic',wrt='vtx_pts')
    # print('time', time.time() - ts)
    # sim.compute_totals(of='aic',wrt='vtx_pts')
    # print('time', time.time() - ts)
    exit()
    