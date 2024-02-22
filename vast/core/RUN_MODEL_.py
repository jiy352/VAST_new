

# RUN_MODEL_

# system evaluation block

# op _0013_decompose_eval
# LANG: surface --> _001e, _0014, _0017, _001d
# SHAPES: (2, 3, 11, 3) --> (2, 1, 11, 3), (2, 2, 11, 3), (2, 2, 11, 3), (2, 1, 11, 3)
# full namespace: VLMFixedWakeSystem.MeshToVortexMesh
v33__0014 = ((v75_surface.flatten())[src_indices__0014__0013]).reshape((2, 2, 11, 3))
v35__0017 = ((v75_surface.flatten())[src_indices__0017__0013]).reshape((2, 2, 11, 3))
v38__001d = ((v75_surface.flatten())[src_indices__001d__0013]).reshape((2, 1, 11, 3))
v39__001e = ((v75_surface.flatten())[src_indices__001e__0013]).reshape((2, 1, 11, 3))

# op _001f_linear_combination_eval
# LANG: _001d, _001e --> _001g
# SHAPES: (2, 1, 11, 3), (2, 1, 11, 3) --> (2, 1, 11, 3)
# full namespace: VLMFixedWakeSystem.MeshToVortexMesh
v40__001g = v38__001d+-1*v39__001e

# op _0015_power_combination_eval
# LANG: _0014 --> _0016
# SHAPES: (2, 2, 11, 3) --> (2, 2, 11, 3)
# full namespace: VLMFixedWakeSystem.MeshToVortexMesh
v34__0016 = (v33__0014)
v34__0016 = (v34__0016*_0015_coeff).reshape((2, 2, 11, 3))

# op _0018_power_combination_eval
# LANG: _0017 --> _0019
# SHAPES: (2, 2, 11, 3) --> (2, 2, 11, 3)
# full namespace: VLMFixedWakeSystem.MeshToVortexMesh
v36__0019 = (v35__0017)
v36__0019 = (v36__0019*_0018_coeff).reshape((2, 2, 11, 3))

# op _001h_power_combination_eval
# LANG: _001g --> _001i
# SHAPES: (2, 1, 11, 3) --> (2, 1, 11, 3)
# full namespace: VLMFixedWakeSystem.MeshToVortexMesh
v41__001i = (v40__001g)
v41__001i = (v41__001i*_001h_coeff).reshape((2, 1, 11, 3))

# op _001a_linear_combination_eval
# LANG: _0016, _0019 --> _001b
# SHAPES: (2, 2, 11, 3), (2, 2, 11, 3) --> (2, 2, 11, 3)
# full namespace: VLMFixedWakeSystem.MeshToVortexMesh
v37__001b = v34__0016+v36__0019

# op _001j_linear_combination_eval
# LANG: _001d, _001i --> _001k
# SHAPES: (2, 1, 11, 3), (2, 1, 11, 3) --> (2, 1, 11, 3)
# full namespace: VLMFixedWakeSystem.MeshToVortexMesh
v42__001k = v38__001d+v41__001i

# op _001c_indexed_passthrough_eval
# LANG: _001b, _001k --> surface_bound_vtx_coords
# SHAPES: (2, 2, 11, 3), (2, 1, 11, 3) --> (2, 3, 11, 3)
# full namespace: VLMFixedWakeSystem.MeshToVortexMesh
v229_surface_bound_vtx_coords__temp[i_v37__001b__001c_indexed_passthrough_eval] = v37__001b.flatten()
v229_surface_bound_vtx_coords = v229_surface_bound_vtx_coords__temp.copy()
v229_surface_bound_vtx_coords__temp[i_v42__001k__001c_indexed_passthrough_eval] = v42__001k.flatten()
v229_surface_bound_vtx_coords = v229_surface_bound_vtx_coords__temp.copy()

# op _001I_decompose_eval
# LANG: surface_bound_vtx_coords --> _001Q, _001J, _001K, _001N, _001V, _001W, _001Z
# SHAPES: (2, 3, 11, 3) --> (2, 2, 10, 3), (2, 2, 10, 3), (2, 2, 10, 3), (2, 2, 10, 3), (2, 2, 10, 3), (2, 2, 10, 3), (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.GeometricPropertyExtraction
v57__001J = ((v229_surface_bound_vtx_coords.flatten())[src_indices__001J__001I]).reshape((2, 2, 10, 3))
v58__001K = ((v229_surface_bound_vtx_coords.flatten())[src_indices__001K__001I]).reshape((2, 2, 10, 3))
v60__001N = ((v229_surface_bound_vtx_coords.flatten())[src_indices__001N__001I]).reshape((2, 2, 10, 3))
v62__001Q = ((v229_surface_bound_vtx_coords.flatten())[src_indices__001Q__001I]).reshape((2, 2, 10, 3))
v65__001V = ((v229_surface_bound_vtx_coords.flatten())[src_indices__001V__001I]).reshape((2, 2, 10, 3))
v66__001W = ((v229_surface_bound_vtx_coords.flatten())[src_indices__001W__001I]).reshape((2, 2, 10, 3))
v68__001Z = ((v229_surface_bound_vtx_coords.flatten())[src_indices__001Z__001I]).reshape((2, 2, 10, 3))

# op _006R_decompose_eval
# LANG: surface_bound_vtx_coords --> _006S
# SHAPES: (2, 3, 11, 3) --> (2, 1, 11, 3)
# full namespace: VLMFixedWakeSystem.GenerateFixedWake
v230__006S = ((v229_surface_bound_vtx_coords.flatten())[src_indices__006S__006R]).reshape((2, 1, 11, 3))

# op _006Y_linear_combination_eval
# LANG: frame_vel --> _006Z
# SHAPES: (2, 3) --> (2, 3)
# full namespace: VLMFixedWakeSystem.GenerateFixedWake
v234__006Z = -1*v228_frame_vel

# op _001L_linear_combination_eval
# LANG: _001J, _001K --> _001M
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.GeometricPropertyExtraction
v59__001M = v57__001J+v58__001K

# op _006T reshape_eval
# LANG: _006S --> _006U
# SHAPES: (2, 1, 11, 3) --> (2, 11, 3)
# full namespace: VLMFixedWakeSystem.GenerateFixedWake
v231__006U = v230__006S.reshape((2, 11, 3))

# op _006_ expand_array_eval
# LANG: _006Z --> _0070
# SHAPES: (2, 3) --> (2, 2, 11, 3)
# full namespace: VLMFixedWakeSystem.GenerateFixedWake
v235__0070 = np.einsum('ad,bc->abcd', v234__006Z.reshape((2, 3)) ,np.ones((2, 11))).reshape((2, 2, 11, 3))

# op _001O_linear_combination_eval
# LANG: _001N, _001M --> _001P
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.GeometricPropertyExtraction
v61__001P = v59__001M+v60__001N

# op _006V expand_array_eval
# LANG: _006U --> _006W
# SHAPES: (2, 11, 3) --> (2, 2, 11, 3)
# full namespace: VLMFixedWakeSystem.GenerateFixedWake
v232__006W = np.einsum('acd,b->abcd', v231__006U.reshape((2, 11, 3)) ,np.ones((2,))).reshape((2, 2, 11, 3))

# op _0071_power_combination_eval
# LANG: surface_factor, _0070 --> _0072
# SHAPES: (2, 2, 11, 3), (2, 2, 11, 3) --> (2, 2, 11, 3)
# full namespace: VLMFixedWakeSystem.GenerateFixedWake
v236__0072 = (v235__0070)*(v233_surface_factor)
v236__0072 = v236__0072.reshape((2, 2, 11, 3))

# op _001R_linear_combination_eval
# LANG: _001Q, _001P --> _001S
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.GeometricPropertyExtraction
v63__001S = v61__001P+v62__001Q

# op _0073_linear_combination_eval
# LANG: _006W, _0072 --> surface_wake_coords
# SHAPES: (2, 2, 11, 3), (2, 2, 11, 3) --> (2, 2, 11, 3)
# full namespace: VLMFixedWakeSystem.GenerateFixedWake
v239_surface_wake_coords = v232__006W+v236__0072

# op _001T_power_combination_eval
# LANG: _001S --> surface_collocation_pts
# SHAPES: (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.GeometricPropertyExtraction
v238_surface_collocation_pts = (v63__001S)
v238_surface_collocation_pts = (v238_surface_collocation_pts*_001T_coeff).reshape((2, 2, 10, 3))

# op _0077_decompose_eval
# LANG: surface_wake_coords --> _0078, _0079, _007a, _007b
# SHAPES: (2, 2, 11, 3) --> (2, 1, 10, 3), (2, 1, 10, 3), (2, 1, 10, 3), (2, 1, 10, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v240__0078 = ((v239_surface_wake_coords.flatten())[src_indices__0078__0077]).reshape((2, 1, 10, 3))
v241__0079 = ((v239_surface_wake_coords.flatten())[src_indices__0079__0077]).reshape((2, 1, 10, 3))
v242__007a = ((v239_surface_wake_coords.flatten())[src_indices__007a__0077]).reshape((2, 1, 10, 3))
v243__007b = ((v239_surface_wake_coords.flatten())[src_indices__007b__0077]).reshape((2, 1, 10, 3))

# op _007C reshape_eval
# LANG: _0079 --> _007D
# SHAPES: (2, 1, 10, 3) --> (2, 10, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v257__007D = v241__0079.reshape((2, 10, 3))

# op _007c reshape_eval
# LANG: surface_collocation_pts --> _007d
# SHAPES: (2, 2, 10, 3) --> (2, 20, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v244__007d = v238_surface_collocation_pts.reshape((2, 20, 3))

# op _007i reshape_eval
# LANG: _0078 --> _007j
# SHAPES: (2, 1, 10, 3) --> (2, 10, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v247__007j = v240__0078.reshape((2, 10, 3))

# op _007w reshape_eval
# LANG: surface_collocation_pts --> _007x
# SHAPES: (2, 2, 10, 3) --> (2, 20, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v254__007x = v238_surface_collocation_pts.reshape((2, 20, 3))

# op _007E expand_array_eval
# LANG: _007D --> _007F
# SHAPES: (2, 10, 3) --> (2, 20, 10, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v258__007F = np.einsum('acd,b->abcd', v257__007D.reshape((2, 10, 3)) ,np.ones((20,))).reshape((2, 20, 10, 3))

# op _007Q reshape_eval
# LANG: surface_collocation_pts --> _007R
# SHAPES: (2, 2, 10, 3) --> (2, 20, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v264__007R = v238_surface_collocation_pts.reshape((2, 20, 3))

# op _007W reshape_eval
# LANG: _007a --> _007X
# SHAPES: (2, 1, 10, 3) --> (2, 10, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v267__007X = v242__007a.reshape((2, 10, 3))

# op _007e expand_array_eval
# LANG: _007d --> _007f
# SHAPES: (2, 20, 3) --> (2, 20, 10, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v245__007f = np.einsum('abd,c->abcd', v244__007d.reshape((2, 20, 3)) ,np.ones((10,))).reshape((2, 20, 10, 3))

# op _007k expand_array_eval
# LANG: _007j --> _007l
# SHAPES: (2, 10, 3) --> (2, 20, 10, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v248__007l = np.einsum('acd,b->abcd', v247__007j.reshape((2, 10, 3)) ,np.ones((20,))).reshape((2, 20, 10, 3))

# op _007y expand_array_eval
# LANG: _007x --> _007z
# SHAPES: (2, 20, 3) --> (2, 20, 10, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v255__007z = np.einsum('abd,c->abcd', v254__007x.reshape((2, 20, 3)) ,np.ones((10,))).reshape((2, 20, 10, 3))

# op _007A reshape_eval
# LANG: _007z --> _007B
# SHAPES: (2, 20, 10, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v256__007B = v255__007z.reshape((2, 200, 3))

# op _007G reshape_eval
# LANG: _007F --> _007H
# SHAPES: (2, 20, 10, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v259__007H = v258__007F.reshape((2, 200, 3))

# op _007S expand_array_eval
# LANG: _007R --> _007T
# SHAPES: (2, 20, 3) --> (2, 20, 10, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v265__007T = np.einsum('abd,c->abcd', v264__007R.reshape((2, 20, 3)) ,np.ones((10,))).reshape((2, 20, 10, 3))

# op _007Y expand_array_eval
# LANG: _007X --> _007Z
# SHAPES: (2, 10, 3) --> (2, 20, 10, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v268__007Z = np.einsum('acd,b->abcd', v267__007X.reshape((2, 10, 3)) ,np.ones((20,))).reshape((2, 20, 10, 3))

# op _007g reshape_eval
# LANG: _007f --> _007h
# SHAPES: (2, 20, 10, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v246__007h = v245__007f.reshape((2, 200, 3))

# op _007m reshape_eval
# LANG: _007l --> _007n
# SHAPES: (2, 20, 10, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v249__007n = v248__007l.reshape((2, 200, 3))

# op _0089 reshape_eval
# LANG: surface_collocation_pts --> _008a
# SHAPES: (2, 2, 10, 3) --> (2, 20, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v274__008a = v238_surface_collocation_pts.reshape((2, 20, 3))

# op _008f reshape_eval
# LANG: _007b --> _008g
# SHAPES: (2, 1, 10, 3) --> (2, 10, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v277__008g = v243__007b.reshape((2, 10, 3))

# op _007I_linear_combination_eval
# LANG: _007B, _007H --> _007J
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v260__007J = v256__007B+-1*v259__007H

# op _007U reshape_eval
# LANG: _007T --> _007V
# SHAPES: (2, 20, 10, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v266__007V = v265__007T.reshape((2, 200, 3))

# op _007_ reshape_eval
# LANG: _007Z --> _0080
# SHAPES: (2, 20, 10, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v269__0080 = v268__007Z.reshape((2, 200, 3))

# op _007o_linear_combination_eval
# LANG: _007h, _007n --> _007p
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v250__007p = v246__007h+-1*v249__007n

# op _008b expand_array_eval
# LANG: _008a --> _008c
# SHAPES: (2, 20, 3) --> (2, 20, 10, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v275__008c = np.einsum('abd,c->abcd', v274__008a.reshape((2, 20, 3)) ,np.ones((10,))).reshape((2, 20, 10, 3))

# op _008h expand_array_eval
# LANG: _008g --> _008i
# SHAPES: (2, 10, 3) --> (2, 20, 10, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v278__008i = np.einsum('acd,b->abcd', v277__008g.reshape((2, 10, 3)) ,np.ones((20,))).reshape((2, 20, 10, 3))

# op _007K_power_combination_eval
# LANG: _007J --> _007L
# SHAPES: (2, 200, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v261__007L = (v260__007J**2)
v261__007L = v261__007L.reshape((2, 200, 3))

# op _007q_power_combination_eval
# LANG: _007p --> _007r
# SHAPES: (2, 200, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v251__007r = (v250__007p**2)
v251__007r = v251__007r.reshape((2, 200, 3))

# op _0081_linear_combination_eval
# LANG: _007V, _0080 --> _0082
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v270__0082 = v266__007V+-1*v269__0080

# op _008d reshape_eval
# LANG: _008c --> _008e
# SHAPES: (2, 20, 10, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v276__008e = v275__008c.reshape((2, 200, 3))

# op _008j reshape_eval
# LANG: _008i --> _008k
# SHAPES: (2, 20, 10, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v279__008k = v278__008i.reshape((2, 200, 3))

# op _007M_single_tensor_sum_with_axis_eval
# LANG: _007L --> _007N
# SHAPES: (2, 200, 3) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v262__007N = np.sum(v261__007L, axis = (2,)).reshape((2, 200))

# op _007s_single_tensor_sum_with_axis_eval
# LANG: _007r --> _007t
# SHAPES: (2, 200, 3) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v252__007t = np.sum(v251__007r, axis = (2,)).reshape((2, 200))

# op _0083_power_combination_eval
# LANG: _0082 --> _0084
# SHAPES: (2, 200, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v271__0084 = (v270__0082**2)
v271__0084 = v271__0084.reshape((2, 200, 3))

# op _008l_linear_combination_eval
# LANG: _008e, _008k --> _008m
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v280__008m = v276__008e+-1*v279__008k

# op _007O_power_combination_eval
# LANG: _007N --> _007P
# SHAPES: (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v263__007P = (v262__007N**0.5)
v263__007P = v263__007P.reshape((2, 200))

# op _007u_power_combination_eval
# LANG: _007t --> _007v
# SHAPES: (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v253__007v = (v252__007t**0.5)
v253__007v = v253__007v.reshape((2, 200))

# op _0085_single_tensor_sum_with_axis_eval
# LANG: _0084 --> _0086
# SHAPES: (2, 200, 3) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v272__0086 = np.sum(v271__0084, axis = (2,)).reshape((2, 200))

# op _008n_power_combination_eval
# LANG: _008m --> _008o
# SHAPES: (2, 200, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v281__008o = (v280__008m**2)
v281__008o = v281__008o.reshape((2, 200, 3))

# op _008x_power_combination_eval
# LANG: _007p, _007J --> _008y
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v286__008y = (v250__007p)*(v260__007J)
v286__008y = v286__008y.reshape((2, 200, 3))

# op _001m_decompose_eval
# LANG: surface --> _001s, _001n, _001o, _001r
# SHAPES: (2, 3, 11, 3) --> (2, 2, 10, 3), (2, 2, 10, 3), (2, 2, 10, 3), (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.ComputeLiftingSurfaceNormals
v44__001n = ((v75_surface.flatten())[src_indices__001n__001m]).reshape((2, 2, 10, 3))
v45__001o = ((v75_surface.flatten())[src_indices__001o__001m]).reshape((2, 2, 10, 3))
v47__001r = ((v75_surface.flatten())[src_indices__001r__001m]).reshape((2, 2, 10, 3))
v48__001s = ((v75_surface.flatten())[src_indices__001s__001m]).reshape((2, 2, 10, 3))

# op _0087_power_combination_eval
# LANG: _0086 --> _0088
# SHAPES: (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v273__0088 = (v272__0086**0.5)
v273__0088 = v273__0088.reshape((2, 200))

# op _008B_power_combination_eval
# LANG: _007v, _007P --> _008C
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v288__008C = (v253__007v)*(v263__007P)
v288__008C = v288__008C.reshape((2, 200))

# op _008X_power_combination_eval
# LANG: _0082, _007J --> _008Y
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v299__008Y = (v260__007J)*(v270__0082)
v299__008Y = v299__008Y.reshape((2, 200, 3))

# op _008p_single_tensor_sum_with_axis_eval
# LANG: _008o --> _008q
# SHAPES: (2, 200, 3) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v282__008q = np.sum(v281__008o, axis = (2,)).reshape((2, 200))

# op _008z_single_tensor_sum_with_axis_eval
# LANG: _008y --> _008A
# SHAPES: (2, 200, 3) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v287__008A = np.sum(v286__008y, axis = (2,)).reshape((2, 200))

# op _001p_linear_combination_eval
# LANG: _001n, _001o --> _001q
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.ComputeLiftingSurfaceNormals
v46__001q = v44__001n+-1*v45__001o

# op _001t_linear_combination_eval
# LANG: _001r, _001s --> _001u
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.ComputeLiftingSurfaceNormals
v49__001u = v47__001r+-1*v48__001s

# op _008D_linear_combination_eval
# LANG: _008C, _008A --> _008E
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v289__008E = v288__008C+v287__008A

# op _008H_power_combination_eval
# LANG: _007v --> _008I
# SHAPES: (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v291__008I = (v253__007v**-1)
v291__008I = v291__008I.reshape((2, 200))

# op _008J_power_combination_eval
# LANG: _007P --> _008K
# SHAPES: (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v292__008K = (v263__007P**-1)
v292__008K = v292__008K.reshape((2, 200))

# op _008Z_single_tensor_sum_with_axis_eval
# LANG: _008Y --> _008_
# SHAPES: (2, 200, 3) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v300__008_ = np.sum(v299__008Y, axis = (2,)).reshape((2, 200))

# op _008r_power_combination_eval
# LANG: _008q --> _008s
# SHAPES: (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v283__008s = (v282__008q**0.5)
v283__008s = v283__008s.reshape((2, 200))

# op _0090_power_combination_eval
# LANG: _0088, _007P --> _0091
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v301__0091 = (v263__007P)*(v273__0088)
v301__0091 = v301__0091.reshape((2, 200))

# op _009m_power_combination_eval
# LANG: _008m, _0082 --> _009n
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v312__009n = (v270__0082)*(v280__008m)
v312__009n = v312__009n.reshape((2, 200, 3))

# op _001v cross_product_eval
# LANG: _001q, _001u --> _001w
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.ComputeLiftingSurfaceNormals
v50__001w = np.cross(v46__001q, v49__001u, axisa = 3, axisb = 3, axisc = 3)

# op _008F_power_combination_eval
# LANG: _008E --> _008G
# SHAPES: (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v290__008G = (v289__008E**-1)
v290__008G = v290__008G.reshape((2, 200))

# op _008L_linear_combination_eval
# LANG: _008I, _008K --> _008M
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v293__008M = v291__008I+v292__008K

# op _0092_linear_combination_eval
# LANG: _0091, _008_ --> _0093
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v302__0093 = v301__0091+v300__008_

# op _0096_power_combination_eval
# LANG: _007P --> _0097
# SHAPES: (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v304__0097 = (v263__007P**-1)
v304__0097 = v304__0097.reshape((2, 200))

# op _0098_power_combination_eval
# LANG: _0088 --> _0099
# SHAPES: (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v305__0099 = (v273__0088**-1)
v305__0099 = v305__0099.reshape((2, 200))

# op _009M_power_combination_eval
# LANG: _008m, _007p --> _009N
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v325__009N = (v280__008m)*(v250__007p)
v325__009N = v325__009N.reshape((2, 200, 3))

# op _009o_single_tensor_sum_with_axis_eval
# LANG: _009n --> _009p
# SHAPES: (2, 200, 3) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v313__009p = np.sum(v312__009n, axis = (2,)).reshape((2, 200))

# op _009q_power_combination_eval
# LANG: _008s, _0088 --> _009r
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v314__009r = (v273__0088)*(v283__008s)
v314__009r = v314__009r.reshape((2, 200))

# op _001x_power_combination_eval
# LANG: _001w --> _001y
# SHAPES: (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.ComputeLiftingSurfaceNormals
v51__001y = (v50__001w**2)
v51__001y = v51__001y.reshape((2, 2, 10, 3))

# op _0035_decompose_eval
# LANG: surface_bound_vtx_coords --> _0036, _0037, _0038, _0039
# SHAPES: (2, 3, 11, 3) --> (2, 2, 10, 3), (2, 2, 10, 3), (2, 2, 10, 3), (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v108__0036 = ((v229_surface_bound_vtx_coords.flatten())[src_indices__0036__0035]).reshape((2, 2, 10, 3))
v109__0037 = ((v229_surface_bound_vtx_coords.flatten())[src_indices__0037__0035]).reshape((2, 2, 10, 3))
v110__0038 = ((v229_surface_bound_vtx_coords.flatten())[src_indices__0038__0035]).reshape((2, 2, 10, 3))
v111__0039 = ((v229_surface_bound_vtx_coords.flatten())[src_indices__0039__0035]).reshape((2, 2, 10, 3))

# op _008N_power_combination_eval
# LANG: _008G, _008M --> _008O
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v294__008O = (v290__008G)*(v293__008M)
v294__008O = v294__008O.reshape((2, 200))

# op _008t cross_product_eval
# LANG: _007p, _007J --> _008u
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v284__008u = np.cross(v250__007p, v260__007J, axisa = 2, axisb = 2, axisc = 2)

# op _0094_power_combination_eval
# LANG: _0093 --> _0095
# SHAPES: (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v303__0095 = (v302__0093**-1)
v303__0095 = v303__0095.reshape((2, 200))

# op _009O_single_tensor_sum_with_axis_eval
# LANG: _009N --> _009P
# SHAPES: (2, 200, 3) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v326__009P = np.sum(v325__009N, axis = (2,)).reshape((2, 200))

# op _009Q_power_combination_eval
# LANG: _007v, _008s --> _009R
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v327__009R = (v283__008s)*(v253__007v)
v327__009R = v327__009R.reshape((2, 200))

# op _009a_linear_combination_eval
# LANG: _0097, _0099 --> _009b
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v306__009b = v304__0097+v305__0099

# op _009s_linear_combination_eval
# LANG: _009r, _009p --> _009t
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v315__009t = v314__009r+v313__009p

# op _009w_power_combination_eval
# LANG: _0088 --> _009x
# SHAPES: (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v317__009x = (v273__0088**-1)
v317__009x = v317__009x.reshape((2, 200))

# op _009y_power_combination_eval
# LANG: _008s --> _009z
# SHAPES: (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v318__009z = (v283__008s**-1)
v318__009z = v318__009z.reshape((2, 200))

# op _001z_single_tensor_sum_with_axis_eval
# LANG: _001y --> _001A
# SHAPES: (2, 2, 10, 3) --> (2, 2, 10)
# full namespace: VLMFixedWakeSystem.ComputeLiftingSurfaceNormals
v52__001A = np.sum(v51__001y, axis = (3,)).reshape((2, 2, 10))

# op _003A reshape_eval
# LANG: _0037 --> _003B
# SHAPES: (2, 2, 10, 3) --> (2, 20, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v125__003B = v109__0037.reshape((2, 20, 3))

# op _003a reshape_eval
# LANG: surface_collocation_pts --> _003b
# SHAPES: (2, 2, 10, 3) --> (2, 20, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v112__003b = v238_surface_collocation_pts.reshape((2, 20, 3))

# op _003g reshape_eval
# LANG: _0036 --> _003h
# SHAPES: (2, 2, 10, 3) --> (2, 20, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v115__003h = v108__0036.reshape((2, 20, 3))

# op _003u reshape_eval
# LANG: surface_collocation_pts --> _003v
# SHAPES: (2, 2, 10, 3) --> (2, 20, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v122__003v = v238_surface_collocation_pts.reshape((2, 20, 3))

# op _008P expand_array_eval
# LANG: _008O --> _008Q
# SHAPES: (2, 200) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v295__008Q = np.einsum('ab,c->abc', v294__008O.reshape((2, 200)) ,np.ones((3,))).reshape((2, 200, 3))

# op _008T cross_product_eval
# LANG: _0082, _007J --> _008U
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v297__008U = np.cross(v260__007J, v270__0082, axisa = 2, axisb = 2, axisc = 2)

# op _008v_power_combination_eval
# LANG: _008u --> _008w
# SHAPES: (2, 200, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v285__008w = (v284__008u)
v285__008w = (v285__008w*_008v_coeff).reshape((2, 200, 3))

# op _009A_linear_combination_eval
# LANG: _009x, _009z --> _009B
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v319__009B = v317__009x+v318__009z

# op _009S_linear_combination_eval
# LANG: _009R, _009P --> _009T
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v328__009T = v327__009R+v326__009P

# op _009W_power_combination_eval
# LANG: _008s --> _009X
# SHAPES: (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v330__009X = (v283__008s**-1)
v330__009X = v330__009X.reshape((2, 200))

# op _009Y_power_combination_eval
# LANG: _007v --> _009Z
# SHAPES: (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v331__009Z = (v253__007v**-1)
v331__009Z = v331__009Z.reshape((2, 200))

# op _009c_power_combination_eval
# LANG: _0095, _009b --> _009d
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v307__009d = (v303__0095)*(v306__009b)
v307__009d = v307__009d.reshape((2, 200))

# op _009u_power_combination_eval
# LANG: _009t --> _009v
# SHAPES: (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v316__009v = (v315__009t**-1)
v316__009v = v316__009v.reshape((2, 200))

# op _001B_power_combination_eval
# LANG: _001A --> _001C
# SHAPES: (2, 2, 10) --> (2, 2, 10)
# full namespace: VLMFixedWakeSystem.ComputeLiftingSurfaceNormals
v53__001C = (v52__001A**0.5)
v53__001C = v53__001C.reshape((2, 2, 10))

# op _003C expand_array_eval
# LANG: _003B --> _003D
# SHAPES: (2, 20, 3) --> (2, 20, 20, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v126__003D = np.einsum('acd,b->abcd', v125__003B.reshape((2, 20, 3)) ,np.ones((20,))).reshape((2, 20, 20, 3))

# op _003O reshape_eval
# LANG: surface_collocation_pts --> _003P
# SHAPES: (2, 2, 10, 3) --> (2, 20, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v132__003P = v238_surface_collocation_pts.reshape((2, 20, 3))

# op _003U reshape_eval
# LANG: _0038 --> _003V
# SHAPES: (2, 2, 10, 3) --> (2, 20, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v135__003V = v110__0038.reshape((2, 20, 3))

# op _003c expand_array_eval
# LANG: _003b --> _003d
# SHAPES: (2, 20, 3) --> (2, 20, 20, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v113__003d = np.einsum('abd,c->abcd', v112__003b.reshape((2, 20, 3)) ,np.ones((20,))).reshape((2, 20, 20, 3))

# op _003i expand_array_eval
# LANG: _003h --> _003j
# SHAPES: (2, 20, 3) --> (2, 20, 20, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v116__003j = np.einsum('acd,b->abcd', v115__003h.reshape((2, 20, 3)) ,np.ones((20,))).reshape((2, 20, 20, 3))

# op _003w expand_array_eval
# LANG: _003v --> _003x
# SHAPES: (2, 20, 3) --> (2, 20, 20, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v123__003x = np.einsum('abd,c->abcd', v122__003v.reshape((2, 20, 3)) ,np.ones((20,))).reshape((2, 20, 20, 3))

# op _008R_power_combination_eval
# LANG: _008Q, _008w --> _008S
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v296__008S = (v295__008Q)*(v285__008w)
v296__008S = v296__008S.reshape((2, 200, 3))

# op _008V_power_combination_eval
# LANG: _008U --> _008W
# SHAPES: (2, 200, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v298__008W = (v297__008U)
v298__008W = (v298__008W*_008V_coeff).reshape((2, 200, 3))

# op _009C_power_combination_eval
# LANG: _009v, _009B --> _009D
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v320__009D = (v316__009v)*(v319__009B)
v320__009D = v320__009D.reshape((2, 200))

# op _009U_power_combination_eval
# LANG: _009T --> _009V
# SHAPES: (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v329__009V = (v328__009T**-1)
v329__009V = v329__009V.reshape((2, 200))

# op _009__linear_combination_eval
# LANG: _009X, _009Z --> _00a0
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v332__00a0 = v330__009X+v331__009Z

# op _009e expand_array_eval
# LANG: _009d --> _009f
# SHAPES: (2, 200) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v308__009f = np.einsum('ab,c->abc', v307__009d.reshape((2, 200)) ,np.ones((3,))).reshape((2, 200, 3))

# op _009i cross_product_eval
# LANG: _008m, _0082 --> _009j
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v310__009j = np.cross(v270__0082, v280__008m, axisa = 2, axisb = 2, axisc = 2)

# op _001D expand_array_eval
# LANG: _001C --> _001E
# SHAPES: (2, 2, 10) --> (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.ComputeLiftingSurfaceNormals
v54__001E = np.einsum('abc,d->abcd', v53__001C.reshape((2, 2, 10)) ,np.ones((3,))).reshape((2, 2, 10, 3))

# op _003E reshape_eval
# LANG: _003D --> _003F
# SHAPES: (2, 20, 20, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v127__003F = v126__003D.reshape((2, 400, 3))

# op _003Q expand_array_eval
# LANG: _003P --> _003R
# SHAPES: (2, 20, 3) --> (2, 20, 20, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v133__003R = np.einsum('abd,c->abcd', v132__003P.reshape((2, 20, 3)) ,np.ones((20,))).reshape((2, 20, 20, 3))

# op _003W expand_array_eval
# LANG: _003V --> _003X
# SHAPES: (2, 20, 3) --> (2, 20, 20, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v136__003X = np.einsum('acd,b->abcd', v135__003V.reshape((2, 20, 3)) ,np.ones((20,))).reshape((2, 20, 20, 3))

# op _003e reshape_eval
# LANG: _003d --> _003f
# SHAPES: (2, 20, 20, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v114__003f = v113__003d.reshape((2, 400, 3))

# op _003k reshape_eval
# LANG: _003j --> _003l
# SHAPES: (2, 20, 20, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v117__003l = v116__003j.reshape((2, 400, 3))

# op _003y reshape_eval
# LANG: _003x --> _003z
# SHAPES: (2, 20, 20, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v124__003z = v123__003x.reshape((2, 400, 3))

# op _0047 reshape_eval
# LANG: surface_collocation_pts --> _0048
# SHAPES: (2, 2, 10, 3) --> (2, 20, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v142__0048 = v238_surface_collocation_pts.reshape((2, 20, 3))

# op _004d reshape_eval
# LANG: _0039 --> _004e
# SHAPES: (2, 2, 10, 3) --> (2, 20, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v145__004e = v111__0039.reshape((2, 20, 3))

# op _009E expand_array_eval
# LANG: _009D --> _009F
# SHAPES: (2, 200) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v321__009F = np.einsum('ab,c->abc', v320__009D.reshape((2, 200)) ,np.ones((3,))).reshape((2, 200, 3))

# op _009I cross_product_eval
# LANG: _008m, _007p --> _009J
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v323__009J = np.cross(v280__008m, v250__007p, axisa = 2, axisb = 2, axisc = 2)

# op _009g_power_combination_eval
# LANG: _009f, _008W --> _009h
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v309__009h = (v308__009f)*(v298__008W)
v309__009h = v309__009h.reshape((2, 200, 3))

# op _009k_power_combination_eval
# LANG: _009j --> _009l
# SHAPES: (2, 200, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v311__009l = (v310__009j)
v311__009l = (v311__009l*_009k_coeff).reshape((2, 200, 3))

# op _00a1_power_combination_eval
# LANG: _009V, _00a0 --> _00a2
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v333__00a2 = (v329__009V)*(v332__00a0)
v333__00a2 = v333__00a2.reshape((2, 200))

# op _00a7_linear_combination_eval
# LANG: _008S --> _00a8
# SHAPES: (2, 200, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v336__00a8 = v296__008S

# op _001F_power_combination_eval
# LANG: _001w, _001E --> surface_normals
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.ComputeLiftingSurfaceNormals
v342_surface_normals = (v50__001w)*(v54__001E**-1)
v342_surface_normals = v342_surface_normals.reshape((2, 2, 10, 3))

# op _003G_linear_combination_eval
# LANG: _003z, _003F --> _003H
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v128__003H = v124__003z+-1*v127__003F

# op _003S reshape_eval
# LANG: _003R --> _003T
# SHAPES: (2, 20, 20, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v134__003T = v133__003R.reshape((2, 400, 3))

# op _003Y reshape_eval
# LANG: _003X --> _003Z
# SHAPES: (2, 20, 20, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v137__003Z = v136__003X.reshape((2, 400, 3))

# op _003m_linear_combination_eval
# LANG: _003f, _003l --> _003n
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v118__003n = v114__003f+-1*v117__003l

# op _0049 expand_array_eval
# LANG: _0048 --> _004a
# SHAPES: (2, 20, 3) --> (2, 20, 20, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v143__004a = np.einsum('abd,c->abcd', v142__0048.reshape((2, 20, 3)) ,np.ones((20,))).reshape((2, 20, 20, 3))

# op _004f expand_array_eval
# LANG: _004e --> _004g
# SHAPES: (2, 20, 3) --> (2, 20, 20, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v146__004g = np.einsum('acd,b->abcd', v145__004e.reshape((2, 20, 3)) ,np.ones((20,))).reshape((2, 20, 20, 3))

# op _009G_power_combination_eval
# LANG: _009F, _009l --> _009H
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v322__009H = (v321__009F)*(v311__009l)
v322__009H = v322__009H.reshape((2, 200, 3))

# op _009K_power_combination_eval
# LANG: _009J --> _009L
# SHAPES: (2, 200, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v324__009L = (v323__009J)
v324__009L = (v324__009L*_009K_coeff).reshape((2, 200, 3))

# op _00a3 expand_array_eval
# LANG: _00a2 --> _00a4
# SHAPES: (2, 200) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v334__00a4 = np.einsum('ab,c->abc', v333__00a2.reshape((2, 200)) ,np.ones((3,))).reshape((2, 200, 3))

# op _00a9_linear_combination_eval
# LANG: _00a8, _009h --> _00aa
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v337__00aa = v336__00a8+v309__009h

# op _003I_power_combination_eval
# LANG: _003H --> _003J
# SHAPES: (2, 400, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v129__003J = (v128__003H**2)
v129__003J = v129__003J.reshape((2, 400, 3))

# op _003__linear_combination_eval
# LANG: _003T, _003Z --> _0040
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v138__0040 = v134__003T+-1*v137__003Z

# op _003o_power_combination_eval
# LANG: _003n --> _003p
# SHAPES: (2, 400, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v119__003p = (v118__003n**2)
v119__003p = v119__003p.reshape((2, 400, 3))

# op _004b reshape_eval
# LANG: _004a --> _004c
# SHAPES: (2, 20, 20, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v144__004c = v143__004a.reshape((2, 400, 3))

# op _004h reshape_eval
# LANG: _004g --> _004i
# SHAPES: (2, 20, 20, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v147__004i = v146__004g.reshape((2, 400, 3))

# op _00a5_power_combination_eval
# LANG: _00a4, _009L --> _00a6
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v335__00a6 = (v334__00a4)*(v324__009L)
v335__00a6 = v335__00a6.reshape((2, 200, 3))

# op _00ab_linear_combination_eval
# LANG: _00aa, _009H --> _00ac
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v338__00ac = v337__00aa+v322__009H

# op _00aj reshape_eval
# LANG: surface_normals --> _00ak
# SHAPES: (2, 2, 10, 3) --> (2, 20, 3)
# full namespace: VLMFixedWakeSystem.ProjectionWakeAic
v343__00ak = v342_surface_normals.reshape((2, 20, 3))

# op _003K_single_tensor_sum_with_axis_eval
# LANG: _003J --> _003L
# SHAPES: (2, 400, 3) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v130__003L = np.sum(v129__003J, axis = (2,)).reshape((2, 400))

# op _003q_single_tensor_sum_with_axis_eval
# LANG: _003p --> _003r
# SHAPES: (2, 400, 3) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v120__003r = np.sum(v119__003p, axis = (2,)).reshape((2, 400))

# op _0041_power_combination_eval
# LANG: _0040 --> _0042
# SHAPES: (2, 400, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v139__0042 = (v138__0040**2)
v139__0042 = v139__0042.reshape((2, 400, 3))

# op _004j_linear_combination_eval
# LANG: _004c, _004i --> _004k
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v148__004k = v144__004c+-1*v147__004i

# op _00ad_linear_combination_eval
# LANG: _00ac, _00a6 --> _00ae
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v339__00ae = v338__00ac+v335__00a6

# op _00al_indexed_passthrough_eval
# LANG: _00ak --> normal_concatenated_wake_aic_projection
# SHAPES: (2, 20, 3) --> (2, 20, 3)
# full namespace: VLMFixedWakeSystem.ProjectionWakeAic
v341_normal_concatenated_wake_aic_projection__temp[i_v343__00ak__00al_indexed_passthrough_eval] = v343__00ak.flatten()
v341_normal_concatenated_wake_aic_projection = v341_normal_concatenated_wake_aic_projection__temp.copy()

# op _003M_power_combination_eval
# LANG: _003L --> _003N
# SHAPES: (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v131__003N = (v130__003L**0.5)
v131__003N = v131__003N.reshape((2, 400))

# op _003s_power_combination_eval
# LANG: _003r --> _003t
# SHAPES: (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v121__003t = (v120__003r**0.5)
v121__003t = v121__003t.reshape((2, 400))

# op _0043_single_tensor_sum_with_axis_eval
# LANG: _0042 --> _0044
# SHAPES: (2, 400, 3) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v140__0044 = np.sum(v139__0042, axis = (2,)).reshape((2, 400))

# op _004l_power_combination_eval
# LANG: _004k --> _004m
# SHAPES: (2, 400, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v149__004m = (v148__004k**2)
v149__004m = v149__004m.reshape((2, 400, 3))

# op _004v_power_combination_eval
# LANG: _003n, _003H --> _004w
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v154__004w = (v118__003n)*(v128__003H)
v154__004w = v154__004w.reshape((2, 400, 3))

# op _00af reshape_eval
# LANG: _00ae --> wake_aic
# SHAPES: (2, 200, 3) --> (2, 20, 10, 3)
# full namespace: VLMFixedWakeSystem.WakeSubAicBiotSavarts
v344_wake_aic = v339__00ae.reshape((2, 20, 10, 3))

# op _00an expand_array_eval
# LANG: normal_concatenated_wake_aic_projection --> _00ao
# SHAPES: (2, 20, 3) --> (2, 20, 10, 3)
# full namespace: VLMFixedWakeSystem.ProjectionWakeAic
v345__00ao = np.einsum('abd,c->abcd', v341_normal_concatenated_wake_aic_projection.reshape((2, 20, 3)) ,np.ones((10,))).reshape((2, 20, 10, 3))

# op _0045_power_combination_eval
# LANG: _0044 --> _0046
# SHAPES: (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v141__0046 = (v140__0044**0.5)
v141__0046 = v141__0046.reshape((2, 400))

# op _004n_single_tensor_sum_with_axis_eval
# LANG: _004m --> _004o
# SHAPES: (2, 400, 3) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v150__004o = np.sum(v149__004m, axis = (2,)).reshape((2, 400))

# op _004x_single_tensor_sum_with_axis_eval
# LANG: _004w --> _004y
# SHAPES: (2, 400, 3) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v155__004y = np.sum(v154__004w, axis = (2,)).reshape((2, 400))

# op _004z_power_combination_eval
# LANG: _003t, _003N --> _004A
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v156__004A = (v121__003t)*(v131__003N)
v156__004A = v156__004A.reshape((2, 400))

# op _0050_power_combination_eval
# LANG: _0040, _003H --> _0051
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v170__0051 = (v128__003H)*(v138__0040)
v170__0051 = v170__0051.reshape((2, 400, 3))

# op _00ap_power_combination_eval
# LANG: _00ao, wake_aic --> _00aq
# SHAPES: (2, 20, 10, 3), (2, 20, 10, 3) --> (2, 20, 10, 3)
# full namespace: VLMFixedWakeSystem.ProjectionWakeAic
v346__00aq = (v344_wake_aic)*(v345__00ao)
v346__00aq = v346__00aq.reshape((2, 20, 10, 3))

# op _004B_linear_combination_eval
# LANG: _004A, _004y --> _004C
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v157__004C = v156__004A+v155__004y

# op _004H_linear_combination_eval
# LANG: _003t --> _004I
# SHAPES: (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v160__004I = _004H_constant+v121__003t

# op _004L_linear_combination_eval
# LANG: _003N --> _004M
# SHAPES: (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v162__004M = _004L_constant+v131__003N

# op _004p_power_combination_eval
# LANG: _004o --> _004q
# SHAPES: (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v151__004q = (v150__004o**0.5)
v151__004q = v151__004q.reshape((2, 400))

# op _0052_single_tensor_sum_with_axis_eval
# LANG: _0051 --> _0053
# SHAPES: (2, 400, 3) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v171__0053 = np.sum(v170__0051, axis = (2,)).reshape((2, 400))

# op _0054_power_combination_eval
# LANG: _0046, _003N --> _0055
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v172__0055 = (v131__003N)*(v141__0046)
v172__0055 = v172__0055.reshape((2, 400))

# op _005w_power_combination_eval
# LANG: _004k, _0040 --> _005x
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v186__005x = (v138__0040)*(v148__004k)
v186__005x = v186__005x.reshape((2, 400, 3))

# op _00ar_single_tensor_sum_with_axis_eval
# LANG: _00aq --> wake_aic_projection
# SHAPES: (2, 20, 10, 3) --> (2, 20, 10)
# full namespace: VLMFixedWakeSystem.ProjectionWakeAic
v347_wake_aic_projection = np.sum(v346__00aq, axis = (3,)).reshape((2, 20, 10))

# op _000e_power_combination_eval
# LANG: wake_aic_projection --> M_mat
# SHAPES: (2, 20, 10) --> (2, 20, 10)
# full namespace: VLMFixedWakeSystem
v3_M_mat = (v347_wake_aic_projection)
v3_M_mat = v3_M_mat.reshape((2, 20, 10))

# op _004D_linear_combination_eval
# LANG: _004C --> _004E
# SHAPES: (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v158__004E = _004D_constant+v157__004C

# op _004J_power_combination_eval
# LANG: _004I --> _004K
# SHAPES: (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v161__004K = (v160__004I**-1)
v161__004K = v161__004K.reshape((2, 400))

# op _004N_power_combination_eval
# LANG: _004M --> _004O
# SHAPES: (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v163__004O = (v162__004M**-1)
v163__004O = v163__004O.reshape((2, 400))

# op _0056_linear_combination_eval
# LANG: _0055, _0053 --> _0057
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v173__0057 = v172__0055+v171__0053

# op _005A_power_combination_eval
# LANG: _004q, _0046 --> _005B
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v188__005B = (v141__0046)*(v151__004q)
v188__005B = v188__005B.reshape((2, 400))

# op _005c_linear_combination_eval
# LANG: _003N --> _005d
# SHAPES: (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v176__005d = _005c_constant+v131__003N

# op _005g_linear_combination_eval
# LANG: _0046 --> _005h
# SHAPES: (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v178__005h = _005g_constant+v141__0046

# op _005y_single_tensor_sum_with_axis_eval
# LANG: _005x --> _005z
# SHAPES: (2, 400, 3) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v187__005z = np.sum(v186__005x, axis = (2,)).reshape((2, 400))

# op _0061_power_combination_eval
# LANG: _004k, _003n --> _0062
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v202__0062 = (v148__004k)*(v118__003n)
v202__0062 = v202__0062.reshape((2, 400, 3))

# op _000g_custom_explicit_eval
# LANG: M_mat --> M_reshaped
# SHAPES: (2, 20, 10) --> (2, 20, 20)
# full namespace: VLMFixedWakeSystem
temp = _000g_custom_explicit_func_M_reshaped.solve(v3_M_mat)
v4_M_reshaped = temp[0].copy()

# op _004F_power_combination_eval
# LANG: _004E --> _004G
# SHAPES: (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v159__004G = (v158__004E**-1)
v159__004G = v159__004G.reshape((2, 400))

# op _004P_linear_combination_eval
# LANG: _004K, _004O --> _004Q
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v164__004Q = v161__004K+v163__004O

# op _0058_linear_combination_eval
# LANG: _0057 --> _0059
# SHAPES: (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v174__0059 = _0058_constant+v173__0057

# op _005C_linear_combination_eval
# LANG: _005B, _005z --> _005D
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v189__005D = v188__005B+v187__005z

# op _005I_linear_combination_eval
# LANG: _0046 --> _005J
# SHAPES: (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v192__005J = _005I_constant+v141__0046

# op _005M_linear_combination_eval
# LANG: _004q --> _005N
# SHAPES: (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v194__005N = _005M_constant+v151__004q

# op _005e_power_combination_eval
# LANG: _005d --> _005f
# SHAPES: (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v177__005f = (v176__005d**-1)
v177__005f = v177__005f.reshape((2, 400))

# op _005i_power_combination_eval
# LANG: _005h --> _005j
# SHAPES: (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v179__005j = (v178__005h**-1)
v179__005j = v179__005j.reshape((2, 400))

# op _0063_single_tensor_sum_with_axis_eval
# LANG: _0062 --> _0064
# SHAPES: (2, 400, 3) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v203__0064 = np.sum(v202__0062, axis = (2,)).reshape((2, 400))

# op _0065_power_combination_eval
# LANG: _003t, _004q --> _0066
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v204__0066 = (v151__004q)*(v121__003t)
v204__0066 = v204__0066.reshape((2, 400))

# op _004R_power_combination_eval
# LANG: _004G, _004Q --> num_004S
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v165_num_004S = (v159__004G)*(v164__004Q)
v165_num_004S = v165_num_004S.reshape((2, 400))

# op _004r cross_product_eval
# LANG: _003n, _003H --> _004s
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v152__004s = np.cross(v118__003n, v128__003H, axisa = 2, axisb = 2, axisc = 2)

# op _005E_linear_combination_eval
# LANG: _005D --> _005F
# SHAPES: (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v190__005F = _005E_constant+v189__005D

# op _005K_power_combination_eval
# LANG: _005J --> _005L
# SHAPES: (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v193__005L = (v192__005J**-1)
v193__005L = v193__005L.reshape((2, 400))

# op _005O_power_combination_eval
# LANG: _005N --> _005P
# SHAPES: (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v195__005P = (v194__005N**-1)
v195__005P = v195__005P.reshape((2, 400))

# op _005a_power_combination_eval
# LANG: _0059 --> _005b
# SHAPES: (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v175__005b = (v174__0059**-1)
v175__005b = v175__005b.reshape((2, 400))

# op _005k_linear_combination_eval
# LANG: _005f, _005j --> _005l
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v180__005l = v177__005f+v179__005j

# op _0067_linear_combination_eval
# LANG: _0066, _0064 --> _0068
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v205__0068 = v204__0066+v203__0064

# op _006d_linear_combination_eval
# LANG: _004q --> _006e
# SHAPES: (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v208__006e = _006d_constant+v151__004q

# op _006h_linear_combination_eval
# LANG: _003t --> _006i
# SHAPES: (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v210__006i = _006h_constant+v121__003t

# op _004T expand_array_eval
# LANG: num_004S --> _004U
# SHAPES: (2, 400) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v166__004U = np.einsum('ab,c->abc', v165_num_004S.reshape((2, 400)) ,np.ones((3,))).reshape((2, 400, 3))

# op _004X cross_product_eval
# LANG: _0040, _003H --> _004Y
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v168__004Y = np.cross(v128__003H, v138__0040, axisa = 2, axisb = 2, axisc = 2)

# op _004t_power_combination_eval
# LANG: _004s --> _004u
# SHAPES: (2, 400, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v153__004u = (v152__004s)
v153__004u = (v153__004u*_004t_coeff).reshape((2, 400, 3))

# op _005G_power_combination_eval
# LANG: _005F --> _005H
# SHAPES: (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v191__005H = (v190__005F**-1)
v191__005H = v191__005H.reshape((2, 400))

# op _005Q_linear_combination_eval
# LANG: _005L, _005P --> _005R
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v196__005R = v193__005L+v195__005P

# op _005m_power_combination_eval
# LANG: _005b, _005l --> num_005n
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v181_num_005n = (v175__005b)*(v180__005l)
v181_num_005n = v181_num_005n.reshape((2, 400))

# op _0069_linear_combination_eval
# LANG: _0068 --> _006a
# SHAPES: (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v206__006a = _0069_constant+v205__0068

# op _006f_power_combination_eval
# LANG: _006e --> _006g
# SHAPES: (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v209__006g = (v208__006e**-1)
v209__006g = v209__006g.reshape((2, 400))

# op _006j_power_combination_eval
# LANG: _006i --> _006k
# SHAPES: (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v211__006k = (v210__006i**-1)
v211__006k = v211__006k.reshape((2, 400))

# op _004V_power_combination_eval
# LANG: _004U, _004u --> _004W
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v167__004W = (v166__004U)*(v153__004u)
v167__004W = v167__004W.reshape((2, 400, 3))

# op _004Z_power_combination_eval
# LANG: _004Y --> _004_
# SHAPES: (2, 400, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v169__004_ = (v168__004Y)
v169__004_ = (v169__004_*_004Z_coeff).reshape((2, 400, 3))

# op _005S_power_combination_eval
# LANG: _005H, _005R --> num_005T
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v197_num_005T = (v191__005H)*(v196__005R)
v197_num_005T = v197_num_005T.reshape((2, 400))

# op _005o expand_array_eval
# LANG: num_005n --> _005p
# SHAPES: (2, 400) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v182__005p = np.einsum('ab,c->abc', v181_num_005n.reshape((2, 400)) ,np.ones((3,))).reshape((2, 400, 3))

# op _005s cross_product_eval
# LANG: _004k, _0040 --> _005t
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v184__005t = np.cross(v138__0040, v148__004k, axisa = 2, axisb = 2, axisc = 2)

# op _006b_power_combination_eval
# LANG: _006a --> _006c
# SHAPES: (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v207__006c = (v206__006a**-1)
v207__006c = v207__006c.reshape((2, 400))

# op _006l_linear_combination_eval
# LANG: _006g, _006k --> _006m
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v212__006m = v209__006g+v211__006k

# op _005U expand_array_eval
# LANG: num_005T --> _005V
# SHAPES: (2, 400) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v198__005V = np.einsum('ab,c->abc', v197_num_005T.reshape((2, 400)) ,np.ones((3,))).reshape((2, 400, 3))

# op _005Y cross_product_eval
# LANG: _004k, _003n --> _005Z
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v200__005Z = np.cross(v148__004k, v118__003n, axisa = 2, axisb = 2, axisc = 2)

# op _005q_power_combination_eval
# LANG: _005p, _004_ --> _005r
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v183__005r = (v182__005p)*(v169__004_)
v183__005r = v183__005r.reshape((2, 400, 3))

# op _005u_power_combination_eval
# LANG: _005t --> _005v
# SHAPES: (2, 400, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v185__005v = (v184__005t)
v185__005v = (v185__005v*_005u_coeff).reshape((2, 400, 3))

# op _006n_power_combination_eval
# LANG: _006c, _006m --> num_006o
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v213_num_006o = (v207__006c)*(v212__006m)
v213_num_006o = v213_num_006o.reshape((2, 400))

# op _006t_linear_combination_eval
# LANG: _004W --> _006u
# SHAPES: (2, 400, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v216__006u = v167__004W

# op _002Q expand_array_eval
# LANG: frame_vel --> _002R
# SHAPES: (2, 3) --> (2, 20, 3)
# full namespace: VLMFixedWakeSystem.KinematicVelocity
v98__002R = np.einsum('ac,b->abc', v228_frame_vel.reshape((2, 3)) ,np.ones((20,))).reshape((2, 20, 3))

# op _005W_power_combination_eval
# LANG: _005V, _005v --> _005X
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v199__005X = (v198__005V)*(v185__005v)
v199__005X = v199__005X.reshape((2, 400, 3))

# op _005__power_combination_eval
# LANG: _005Z --> _0060
# SHAPES: (2, 400, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v201__0060 = (v200__005Z)
v201__0060 = (v201__0060*_005__coeff).reshape((2, 400, 3))

# op _006p expand_array_eval
# LANG: num_006o --> _006q
# SHAPES: (2, 400) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v214__006q = np.einsum('ab,c->abc', v213_num_006o.reshape((2, 400)) ,np.ones((3,))).reshape((2, 400, 3))

# op _006v_linear_combination_eval
# LANG: _006u, _005r --> _006w
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v217__006w = v216__006u+v183__005r

# op _002S_linear_combination_eval
# LANG: _002R --> surface_kinematic_vel
# SHAPES: (2, 20, 3) --> (2, 20, 3)
# full namespace: VLMFixedWakeSystem.KinematicVelocity
v101_surface_kinematic_vel = -1*v98__002R

# op _002X reshape_eval
# LANG: surface_normals --> _002Y
# SHAPES: (2, 2, 10, 3) --> (2, 20, 3)
# full namespace: VLMFixedWakeSystem.Projection_rhs
v103__002Y = v342_surface_normals.reshape((2, 20, 3))

# op _006F reshape_eval
# LANG: surface_normals --> _006G
# SHAPES: (2, 2, 10, 3) --> (2, 20, 3)
# full namespace: VLMFixedWakeSystem.ProjectionLHSA
v223__006G = v342_surface_normals.reshape((2, 20, 3))

# op _006r_power_combination_eval
# LANG: _006q, _0060 --> _006s
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v215__006s = (v214__006q)*(v201__0060)
v215__006s = v215__006s.reshape((2, 400, 3))

# op _006x_linear_combination_eval
# LANG: _006w, _005X --> _006y
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v218__006y = v217__006w+v199__005X

# op _002Z_power_combination_eval
# LANG: _002Y, surface_kinematic_vel --> _002_
# SHAPES: (2, 20, 3), (2, 20, 3) --> (2, 20, 3)
# full namespace: VLMFixedWakeSystem.Projection_rhs
v104__002_ = (v101_surface_kinematic_vel)*(v103__002Y)
v104__002_ = v104__002_.reshape((2, 20, 3))

# op _006H_indexed_passthrough_eval
# LANG: _006G --> normal_concatenated_lhs_A_matrix
# SHAPES: (2, 20, 3) --> (2, 20, 3)
# full namespace: VLMFixedWakeSystem.ProjectionLHSA
v221_normal_concatenated_lhs_A_matrix__temp[i_v223__006G__006H_indexed_passthrough_eval] = v223__006G.flatten()
v221_normal_concatenated_lhs_A_matrix = v221_normal_concatenated_lhs_A_matrix__temp.copy()

# op _006z_linear_combination_eval
# LANG: _006y, _006s --> _006A
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v219__006A = v218__006y+v215__006s

# op _0030_single_tensor_sum_with_axis_eval
# LANG: _002_ --> _0031
# SHAPES: (2, 20, 3) --> (2, 20)
# full namespace: VLMFixedWakeSystem.Projection_rhs
v105__0031 = np.sum(v104__002_, axis = (2,)).reshape((2, 20))

# op _006B reshape_eval
# LANG: _006A --> bound_aic
# SHAPES: (2, 400, 3) --> (2, 20, 20, 3)
# full namespace: VLMFixedWakeSystem.SubAicBiotSavarts
v224_bound_aic = v219__006A.reshape((2, 20, 20, 3))

# op _006J expand_array_eval
# LANG: normal_concatenated_lhs_A_matrix --> _006K
# SHAPES: (2, 20, 3) --> (2, 20, 20, 3)
# full namespace: VLMFixedWakeSystem.ProjectionLHSA
v225__006K = np.einsum('abd,c->abcd', v221_normal_concatenated_lhs_A_matrix.reshape((2, 20, 3)) ,np.ones((20,))).reshape((2, 20, 20, 3))

# op _0032_indexed_passthrough_eval
# LANG: _0031 --> rhs
# SHAPES: (2, 20) --> (2, 20)
# full namespace: VLMFixedWakeSystem.Projection_rhs
v100_rhs__temp[i_v105__0031__0032_indexed_passthrough_eval] = v105__0031.flatten()
v100_rhs = v100_rhs__temp.copy()

# op _006L_power_combination_eval
# LANG: _006K, bound_aic --> _006M
# SHAPES: (2, 20, 20, 3), (2, 20, 20, 3) --> (2, 20, 20, 3)
# full namespace: VLMFixedWakeSystem.ProjectionLHSA
v226__006M = (v224_bound_aic)*(v225__006K)
v226__006M = v226__006M.reshape((2, 20, 20, 3))

# op _000j reshape_eval
# LANG: M_reshaped --> _000k
# SHAPES: (2, 20, 20) --> (2, 20, 20)
# full namespace: VLMFixedWakeSystem
v6__000k = v4_M_reshaped.reshape((2, 20, 20))

# op _000u_decompose_eval
# LANG: rhs --> _000O, _000v
# SHAPES: (2, 20) --> (1, 20), (1, 20)
# full namespace: VLMFixedWakeSystem
v13__000v = ((v100_rhs.flatten())[src_indices__000v__000u]).reshape((1, 20))
v23__000O = ((v100_rhs.flatten())[src_indices__000O__000u]).reshape((1, 20))

# op _002c_decompose_eval
# LANG: surface --> _002q, _002d, _002g, _002l
# SHAPES: (2, 3, 11, 3) --> (2, 2, 10, 3), (2, 2, 10, 3), (2, 2, 10, 3), (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.GeometricPropertyExtraction
v76__002d = ((v75_surface.flatten())[src_indices__002d__002c]).reshape((2, 2, 10, 3))
v78__002g = ((v75_surface.flatten())[src_indices__002g__002c]).reshape((2, 2, 10, 3))
v81__002l = ((v75_surface.flatten())[src_indices__002l__002c]).reshape((2, 2, 10, 3))
v84__002q = ((v75_surface.flatten())[src_indices__002q__002c]).reshape((2, 2, 10, 3))

# op _006N_single_tensor_sum_with_axis_eval
# LANG: _006M --> lhs_A_matrix
# SHAPES: (2, 20, 20, 3) --> (2, 20, 20)
# full namespace: VLMFixedWakeSystem.ProjectionLHSA
v227_lhs_A_matrix = np.sum(v226__006M, axis = (3,)).reshape((2, 20, 20))

# op _000P reshape_eval
# LANG: _000O --> _000Q
# SHAPES: (1, 20) --> (20,)
# full namespace: VLMFixedWakeSystem
v24__000Q = v23__000O.reshape((20,))

# op _000l_linear_combination_eval
# LANG: _000k, lhs_A_matrix --> MTX
# SHAPES: (2, 20, 20), (2, 20, 20) --> (2, 20, 20)
# full namespace: VLMFixedWakeSystem
v8_MTX = v227_lhs_A_matrix+v6__000k

# op _000w reshape_eval
# LANG: _000v --> _000x
# SHAPES: (1, 20) --> (20,)
# full namespace: VLMFixedWakeSystem
v14__000x = v13__000v.reshape((20,))

# op _002w_power_combination_eval
# LANG: _002d --> _002x
# SHAPES: (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.GeometricPropertyExtraction
v88__002x = (v76__002d)
v88__002x = (v88__002x*_002w_coeff).reshape((2, 2, 10, 3))

# op _002y_power_combination_eval
# LANG: _002l --> _002z
# SHAPES: (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.GeometricPropertyExtraction
v89__002z = (v81__002l)
v89__002z = (v89__002z*_002y_coeff).reshape((2, 2, 10, 3))

# op _000R_linear_combination_eval
# LANG: _000Q --> _000S
# SHAPES: (20,) --> (20,)
# full namespace: VLMFixedWakeSystem
v25__000S = -1*v24__000Q

# op _000q_decompose_eval
# LANG: MTX --> _000L, _000r
# SHAPES: (2, 20, 20) --> (1, 20, 20), (1, 20, 20)
# full namespace: VLMFixedWakeSystem
v11__000r = ((v8_MTX.flatten())[src_indices__000r__000q]).reshape((1, 20, 20))
v21__000L = ((v8_MTX.flatten())[src_indices__000L__000q]).reshape((1, 20, 20))

# op _000y_linear_combination_eval
# LANG: _000x --> _000z
# SHAPES: (20,) --> (20,)
# full namespace: VLMFixedWakeSystem
v15__000z = -1*v14__000x

# op _001X_linear_combination_eval
# LANG: _001V, _001W --> _001Y
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.GeometricPropertyExtraction
v67__001Y = v65__001V+-1*v66__001W

# op _001__linear_combination_eval
# LANG: _001Z, _001Q --> _0020
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.GeometricPropertyExtraction
v69__0020 = v68__001Z+-1*v62__001Q

# op _002A_linear_combination_eval
# LANG: _002x, _002z --> _002B
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.GeometricPropertyExtraction
v90__002B = v88__002x+v89__002z

# op _002C_power_combination_eval
# LANG: _002g --> _002D
# SHAPES: (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.GeometricPropertyExtraction
v91__002D = (v78__002g)
v91__002D = (v91__002D*_002C_coeff).reshape((2, 2, 10, 3))

# op _000A reshape_eval
# LANG: _000z --> _000B
# SHAPES: (20,) --> (20, 1)
# full namespace: VLMFixedWakeSystem
v16__000B = v15__000z.reshape((20, 1))

# op _000M reshape_eval
# LANG: _000L --> _000N
# SHAPES: (1, 20, 20) --> (20, 20)
# full namespace: VLMFixedWakeSystem
v22__000N = v21__000L.reshape((20, 20))

# op _000T reshape_eval
# LANG: _000S --> _000U
# SHAPES: (20,) --> (20, 1)
# full namespace: VLMFixedWakeSystem
v26__000U = v25__000S.reshape((20, 1))

# op _000s reshape_eval
# LANG: _000r --> _000t
# SHAPES: (1, 20, 20) --> (20, 20)
# full namespace: VLMFixedWakeSystem
v12__000t = v11__000r.reshape((20, 20))

# op _0021 cross_product_eval
# LANG: _001Y, _0020 --> _0022
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.GeometricPropertyExtraction
v70__0022 = np.cross(v67__001Y, v69__0020, axisa = 3, axisb = 3, axisc = 3)

# op _002E_linear_combination_eval
# LANG: _002B, _002D --> _002F
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.GeometricPropertyExtraction
v92__002F = v90__002B+-1*v91__002D

# op _002G_power_combination_eval
# LANG: _002q --> _002H
# SHAPES: (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.GeometricPropertyExtraction
v93__002H = (v84__002q)
v93__002H = (v93__002H*_002G_coeff).reshape((2, 2, 10, 3))

# op _000C_solve_linear_system_eval
# LANG: _000t, _000B --> _000D
# SHAPES: (20, 20), (20, 1) --> (20, 1)
# full namespace: VLMFixedWakeSystem
v17__000D = _000Cv17__000D_solver(v12__000t, v16__000B, False)

# op _000V_solve_linear_system_eval
# LANG: _000N, _000U --> _000W
# SHAPES: (20, 20), (20, 1) --> (20, 1)
# full namespace: VLMFixedWakeSystem
v27__000W = _000Vv27__000W_solver(v22__000N, v26__000U, False)

# op _0023_power_combination_eval
# LANG: _0022 --> _0024
# SHAPES: (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.GeometricPropertyExtraction
v71__0024 = (v70__0022**2)
v71__0024 = v71__0024.reshape((2, 2, 10, 3))

# op _002I_linear_combination_eval
# LANG: _002F, _002H --> _002J
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.GeometricPropertyExtraction
v94__002J = v92__002F+-1*v93__002H

# op _002e_power_combination_eval
# LANG: _002d --> _002f
# SHAPES: (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.GeometricPropertyExtraction
v77__002f = (v76__002d)
v77__002f = (v77__002f*_002e_coeff).reshape((2, 2, 10, 3))

# op _002h_power_combination_eval
# LANG: _002g --> _002i
# SHAPES: (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.GeometricPropertyExtraction
v79__002i = (v78__002g)
v79__002i = (v79__002i*_002h_coeff).reshape((2, 2, 10, 3))

# op _000E reshape_eval
# LANG: _000D --> _000F
# SHAPES: (20, 1) --> (20,)
# full namespace: VLMFixedWakeSystem
v18__000F = v17__000D.reshape((20,))

# op _000X reshape_eval
# LANG: _000W --> _000Y
# SHAPES: (20, 1) --> (20,)
# full namespace: VLMFixedWakeSystem
v28__000Y = v27__000W.reshape((20,))

# op _0025_single_tensor_sum_with_axis_eval
# LANG: _0024 --> _0026
# SHAPES: (2, 2, 10, 3) --> (2, 2, 10)
# full namespace: VLMFixedWakeSystem.GeometricPropertyExtraction
v72__0026 = np.sum(v71__0024, axis = (3,)).reshape((2, 2, 10))

# op _002K reshape_eval
# LANG: _002J --> _002L
# SHAPES: (2, 2, 10, 3) --> (2, 20, 3)
# full namespace: VLMFixedWakeSystem.GeometricPropertyExtraction
v95__002L = v94__002J.reshape((2, 20, 3))

# op _002j_linear_combination_eval
# LANG: _002f, _002i --> _002k
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.GeometricPropertyExtraction
v80__002k = v77__002f+v79__002i

# op _002m_power_combination_eval
# LANG: _002l --> _002n
# SHAPES: (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.GeometricPropertyExtraction
v82__002n = (v81__002l)
v82__002n = (v82__002n*_002m_coeff).reshape((2, 2, 10, 3))

# op _000I reshape_eval
# LANG: _000F --> _000J
# SHAPES: (20,) --> (1, 20)
# full namespace: VLMFixedWakeSystem
v20__000J = v18__000F.reshape((1, 20))

# op _000_ reshape_eval
# LANG: _000Y --> _0010
# SHAPES: (20,) --> (1, 20)
# full namespace: VLMFixedWakeSystem
v30__0010 = v28__000Y.reshape((1, 20))

# op _0027_power_combination_eval
# LANG: _0026 --> _0028
# SHAPES: (2, 2, 10) --> (2, 2, 10)
# full namespace: VLMFixedWakeSystem.GeometricPropertyExtraction
v73__0028 = (v72__0026**0.5)
v73__0028 = v73__0028.reshape((2, 2, 10))

# op _002M_linear_combination_eval
# LANG: _002L --> _002N
# SHAPES: (2, 20, 3) --> (2, 20, 3)
# full namespace: VLMFixedWakeSystem.GeometricPropertyExtraction
v96__002N = -1*v95__002L

# op _002o_linear_combination_eval
# LANG: _002k, _002n --> _002p
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.GeometricPropertyExtraction
v83__002p = v80__002k+v82__002n

# op _002r_power_combination_eval
# LANG: _002q --> _002s
# SHAPES: (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.GeometricPropertyExtraction
v85__002s = (v84__002q)
v85__002s = (v85__002s*_002r_coeff).reshape((2, 2, 10, 3))

# op _000K_indexed_passthrough_eval
# LANG: _000J, _0010 --> circulation_strength
# SHAPES: (1, 20), (1, 20) --> (2, 20)
# full namespace: VLMFixedWakeSystem
v10_circulation_strength__temp[i_v20__000J__000K_indexed_passthrough_eval] = v20__000J.flatten()
v10_circulation_strength = v10_circulation_strength__temp.copy()
v10_circulation_strength__temp[i_v30__0010__000K_indexed_passthrough_eval] = v30__0010.flatten()
v10_circulation_strength = v10_circulation_strength__temp.copy()

# op _0029_power_combination_eval
# LANG: _0028 --> surface_panel_areas
# SHAPES: (2, 2, 10) --> (2, 2, 10)
# full namespace: VLMFixedWakeSystem.GeometricPropertyExtraction
v74_surface_panel_areas = (v73__0028)
v74_surface_panel_areas = (v74_surface_panel_areas*_0029_coeff).reshape((2, 2, 10))

# op _002O_indexed_passthrough_eval
# LANG: _002N --> bound_vecs_all_surfaces
# SHAPES: (2, 20, 3) --> (2, 20, 3)
# full namespace: VLMFixedWakeSystem.GeometricPropertyExtraction
v87_bound_vecs_all_surfaces__temp[i_v96__002N__002O_indexed_passthrough_eval] = v96__002N.flatten()
v87_bound_vecs_all_surfaces = v87_bound_vecs_all_surfaces__temp.copy()

# op _002t_linear_combination_eval
# LANG: _002p, _002s --> surface_force_evaluation_pts
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: VLMFixedWakeSystem.GeometricPropertyExtraction
v86_surface_force_evaluation_pts = v83__002p+v85__002s