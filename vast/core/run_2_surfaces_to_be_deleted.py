
import numpy as np
from vast.core.vlm_fixed_wake_system_new import VLMFixedWakeSystem
import csdl
from python_csdl_backend import Simulator
from VAST.utils.generate_mesh import *

# define mesh as the input to the model
nc = 3
ns = 11
num_nodes = 2
surface_shapes = [(num_nodes, nc, ns, 3)]
surface_names = ['wing_surface']
n_wake_pts_chord=2

nc_tail = 5
ns_tail = 7

surface_shapes.append((num_nodes, nc_tail, ns_tail, 3))
surface_names.append('tail_surface')

surface_meshs = []
# create a simple rectangular mesh
mesh_dict = {
    "num_y": ns, "num_x": nc, "wing_type": "rect", "symmetry": False, "span": 10.0,
    "chord": 1, "span_cos_sppacing": 1.0, "chord_cos_sacing": 1.0,
}
# Generate mesh of a rectangular wing
mesh = generate_mesh(mesh_dict)
wing_surface_mesh = [np.einsum('i,jkl->ijkl', np.ones((num_nodes)), mesh)]

# Generate mesh of a rectangular tail
mesh_dict_tail = {
    "num_y": ns_tail, "num_x": nc_tail, "wing_type": "rect", "symmetry": False, "span": 4.0,
    "chord": 1, "span_cos_sppacing": 1.0, "chord_cos_sacing": 1.0,
}
tail_mesh = generate_mesh(mesh_dict_tail)
tail_surface_mesh = [np.einsum('i,jkl->ijkl', np.ones((num_nodes)), tail_mesh)]
surface_meshs.append(wing_surface_mesh)
surface_meshs.append(tail_surface_mesh)
#####################################################################################


# Here, the mesh is checked to be the same as ex_1vlm_simulation_rec_wing.py in VAST 0.1.0

# define frame velocity
angle_of_attack_degree = np.array([5, -5])  # deg
v_inf = 248.136 # m/s

angle_of_attack_rad = np.deg2rad(angle_of_attack_degree)
frame_vel_numpy = np.zeros((num_nodes, 3))
frame_vel_numpy[:, 0] = -v_inf * np.cos(angle_of_attack_rad)
frame_vel_numpy[:, 2] = -v_inf * np.sin(angle_of_attack_rad)
#####################################################################################


# create a model
model = csdl.Model()

# create a csdl variable for the input mesh
for surface_name, surface_mesh in zip(surface_names, surface_meshs):
    input_mesh = model.create_input(surface_name, surface_mesh)

# create input for the frame velocity
frame_vel = model.create_input('frame_vel', frame_vel_numpy)
vlm_fixed_wake_model = VLMFixedWakeSystem(
    surface_names=surface_names,
    surface_shapes=surface_shapes,
    mesh_unit='m',
    problem_type='fixed_wake',
    num_wake_pts=2,
    delta_t=100.,
    compressible=False,
    Ma=None
)
model.add(vlm_fixed_wake_model, 'VLMFixedWakeSystem')
sim = Simulator(model,display_scripts=True)
sim.run()