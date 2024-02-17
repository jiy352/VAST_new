'''Example 1: An example written as a Python file (.py) 
with explanations given as comments. <br>
Note that the title and description for the example on the web page are generated 
based on the first docstring in the Python file. <br>
**Docstring syntax:** *```"""Title: Description (optional)"""```*  <br>
Refer to examples 2 and 3 for a cleaner demonstration of using the docstring.'''

import numpy as np

import csdl
from python_csdl_backend import Simulator
# from vast.utils.generate_rectangular_mesh import generate_rectangular_mesh
from vast.core.submodels.geometric_submodels.mesh_to_vortex_mesh import MeshToVortexMesh
from vast.core.submodels.geometric_submodels.compute_normals import ComputeNormals
from vast.core.submodels.geometric_submodels.geometric_property_extraction import GeometricPropertyExtraction
from vast.core.submodels.aerodynamic_coeffs_submodels.sub_aic_biot_savarts import SubAicBiotSavarts

from vast.core.submodels.aerodynamic_coeffs_submodels.projection_gpt import Projection
from vast.core.submodels.wake_submodels.generate_fixed_wake import GenerateFixedWake

from VAST.utils.generate_mesh import *

# define mesh as the input to the model
nc = 3
ns = 11
num_nodes = 2
surface_shapes = [(num_nodes, nc, ns, 3)]
surface_names = ['surface']
n_wake_pts_chord=2

# create a simple rectangular mesh
mesh_dict = {
    "num_y": ns, "num_x": nc, "wing_type": "rect", "symmetry": False, "span": 10.0,
    "chord": 1, "span_cos_sppacing": 1.0, "chord_cos_sacing": 1.0,
}
# Generate mesh of a rectangular wing
mesh = generate_mesh(mesh_dict)
surface_mesh = [np.einsum('i,jkl->ijkl', np.ones((num_nodes)), mesh)]
# Here, the mesh is checked to be the same as ex_1vlm_simulation_rec_wing.py in VAST 0.1.0

# define frame velocity
angle_of_attack_degree = np.array([5, -5])  # deg
v_inf = 248.136 # m/s

angle_of_attack_rad = np.deg2rad(angle_of_attack_degree)
frame_vel_numpy = np.zeros((num_nodes, 3))
frame_vel_numpy[:, 0] = -v_inf * np.cos(angle_of_attack_rad)
frame_vel_numpy[:, 2] = -v_inf * np.sin(angle_of_attack_rad)


# create a model
model = csdl.Model()

# create a csdl variable for the input mesh
for surface_name, surface_mesh in zip(surface_names, surface_mesh):
    input_mesh = model.create_input(surface_name, surface_mesh)

# create input for the frame velocity
frame_vel = model.create_input('frame_vel', frame_vel_numpy)


# create a mesh to vortex mesh model
parameters = {
    'surface_names': surface_names,
    'surface_shapes': surface_shapes,
    'mesh_unit': 'm',
    'delta_t': 0,
    'problem_type': 'fixed_wake',
    'compressible': False,
    'Ma': None
}

m2vm = MeshToVortexMesh(**parameters)  # mesh 2 vortex mesh
model.add(m2vm, 'MeshToVortexMesh')


# create a compute normals model
normal_names = [surface_name + '_normals' for surface_name in surface_names]

normal_models = ComputeNormals(surfaces_to_eval_normals=surface_names,
                                 normal_names=normal_names,
                                 surfaces_to_eval_normal_shapes=surface_shapes)
model.add(normal_models, 'ComputeNormals')

# add GeometricPropertyExtraction model
geoprop = GeometricPropertyExtraction(surface_names=surface_names,
                                      surface_shapes=surface_shapes)
model.add(geoprop, 'GeometricPropertyExtraction')

# compute the normal velocity, based on the expanded kinematic velocity
# expand the frame velocity to get the kinematic velocity
for surface_name, surface_shape in zip(surface_names, surface_shapes):
    nc = surface_shape[1]
    ns = surface_shape[2]

    kinematic_vel = -csdl.expand(frame_vel, (num_nodes, (nc-1)* (ns-1), 3), 'ik->ijk')
    # register the kinematic velocity
    model.register_output(surface_name + '_kinematic_vel', kinematic_vel)

# compute the normal velocity for the RHS
input_var_shapes = [(num_nodes, nc-1, ns-1, 3)]
projection = Projection(
    input_var_names=[surface_name + '_kinematic_vel' for surface_name in surface_names],
    normal_names=normal_names,
    output_var_name='rhs',
    input_var_shapes=[(num_nodes, (nc-1)* (ns-1), 3)],
    normal_shapes=[(num_nodes, nc-1, ns-1, 3)])

model.add(projection, 'Projection_rhs')


# compute aic using the biot savarts law
vortex_coords_names = [surface_name + '_bound_vtx_coords' for surface_name in surface_names]
collocation_pts_names = [surface_name + '_collocation_pts' for surface_name in surface_names]

aic_model = SubAicBiotSavarts(eval_pt_names=collocation_pts_names,
                        eval_pt_shapes=input_var_shapes,
                        vortex_coords_names=vortex_coords_names,
                        vortex_coords_shapes=surface_shapes,
                        vc=True,
                        output_names=['aic'])


model.add(aic_model, 'SubAicBiotSavarts')

aic_shapes = [(num_nodes, (nc-1)* (ns-1), (nc-1)* (ns-1), 3)]

# project the aic to the normal direction
aic_projected_model = Projection(
    input_var_names=['aic'],
    normal_names=normal_names,
    output_var_name='aic_projection',
    input_var_shapes=aic_shapes,
    normal_shapes=[(num_nodes, nc-1, ns-1, 3)])
model.add(aic_projected_model, 'ProjectionAic')

# Here aic_projection is verfied against the example in VAST 0.1.0

# generate the wake for the wake induced velocity
wake_model = GenerateFixedWake(
    surface_names=surface_names,
    surface_shapes=surface_shapes,
    n_wake_pts_chord = n_wake_pts_chord,
    delta_t = 100.,
)

model.add(wake_model, 'GenerateFixedWake')

wake_coords_names = [surface_name + '_wake_coords' for surface_name in surface_names]
wake_coords_shapes = [(num_nodes, n_wake_pts_chord, surface_shape[2], 3) for surface_shape in surface_shapes]
# compute wake induced velocity, with eval pts as collcation points, induced by wake

wake_aic_model = SubAicBiotSavarts(eval_pt_names=collocation_pts_names,
                        eval_pt_shapes=input_var_shapes,
                        vortex_coords_names=wake_coords_names,
                        vortex_coords_shapes=wake_coords_shapes,
                        output_names=['wake_aic'])
print('input_var_shapes', input_var_shapes) 
model.add(wake_aic_model, 'WakeSubAicBiotSavarts')

# get LHS A matrix

# project wake aic to the normal direction
wake_aic = model.declare_variable('wake_aic', shape=(num_nodes, (nc-1)* (ns-1), (n_wake_pts_chord-1)* (ns-1), 3))

# compute the normals
normal_names_wake = [wake_name + '_normals' for wake_name in wake_coords_names]
normal_models = ComputeNormals(surfaces_to_eval_normals=wake_coords_names,
                                 normal_names=normal_names_wake,
                                 surfaces_to_eval_normal_shapes=wake_coords_shapes)
model.add(normal_models, 'ComputeNormalsWake')

# project wake aic to the normal direction
input_var_shapes = [(num_nodes, (nc-1)* (ns-1), (n_wake_pts_chord-1)* (ns-1), 3)]
projection = Projection(
    input_var_names=['wake_aic'],
    normal_names=normal_names_wake,
    output_var_name='wake_rhs',
    input_var_shapes=input_var_shapes,
    normal_shapes=[(num_nodes, (n_wake_pts_chord-1), ns-1, 3)])

model.add(projection, 'ProjectionWake')
M = model.declare_variable('wake_rhs', shape=(num_nodes, (nc-1)* (ns-1), (n_wake_pts_chord-1)* (ns-1)))
M_mat = M*1.0
model.register_output('M_mat', M_mat)
from vast.utils.custom_explicit_mat_sprsmat import Explicit, compute_spars
sprs = compute_spars(surface_shapes)

M_reshaped = csdl.custom(M_mat,op=Explicit(
                                        num_nodes=num_nodes,
                                        sprs=sprs,
                                        num_bd_panel=(nc-1)* (ns-1),
                                        num_wake_panel=(n_wake_pts_chord-1)* (ns-1),
                                    ))
model.register_output('M_reshaped', M_reshaped)
aic_projection = model.declare_variable('aic_projection', shape=(num_nodes, (nc-1)* (ns-1), (nc-1)* (ns-1)))
MTX = aic_projection + csdl.reshape(M_reshaped, (num_nodes, (nc-1)* (ns-1), (nc-1)* (ns-1)))

model.register_output('MTX', MTX)
# solve for circulation strength
rhs = model.declare_variable('rhs', shape=(num_nodes, (nc-1)* (ns-1)))
from csdl.solvers.linear.direct import DirectSolver

circulation_strength = model.create_output('circulation_strength', shape=(num_nodes, (nc-1)* (ns-1)))

for i in range(num_nodes):
    A = csdl.reshape(MTX[i,:,:], ((nc-1)* (ns-1), (nc-1)* (ns-1)))
    rhs_i = csdl.reshape(rhs[i,:], ((nc-1)* (ns-1), ))
    # model.register_output('A', A)
    # model.register_output('rhs_i', rhs_i)
    sol = csdl.solve(A, -rhs_i, solver = DirectSolver())

    circulation_strength[i,:] = csdl.reshape(sol, circulation_strength[i,:].shape)

# run the model
sim = Simulator(model, display_scripts=True)
sim.run()

# print('surface_bound_vtx_coords', sim['surface_bound_vtx_coords'])
# print('wake_coords', sim['surface_wake_coords'])
# print('wake_aic', sim['wake_aic'])
# print('surface_normals', sim['surface_normals'])
# sim['surface_bound_vtx_coords']