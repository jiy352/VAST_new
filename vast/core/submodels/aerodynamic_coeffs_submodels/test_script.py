import time
import timeit
from vast.core.submodels.aerodynamic_coeffs_submodels.sub_aic_biot_savarts import SubAicBiotSavarts
from vast.core.submodels.geometric_submodels.compute_normals import ComputeNormals
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

# test if multiple ops work
submodel=SubAicBiotSavarts(eval_pt_names=eval_pt_names,
                            vortex_coords_names=vortex_coords_names,
                            eval_pt_shapes=eval_pt_shapes,
                            vortex_coords_shapes=vortex_coords_shapes,
                            output_names=output_names,
                            symmetry=True,
                            vc=True)
# aic = model_1.declare_variable('aic', shape=(1, (nc-1)*(ns-1)*(nc-1)*(ns-1), 3))


model_1.add(submodel,'submodel')

#####################
# finshed adding model
####################
sim = Simulator(model_1)
print('time', time.time() - ts)
sim.run()