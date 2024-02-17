

# RUN_MODEL_

# system evaluation block

# op _0016_decompose_eval
# LANG: surface --> _001h, _0017, _001a, _001g
# SHAPES: (2, 3, 11, 3) --> (2, 1, 11, 3), (2, 2, 11, 3), (2, 2, 11, 3), (2, 1, 11, 3)
# full namespace: MeshToVortexMesh
v35__0017 = ((v77_surface.flatten())[src_indices__0017__0016]).reshape((2, 2, 11, 3))
v37__001a = ((v77_surface.flatten())[src_indices__001a__0016]).reshape((2, 2, 11, 3))
v40__001g = ((v77_surface.flatten())[src_indices__001g__0016]).reshape((2, 1, 11, 3))
v41__001h = ((v77_surface.flatten())[src_indices__001h__0016]).reshape((2, 1, 11, 3))

# op _001i_linear_combination_eval
# LANG: _001g, _001h --> _001j
# SHAPES: (2, 1, 11, 3), (2, 1, 11, 3) --> (2, 1, 11, 3)
# full namespace: MeshToVortexMesh
v42__001j = v40__001g+-1*v41__001h

# op _0018_power_combination_eval
# LANG: _0017 --> _0019
# SHAPES: (2, 2, 11, 3) --> (2, 2, 11, 3)
# full namespace: MeshToVortexMesh
v36__0019 = (v35__0017)
v36__0019 = (v36__0019*_0018_coeff).reshape((2, 2, 11, 3))

# op _001b_power_combination_eval
# LANG: _001a --> _001c
# SHAPES: (2, 2, 11, 3) --> (2, 2, 11, 3)
# full namespace: MeshToVortexMesh
v38__001c = (v37__001a)
v38__001c = (v38__001c*_001b_coeff).reshape((2, 2, 11, 3))

# op _001k_power_combination_eval
# LANG: _001j --> _001l
# SHAPES: (2, 1, 11, 3) --> (2, 1, 11, 3)
# full namespace: MeshToVortexMesh
v43__001l = (v42__001j)
v43__001l = (v43__001l*_001k_coeff).reshape((2, 1, 11, 3))

# op _001d_linear_combination_eval
# LANG: _0019, _001c --> _001e
# SHAPES: (2, 2, 11, 3), (2, 2, 11, 3) --> (2, 2, 11, 3)
# full namespace: MeshToVortexMesh
v39__001e = v36__0019+v38__001c

# op _001m_linear_combination_eval
# LANG: _001g, _001l --> _001n
# SHAPES: (2, 1, 11, 3), (2, 1, 11, 3) --> (2, 1, 11, 3)
# full namespace: MeshToVortexMesh
v44__001n = v40__001g+v43__001l

# op _001f_indexed_passthrough_eval
# LANG: _001e, _001n --> surface_bound_vtx_coords
# SHAPES: (2, 2, 11, 3), (2, 1, 11, 3) --> (2, 3, 11, 3)
# full namespace: MeshToVortexMesh
v232_surface_bound_vtx_coords__temp[i_v39__001e__001f_indexed_passthrough_eval] = v39__001e.flatten()
v232_surface_bound_vtx_coords = v232_surface_bound_vtx_coords__temp.copy()
v232_surface_bound_vtx_coords__temp[i_v44__001n__001f_indexed_passthrough_eval] = v44__001n.flatten()
v232_surface_bound_vtx_coords = v232_surface_bound_vtx_coords__temp.copy()

# op _001L_decompose_eval
# LANG: surface_bound_vtx_coords --> _001T, _001M, _001N, _001Q, _001Y, _001Z, _0021
# SHAPES: (2, 3, 11, 3) --> (2, 2, 10, 3), (2, 2, 10, 3), (2, 2, 10, 3), (2, 2, 10, 3), (2, 2, 10, 3), (2, 2, 10, 3), (2, 2, 10, 3)
# full namespace: GeometricPropertyExtraction
v59__001M = ((v232_surface_bound_vtx_coords.flatten())[src_indices__001M__001L]).reshape((2, 2, 10, 3))
v60__001N = ((v232_surface_bound_vtx_coords.flatten())[src_indices__001N__001L]).reshape((2, 2, 10, 3))
v62__001Q = ((v232_surface_bound_vtx_coords.flatten())[src_indices__001Q__001L]).reshape((2, 2, 10, 3))
v64__001T = ((v232_surface_bound_vtx_coords.flatten())[src_indices__001T__001L]).reshape((2, 2, 10, 3))
v67__001Y = ((v232_surface_bound_vtx_coords.flatten())[src_indices__001Y__001L]).reshape((2, 2, 10, 3))
v68__001Z = ((v232_surface_bound_vtx_coords.flatten())[src_indices__001Z__001L]).reshape((2, 2, 10, 3))
v70__0021 = ((v232_surface_bound_vtx_coords.flatten())[src_indices__0021__001L]).reshape((2, 2, 10, 3))

# op _006X_decompose_eval
# LANG: surface_bound_vtx_coords --> _006Y
# SHAPES: (2, 3, 11, 3) --> (2, 1, 11, 3)
# full namespace: GenerateFixedWake
v233__006Y = ((v232_surface_bound_vtx_coords.flatten())[src_indices__006Y__006X]).reshape((2, 1, 11, 3))

# op _0073_linear_combination_eval
# LANG: frame_vel --> _0074
# SHAPES: (2, 3) --> (2, 3)
# full namespace: GenerateFixedWake
v237__0074 = -1*v231_frame_vel

# op _001O_linear_combination_eval
# LANG: _001M, _001N --> _001P
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: GeometricPropertyExtraction
v61__001P = v59__001M+v60__001N

# op _006Z reshape_eval
# LANG: _006Y --> _006_
# SHAPES: (2, 1, 11, 3) --> (2, 11, 3)
# full namespace: GenerateFixedWake
v234__006_ = v233__006Y.reshape((2, 11, 3))

# op _0075 expand_array_eval
# LANG: _0074 --> _0076
# SHAPES: (2, 3) --> (2, 2, 11, 3)
# full namespace: GenerateFixedWake
v238__0076 = np.einsum('ad,bc->abcd', v237__0074.reshape((2, 3)) ,np.ones((2, 11))).reshape((2, 2, 11, 3))

# op _001R_linear_combination_eval
# LANG: _001Q, _001P --> _001S
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: GeometricPropertyExtraction
v63__001S = v61__001P+v62__001Q

# op _0070 expand_array_eval
# LANG: _006_ --> _0071
# SHAPES: (2, 11, 3) --> (2, 2, 11, 3)
# full namespace: GenerateFixedWake
v235__0071 = np.einsum('acd,b->abcd', v234__006_.reshape((2, 11, 3)) ,np.ones((2,))).reshape((2, 2, 11, 3))

# op _0077_power_combination_eval
# LANG: surface_factor, _0076 --> _0078
# SHAPES: (2, 2, 11, 3), (2, 2, 11, 3) --> (2, 2, 11, 3)
# full namespace: GenerateFixedWake
v239__0078 = (v238__0076)*(v236_surface_factor)
v239__0078 = v239__0078.reshape((2, 2, 11, 3))

# op _001U_linear_combination_eval
# LANG: _001T, _001S --> _001V
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: GeometricPropertyExtraction
v65__001V = v63__001S+v64__001T

# op _0079_linear_combination_eval
# LANG: _0071, _0078 --> surface_wake_coords
# SHAPES: (2, 2, 11, 3), (2, 2, 11, 3) --> (2, 2, 11, 3)
# full namespace: GenerateFixedWake
v348_surface_wake_coords = v235__0071+v239__0078

# op _001W_power_combination_eval
# LANG: _001V --> surface_collocation_pts
# SHAPES: (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: GeometricPropertyExtraction
v241_surface_collocation_pts = (v65__001V)
v241_surface_collocation_pts = (v241_surface_collocation_pts*_001W_coeff).reshape((2, 2, 10, 3))

# op _007l_decompose_eval
# LANG: surface_wake_coords --> _007m, _007n, _007o, _007p
# SHAPES: (2, 2, 11, 3) --> (2, 1, 10, 3), (2, 1, 10, 3), (2, 1, 10, 3), (2, 1, 10, 3)
# full namespace: WakeSubAicBiotSavarts
v247__007m = ((v348_surface_wake_coords.flatten())[src_indices__007m__007l]).reshape((2, 1, 10, 3))
v248__007n = ((v348_surface_wake_coords.flatten())[src_indices__007n__007l]).reshape((2, 1, 10, 3))
v249__007o = ((v348_surface_wake_coords.flatten())[src_indices__007o__007l]).reshape((2, 1, 10, 3))
v250__007p = ((v348_surface_wake_coords.flatten())[src_indices__007p__007l]).reshape((2, 1, 10, 3))

# op _007K reshape_eval
# LANG: surface_collocation_pts --> _007L
# SHAPES: (2, 2, 10, 3) --> (2, 20, 3)
# full namespace: WakeSubAicBiotSavarts
v261__007L = v241_surface_collocation_pts.reshape((2, 20, 3))

# op _007Q reshape_eval
# LANG: _007n --> _007R
# SHAPES: (2, 1, 10, 3) --> (2, 10, 3)
# full namespace: WakeSubAicBiotSavarts
v264__007R = v248__007n.reshape((2, 10, 3))

# op _007q reshape_eval
# LANG: surface_collocation_pts --> _007r
# SHAPES: (2, 2, 10, 3) --> (2, 20, 3)
# full namespace: WakeSubAicBiotSavarts
v251__007r = v241_surface_collocation_pts.reshape((2, 20, 3))

# op _007w reshape_eval
# LANG: _007m --> _007x
# SHAPES: (2, 1, 10, 3) --> (2, 10, 3)
# full namespace: WakeSubAicBiotSavarts
v254__007x = v247__007m.reshape((2, 10, 3))

# op _007M expand_array_eval
# LANG: _007L --> _007N
# SHAPES: (2, 20, 3) --> (2, 20, 10, 3)
# full namespace: WakeSubAicBiotSavarts
v262__007N = np.einsum('abd,c->abcd', v261__007L.reshape((2, 20, 3)) ,np.ones((10,))).reshape((2, 20, 10, 3))

# op _007S expand_array_eval
# LANG: _007R --> _007T
# SHAPES: (2, 10, 3) --> (2, 20, 10, 3)
# full namespace: WakeSubAicBiotSavarts
v265__007T = np.einsum('acd,b->abcd', v264__007R.reshape((2, 10, 3)) ,np.ones((20,))).reshape((2, 20, 10, 3))

# op _007s expand_array_eval
# LANG: _007r --> _007t
# SHAPES: (2, 20, 3) --> (2, 20, 10, 3)
# full namespace: WakeSubAicBiotSavarts
v252__007t = np.einsum('abd,c->abcd', v251__007r.reshape((2, 20, 3)) ,np.ones((10,))).reshape((2, 20, 10, 3))

# op _007y expand_array_eval
# LANG: _007x --> _007z
# SHAPES: (2, 10, 3) --> (2, 20, 10, 3)
# full namespace: WakeSubAicBiotSavarts
v255__007z = np.einsum('acd,b->abcd', v254__007x.reshape((2, 10, 3)) ,np.ones((20,))).reshape((2, 20, 10, 3))

# op _0083 reshape_eval
# LANG: surface_collocation_pts --> _0084
# SHAPES: (2, 2, 10, 3) --> (2, 20, 3)
# full namespace: WakeSubAicBiotSavarts
v271__0084 = v241_surface_collocation_pts.reshape((2, 20, 3))

# op _0089 reshape_eval
# LANG: _007o --> _008a
# SHAPES: (2, 1, 10, 3) --> (2, 10, 3)
# full namespace: WakeSubAicBiotSavarts
v274__008a = v249__007o.reshape((2, 10, 3))

# op _007A reshape_eval
# LANG: _007z --> _007B
# SHAPES: (2, 20, 10, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v256__007B = v255__007z.reshape((2, 200, 3))

# op _007O reshape_eval
# LANG: _007N --> _007P
# SHAPES: (2, 20, 10, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v263__007P = v262__007N.reshape((2, 200, 3))

# op _007U reshape_eval
# LANG: _007T --> _007V
# SHAPES: (2, 20, 10, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v266__007V = v265__007T.reshape((2, 200, 3))

# op _007u reshape_eval
# LANG: _007t --> _007v
# SHAPES: (2, 20, 10, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v253__007v = v252__007t.reshape((2, 200, 3))

# op _0085 expand_array_eval
# LANG: _0084 --> _0086
# SHAPES: (2, 20, 3) --> (2, 20, 10, 3)
# full namespace: WakeSubAicBiotSavarts
v272__0086 = np.einsum('abd,c->abcd', v271__0084.reshape((2, 20, 3)) ,np.ones((10,))).reshape((2, 20, 10, 3))

# op _008b expand_array_eval
# LANG: _008a --> _008c
# SHAPES: (2, 10, 3) --> (2, 20, 10, 3)
# full namespace: WakeSubAicBiotSavarts
v275__008c = np.einsum('acd,b->abcd', v274__008a.reshape((2, 10, 3)) ,np.ones((20,))).reshape((2, 20, 10, 3))

# op _008n reshape_eval
# LANG: surface_collocation_pts --> _008o
# SHAPES: (2, 2, 10, 3) --> (2, 20, 3)
# full namespace: WakeSubAicBiotSavarts
v281__008o = v241_surface_collocation_pts.reshape((2, 20, 3))

# op _008t reshape_eval
# LANG: _007p --> _008u
# SHAPES: (2, 1, 10, 3) --> (2, 10, 3)
# full namespace: WakeSubAicBiotSavarts
v284__008u = v250__007p.reshape((2, 10, 3))

# op _007C_linear_combination_eval
# LANG: _007v, _007B --> _007D
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v257__007D = v253__007v+-1*v256__007B

# op _007W_linear_combination_eval
# LANG: _007P, _007V --> _007X
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v267__007X = v263__007P+-1*v266__007V

# op _0087 reshape_eval
# LANG: _0086 --> _0088
# SHAPES: (2, 20, 10, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v273__0088 = v272__0086.reshape((2, 200, 3))

# op _008d reshape_eval
# LANG: _008c --> _008e
# SHAPES: (2, 20, 10, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v276__008e = v275__008c.reshape((2, 200, 3))

# op _008p expand_array_eval
# LANG: _008o --> _008q
# SHAPES: (2, 20, 3) --> (2, 20, 10, 3)
# full namespace: WakeSubAicBiotSavarts
v282__008q = np.einsum('abd,c->abcd', v281__008o.reshape((2, 20, 3)) ,np.ones((10,))).reshape((2, 20, 10, 3))

# op _008v expand_array_eval
# LANG: _008u --> _008w
# SHAPES: (2, 10, 3) --> (2, 20, 10, 3)
# full namespace: WakeSubAicBiotSavarts
v285__008w = np.einsum('acd,b->abcd', v284__008u.reshape((2, 10, 3)) ,np.ones((20,))).reshape((2, 20, 10, 3))

# op _007E_power_combination_eval
# LANG: _007D --> _007F
# SHAPES: (2, 200, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v258__007F = (v257__007D**2)
v258__007F = v258__007F.reshape((2, 200, 3))

# op _007Y_power_combination_eval
# LANG: _007X --> _007Z
# SHAPES: (2, 200, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v268__007Z = (v267__007X**2)
v268__007Z = v268__007Z.reshape((2, 200, 3))

# op _008f_linear_combination_eval
# LANG: _0088, _008e --> _008g
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v277__008g = v273__0088+-1*v276__008e

# op _008r reshape_eval
# LANG: _008q --> _008s
# SHAPES: (2, 20, 10, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v283__008s = v282__008q.reshape((2, 200, 3))

# op _008x reshape_eval
# LANG: _008w --> _008y
# SHAPES: (2, 20, 10, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v286__008y = v285__008w.reshape((2, 200, 3))

# op _007G_single_tensor_sum_with_axis_eval
# LANG: _007F --> _007H
# SHAPES: (2, 200, 3) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v259__007H = np.sum(v258__007F, axis = (2,)).reshape((2, 200))

# op _007__single_tensor_sum_with_axis_eval
# LANG: _007Z --> _0080
# SHAPES: (2, 200, 3) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v269__0080 = np.sum(v268__007Z, axis = (2,)).reshape((2, 200))

# op _008h_power_combination_eval
# LANG: _008g --> _008i
# SHAPES: (2, 200, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v278__008i = (v277__008g**2)
v278__008i = v278__008i.reshape((2, 200, 3))

# op _008z_linear_combination_eval
# LANG: _008s, _008y --> _008A
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v287__008A = v283__008s+-1*v286__008y

# op _007I_power_combination_eval
# LANG: _007H --> _007J
# SHAPES: (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v260__007J = (v259__007H**0.5)
v260__007J = v260__007J.reshape((2, 200))

# op _0081_power_combination_eval
# LANG: _0080 --> _0082
# SHAPES: (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v270__0082 = (v269__0080**0.5)
v270__0082 = v270__0082.reshape((2, 200))

# op _008B_power_combination_eval
# LANG: _008A --> _008C
# SHAPES: (2, 200, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v288__008C = (v287__008A**2)
v288__008C = v288__008C.reshape((2, 200, 3))

# op _008L_power_combination_eval
# LANG: _007D, _007X --> _008M
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v293__008M = (v257__007D)*(v267__007X)
v293__008M = v293__008M.reshape((2, 200, 3))

# op _008j_single_tensor_sum_with_axis_eval
# LANG: _008i --> _008k
# SHAPES: (2, 200, 3) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v279__008k = np.sum(v278__008i, axis = (2,)).reshape((2, 200))

# op _008D_single_tensor_sum_with_axis_eval
# LANG: _008C --> _008E
# SHAPES: (2, 200, 3) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v289__008E = np.sum(v288__008C, axis = (2,)).reshape((2, 200))

# op _008N_single_tensor_sum_with_axis_eval
# LANG: _008M --> _008O
# SHAPES: (2, 200, 3) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v294__008O = np.sum(v293__008M, axis = (2,)).reshape((2, 200))

# op _008P_power_combination_eval
# LANG: _007J, _0082 --> _008Q
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v295__008Q = (v260__007J)*(v270__0082)
v295__008Q = v295__008Q.reshape((2, 200))

# op _008l_power_combination_eval
# LANG: _008k --> _008m
# SHAPES: (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v280__008m = (v279__008k**0.5)
v280__008m = v280__008m.reshape((2, 200))

# op _009a_power_combination_eval
# LANG: _008g, _007X --> _009b
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v306__009b = (v267__007X)*(v277__008g)
v306__009b = v306__009b.reshape((2, 200, 3))

# op _00aw_decompose_eval
# LANG: surface_wake_coords --> _00aC, _00ax, _00ay, _00aB
# SHAPES: (2, 2, 11, 3) --> (2, 1, 10, 3), (2, 1, 10, 3), (2, 1, 10, 3), (2, 1, 10, 3)
# full namespace: ComputeNormalsWake
v349__00ax = ((v348_surface_wake_coords.flatten())[src_indices__00ax__00aw]).reshape((2, 1, 10, 3))
v350__00ay = ((v348_surface_wake_coords.flatten())[src_indices__00ay__00aw]).reshape((2, 1, 10, 3))
v352__00aB = ((v348_surface_wake_coords.flatten())[src_indices__00aB__00aw]).reshape((2, 1, 10, 3))
v353__00aC = ((v348_surface_wake_coords.flatten())[src_indices__00aC__00aw]).reshape((2, 1, 10, 3))

# op _008F_power_combination_eval
# LANG: _008E --> _008G
# SHAPES: (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v290__008G = (v289__008E**0.5)
v290__008G = v290__008G.reshape((2, 200))

# op _008R_linear_combination_eval
# LANG: _008Q, _008O --> _008S
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v296__008S = v295__008Q+v294__008O

# op _008V_power_combination_eval
# LANG: _007J --> _008W
# SHAPES: (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v298__008W = (v260__007J**-1)
v298__008W = v298__008W.reshape((2, 200))

# op _008X_power_combination_eval
# LANG: _0082 --> _008Y
# SHAPES: (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v299__008Y = (v270__0082**-1)
v299__008Y = v299__008Y.reshape((2, 200))

# op _009A_power_combination_eval
# LANG: _008A, _008g --> _009B
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v319__009B = (v277__008g)*(v287__008A)
v319__009B = v319__009B.reshape((2, 200, 3))

# op _009c_single_tensor_sum_with_axis_eval
# LANG: _009b --> _009d
# SHAPES: (2, 200, 3) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v307__009d = np.sum(v306__009b, axis = (2,)).reshape((2, 200))

# op _009e_power_combination_eval
# LANG: _008m, _0082 --> _009f
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v308__009f = (v270__0082)*(v280__008m)
v308__009f = v308__009f.reshape((2, 200))

# op _00aD_linear_combination_eval
# LANG: _00aB, _00aC --> _00aE
# SHAPES: (2, 1, 10, 3), (2, 1, 10, 3) --> (2, 1, 10, 3)
# full namespace: ComputeNormalsWake
v354__00aE = v352__00aB+-1*v353__00aC

# op _00az_linear_combination_eval
# LANG: _00ax, _00ay --> _00aA
# SHAPES: (2, 1, 10, 3), (2, 1, 10, 3) --> (2, 1, 10, 3)
# full namespace: ComputeNormalsWake
v351__00aA = v349__00ax+-1*v350__00ay

# op _008T_power_combination_eval
# LANG: _008S --> _008U
# SHAPES: (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v297__008U = (v296__008S**-1)
v297__008U = v297__008U.reshape((2, 200))

# op _008Z_linear_combination_eval
# LANG: _008W, _008Y --> _008_
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v300__008_ = v298__008W+v299__008Y

# op _009C_single_tensor_sum_with_axis_eval
# LANG: _009B --> _009D
# SHAPES: (2, 200, 3) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v320__009D = np.sum(v319__009B, axis = (2,)).reshape((2, 200))

# op _009E_power_combination_eval
# LANG: _008G, _008m --> _009F
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v321__009F = (v280__008m)*(v290__008G)
v321__009F = v321__009F.reshape((2, 200))

# op _009__power_combination_eval
# LANG: _008A, _007D --> _00a0
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v332__00a0 = (v287__008A)*(v257__007D)
v332__00a0 = v332__00a0.reshape((2, 200, 3))

# op _009g_linear_combination_eval
# LANG: _009f, _009d --> _009h
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v309__009h = v308__009f+v307__009d

# op _009k_power_combination_eval
# LANG: _0082 --> _009l
# SHAPES: (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v311__009l = (v270__0082**-1)
v311__009l = v311__009l.reshape((2, 200))

# op _009m_power_combination_eval
# LANG: _008m --> _009n
# SHAPES: (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v312__009n = (v280__008m**-1)
v312__009n = v312__009n.reshape((2, 200))

# op _00aF cross_product_eval
# LANG: _00aA, _00aE --> _00aG
# SHAPES: (2, 1, 10, 3), (2, 1, 10, 3) --> (2, 1, 10, 3)
# full namespace: ComputeNormalsWake
v355__00aG = np.cross(v351__00aA, v354__00aE, axisa = 3, axisb = 3, axisc = 3)

# op _003b_decompose_eval
# LANG: surface_bound_vtx_coords --> _003c, _003d, _003e, _003f
# SHAPES: (2, 3, 11, 3) --> (2, 2, 10, 3), (2, 2, 10, 3), (2, 2, 10, 3), (2, 2, 10, 3)
# full namespace: SubAicBiotSavarts
v111__003c = ((v232_surface_bound_vtx_coords.flatten())[src_indices__003c__003b]).reshape((2, 2, 10, 3))
v112__003d = ((v232_surface_bound_vtx_coords.flatten())[src_indices__003d__003b]).reshape((2, 2, 10, 3))
v113__003e = ((v232_surface_bound_vtx_coords.flatten())[src_indices__003e__003b]).reshape((2, 2, 10, 3))
v114__003f = ((v232_surface_bound_vtx_coords.flatten())[src_indices__003f__003b]).reshape((2, 2, 10, 3))

# op _008H cross_product_eval
# LANG: _007D, _007X --> _008I
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v291__008I = np.cross(v257__007D, v267__007X, axisa = 2, axisb = 2, axisc = 2)

# op _0090_power_combination_eval
# LANG: _008U, _008_ --> _0091
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v301__0091 = (v297__008U)*(v300__008_)
v301__0091 = v301__0091.reshape((2, 200))

# op _009G_linear_combination_eval
# LANG: _009F, _009D --> _009H
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v322__009H = v321__009F+v320__009D

# op _009K_power_combination_eval
# LANG: _008m --> _009L
# SHAPES: (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v324__009L = (v280__008m**-1)
v324__009L = v324__009L.reshape((2, 200))

# op _009M_power_combination_eval
# LANG: _008G --> _009N
# SHAPES: (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v325__009N = (v290__008G**-1)
v325__009N = v325__009N.reshape((2, 200))

# op _009i_power_combination_eval
# LANG: _009h --> _009j
# SHAPES: (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v310__009j = (v309__009h**-1)
v310__009j = v310__009j.reshape((2, 200))

# op _009o_linear_combination_eval
# LANG: _009l, _009n --> _009p
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v313__009p = v311__009l+v312__009n

# op _00a1_single_tensor_sum_with_axis_eval
# LANG: _00a0 --> _00a2
# SHAPES: (2, 200, 3) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v333__00a2 = np.sum(v332__00a0, axis = (2,)).reshape((2, 200))

# op _00a3_power_combination_eval
# LANG: _007J, _008G --> _00a4
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v334__00a4 = (v290__008G)*(v260__007J)
v334__00a4 = v334__00a4.reshape((2, 200))

# op _00aH_power_combination_eval
# LANG: _00aG --> _00aI
# SHAPES: (2, 1, 10, 3) --> (2, 1, 10, 3)
# full namespace: ComputeNormalsWake
v356__00aI = (v355__00aG**2)
v356__00aI = v356__00aI.reshape((2, 1, 10, 3))

# op _003A reshape_eval
# LANG: surface_collocation_pts --> _003B
# SHAPES: (2, 2, 10, 3) --> (2, 20, 3)
# full namespace: SubAicBiotSavarts
v125__003B = v241_surface_collocation_pts.reshape((2, 20, 3))

# op _003G reshape_eval
# LANG: _003d --> _003H
# SHAPES: (2, 2, 10, 3) --> (2, 20, 3)
# full namespace: SubAicBiotSavarts
v128__003H = v112__003d.reshape((2, 20, 3))

# op _003g reshape_eval
# LANG: surface_collocation_pts --> _003h
# SHAPES: (2, 2, 10, 3) --> (2, 20, 3)
# full namespace: SubAicBiotSavarts
v115__003h = v241_surface_collocation_pts.reshape((2, 20, 3))

# op _003m reshape_eval
# LANG: _003c --> _003n
# SHAPES: (2, 2, 10, 3) --> (2, 20, 3)
# full namespace: SubAicBiotSavarts
v118__003n = v111__003c.reshape((2, 20, 3))

# op _008J_power_combination_eval
# LANG: _008I --> _008K
# SHAPES: (2, 200, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v292__008K = (v291__008I)
v292__008K = (v292__008K*_008J_coeff).reshape((2, 200, 3))

# op _0092 expand_array_eval
# LANG: _0091 --> _0093
# SHAPES: (2, 200) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v302__0093 = np.einsum('ab,c->abc', v301__0091.reshape((2, 200)) ,np.ones((3,))).reshape((2, 200, 3))

# op _0096 cross_product_eval
# LANG: _008g, _007X --> _0097
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v304__0097 = np.cross(v267__007X, v277__008g, axisa = 2, axisb = 2, axisc = 2)

# op _009I_power_combination_eval
# LANG: _009H --> _009J
# SHAPES: (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v323__009J = (v322__009H**-1)
v323__009J = v323__009J.reshape((2, 200))

# op _009O_linear_combination_eval
# LANG: _009L, _009N --> _009P
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v326__009P = v324__009L+v325__009N

# op _009q_power_combination_eval
# LANG: _009j, _009p --> _009r
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v314__009r = (v310__009j)*(v313__009p)
v314__009r = v314__009r.reshape((2, 200))

# op _00a5_linear_combination_eval
# LANG: _00a4, _00a2 --> _00a6
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v335__00a6 = v334__00a4+v333__00a2

# op _00a9_power_combination_eval
# LANG: _008G --> _00aa
# SHAPES: (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v337__00aa = (v290__008G**-1)
v337__00aa = v337__00aa.reshape((2, 200))

# op _00aJ_single_tensor_sum_with_axis_eval
# LANG: _00aI --> _00aK
# SHAPES: (2, 1, 10, 3) --> (2, 1, 10)
# full namespace: ComputeNormalsWake
v357__00aK = np.sum(v356__00aI, axis = (3,)).reshape((2, 1, 10))

# op _00ab_power_combination_eval
# LANG: _007J --> _00ac
# SHAPES: (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v338__00ac = (v260__007J**-1)
v338__00ac = v338__00ac.reshape((2, 200))

# op _003C expand_array_eval
# LANG: _003B --> _003D
# SHAPES: (2, 20, 3) --> (2, 20, 20, 3)
# full namespace: SubAicBiotSavarts
v126__003D = np.einsum('abd,c->abcd', v125__003B.reshape((2, 20, 3)) ,np.ones((20,))).reshape((2, 20, 20, 3))

# op _003I expand_array_eval
# LANG: _003H --> _003J
# SHAPES: (2, 20, 3) --> (2, 20, 20, 3)
# full namespace: SubAicBiotSavarts
v129__003J = np.einsum('acd,b->abcd', v128__003H.reshape((2, 20, 3)) ,np.ones((20,))).reshape((2, 20, 20, 3))

# op _003U reshape_eval
# LANG: surface_collocation_pts --> _003V
# SHAPES: (2, 2, 10, 3) --> (2, 20, 3)
# full namespace: SubAicBiotSavarts
v135__003V = v241_surface_collocation_pts.reshape((2, 20, 3))

# op _003_ reshape_eval
# LANG: _003e --> _0040
# SHAPES: (2, 2, 10, 3) --> (2, 20, 3)
# full namespace: SubAicBiotSavarts
v138__0040 = v113__003e.reshape((2, 20, 3))

# op _003i expand_array_eval
# LANG: _003h --> _003j
# SHAPES: (2, 20, 3) --> (2, 20, 20, 3)
# full namespace: SubAicBiotSavarts
v116__003j = np.einsum('abd,c->abcd', v115__003h.reshape((2, 20, 3)) ,np.ones((20,))).reshape((2, 20, 20, 3))

# op _003o expand_array_eval
# LANG: _003n --> _003p
# SHAPES: (2, 20, 3) --> (2, 20, 20, 3)
# full namespace: SubAicBiotSavarts
v119__003p = np.einsum('acd,b->abcd', v118__003n.reshape((2, 20, 3)) ,np.ones((20,))).reshape((2, 20, 20, 3))

# op _0094_power_combination_eval
# LANG: _0093, _008K --> _0095
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v303__0095 = (v302__0093)*(v292__008K)
v303__0095 = v303__0095.reshape((2, 200, 3))

# op _0098_power_combination_eval
# LANG: _0097 --> _0099
# SHAPES: (2, 200, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v305__0099 = (v304__0097)
v305__0099 = (v305__0099*_0098_coeff).reshape((2, 200, 3))

# op _009Q_power_combination_eval
# LANG: _009J, _009P --> _009R
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v327__009R = (v323__009J)*(v326__009P)
v327__009R = v327__009R.reshape((2, 200))

# op _009s expand_array_eval
# LANG: _009r --> _009t
# SHAPES: (2, 200) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v315__009t = np.einsum('ab,c->abc', v314__009r.reshape((2, 200)) ,np.ones((3,))).reshape((2, 200, 3))

# op _009w cross_product_eval
# LANG: _008A, _008g --> _009x
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v317__009x = np.cross(v277__008g, v287__008A, axisa = 2, axisb = 2, axisc = 2)

# op _00a7_power_combination_eval
# LANG: _00a6 --> _00a8
# SHAPES: (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v336__00a8 = (v335__00a6**-1)
v336__00a8 = v336__00a8.reshape((2, 200))

# op _00aL_power_combination_eval
# LANG: _00aK --> _00aM
# SHAPES: (2, 1, 10) --> (2, 1, 10)
# full namespace: ComputeNormalsWake
v358__00aM = (v357__00aK**0.5)
v358__00aM = v358__00aM.reshape((2, 1, 10))

# op _00ad_linear_combination_eval
# LANG: _00aa, _00ac --> _00ae
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v339__00ae = v337__00aa+v338__00ac

# op _003E reshape_eval
# LANG: _003D --> _003F
# SHAPES: (2, 20, 20, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v127__003F = v126__003D.reshape((2, 400, 3))

# op _003K reshape_eval
# LANG: _003J --> _003L
# SHAPES: (2, 20, 20, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v130__003L = v129__003J.reshape((2, 400, 3))

# op _003W expand_array_eval
# LANG: _003V --> _003X
# SHAPES: (2, 20, 3) --> (2, 20, 20, 3)
# full namespace: SubAicBiotSavarts
v136__003X = np.einsum('abd,c->abcd', v135__003V.reshape((2, 20, 3)) ,np.ones((20,))).reshape((2, 20, 20, 3))

# op _003k reshape_eval
# LANG: _003j --> _003l
# SHAPES: (2, 20, 20, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v117__003l = v116__003j.reshape((2, 400, 3))

# op _003q reshape_eval
# LANG: _003p --> _003r
# SHAPES: (2, 20, 20, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v120__003r = v119__003p.reshape((2, 400, 3))

# op _0041 expand_array_eval
# LANG: _0040 --> _0042
# SHAPES: (2, 20, 3) --> (2, 20, 20, 3)
# full namespace: SubAicBiotSavarts
v139__0042 = np.einsum('acd,b->abcd', v138__0040.reshape((2, 20, 3)) ,np.ones((20,))).reshape((2, 20, 20, 3))

# op _004d reshape_eval
# LANG: surface_collocation_pts --> _004e
# SHAPES: (2, 2, 10, 3) --> (2, 20, 3)
# full namespace: SubAicBiotSavarts
v145__004e = v241_surface_collocation_pts.reshape((2, 20, 3))

# op _004j reshape_eval
# LANG: _003f --> _004k
# SHAPES: (2, 2, 10, 3) --> (2, 20, 3)
# full namespace: SubAicBiotSavarts
v148__004k = v114__003f.reshape((2, 20, 3))

# op _009S expand_array_eval
# LANG: _009R --> _009T
# SHAPES: (2, 200) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v328__009T = np.einsum('ab,c->abc', v327__009R.reshape((2, 200)) ,np.ones((3,))).reshape((2, 200, 3))

# op _009W cross_product_eval
# LANG: _008A, _007D --> _009X
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v330__009X = np.cross(v287__008A, v257__007D, axisa = 2, axisb = 2, axisc = 2)

# op _009u_power_combination_eval
# LANG: _009t, _0099 --> _009v
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v316__009v = (v315__009t)*(v305__0099)
v316__009v = v316__009v.reshape((2, 200, 3))

# op _009y_power_combination_eval
# LANG: _009x --> _009z
# SHAPES: (2, 200, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v318__009z = (v317__009x)
v318__009z = (v318__009z*_009y_coeff).reshape((2, 200, 3))

# op _00aN expand_array_eval
# LANG: _00aM --> _00aO
# SHAPES: (2, 1, 10) --> (2, 1, 10, 3)
# full namespace: ComputeNormalsWake
v359__00aO = np.einsum('abc,d->abcd', v358__00aM.reshape((2, 1, 10)) ,np.ones((3,))).reshape((2, 1, 10, 3))

# op _00af_power_combination_eval
# LANG: _00a8, _00ae --> _00ag
# SHAPES: (2, 200), (2, 200) --> (2, 200)
# full namespace: WakeSubAicBiotSavarts
v340__00ag = (v336__00a8)*(v339__00ae)
v340__00ag = v340__00ag.reshape((2, 200))

# op _00al_linear_combination_eval
# LANG: _0095 --> _00am
# SHAPES: (2, 200, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v343__00am = v303__0095

# op _003M_linear_combination_eval
# LANG: _003F, _003L --> _003N
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v131__003N = v127__003F+-1*v130__003L

# op _003Y reshape_eval
# LANG: _003X --> _003Z
# SHAPES: (2, 20, 20, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v137__003Z = v136__003X.reshape((2, 400, 3))

# op _003s_linear_combination_eval
# LANG: _003l, _003r --> _003t
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v121__003t = v117__003l+-1*v120__003r

# op _0043 reshape_eval
# LANG: _0042 --> _0044
# SHAPES: (2, 20, 20, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v140__0044 = v139__0042.reshape((2, 400, 3))

# op _004f expand_array_eval
# LANG: _004e --> _004g
# SHAPES: (2, 20, 3) --> (2, 20, 20, 3)
# full namespace: SubAicBiotSavarts
v146__004g = np.einsum('abd,c->abcd', v145__004e.reshape((2, 20, 3)) ,np.ones((20,))).reshape((2, 20, 20, 3))

# op _004l expand_array_eval
# LANG: _004k --> _004m
# SHAPES: (2, 20, 3) --> (2, 20, 20, 3)
# full namespace: SubAicBiotSavarts
v149__004m = np.einsum('acd,b->abcd', v148__004k.reshape((2, 20, 3)) ,np.ones((20,))).reshape((2, 20, 20, 3))

# op _009U_power_combination_eval
# LANG: _009T, _009z --> _009V
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v329__009V = (v328__009T)*(v318__009z)
v329__009V = v329__009V.reshape((2, 200, 3))

# op _009Y_power_combination_eval
# LANG: _009X --> _009Z
# SHAPES: (2, 200, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v331__009Z = (v330__009X)
v331__009Z = (v331__009Z*_009Y_coeff).reshape((2, 200, 3))

# op _00aP_power_combination_eval
# LANG: _00aG, _00aO --> surface_wake_coords_normals
# SHAPES: (2, 1, 10, 3), (2, 1, 10, 3) --> (2, 1, 10, 3)
# full namespace: ComputeNormalsWake
v362_surface_wake_coords_normals = (v355__00aG)*(v359__00aO**-1)
v362_surface_wake_coords_normals = v362_surface_wake_coords_normals.reshape((2, 1, 10, 3))

# op _00ah expand_array_eval
# LANG: _00ag --> _00ai
# SHAPES: (2, 200) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v341__00ai = np.einsum('ab,c->abc', v340__00ag.reshape((2, 200)) ,np.ones((3,))).reshape((2, 200, 3))

# op _00an_linear_combination_eval
# LANG: _00am, _009v --> _00ao
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v344__00ao = v343__00am+v316__009v

# op _003O_power_combination_eval
# LANG: _003N --> _003P
# SHAPES: (2, 400, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v132__003P = (v131__003N**2)
v132__003P = v132__003P.reshape((2, 400, 3))

# op _003u_power_combination_eval
# LANG: _003t --> _003v
# SHAPES: (2, 400, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v122__003v = (v121__003t**2)
v122__003v = v122__003v.reshape((2, 400, 3))

# op _0045_linear_combination_eval
# LANG: _003Z, _0044 --> _0046
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v141__0046 = v137__003Z+-1*v140__0044

# op _004h reshape_eval
# LANG: _004g --> _004i
# SHAPES: (2, 20, 20, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v147__004i = v146__004g.reshape((2, 400, 3))

# op _004n reshape_eval
# LANG: _004m --> _004o
# SHAPES: (2, 20, 20, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v150__004o = v149__004m.reshape((2, 400, 3))

# op _00aT reshape_eval
# LANG: surface_wake_coords_normals --> _00aU
# SHAPES: (2, 1, 10, 3) --> (2, 10, 3)
# full namespace: ProjectionWake
v363__00aU = v362_surface_wake_coords_normals.reshape((2, 10, 3))

# op _00aj_power_combination_eval
# LANG: _00ai, _009Z --> _00ak
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v342__00ak = (v341__00ai)*(v331__009Z)
v342__00ak = v342__00ak.reshape((2, 200, 3))

# op _00ap_linear_combination_eval
# LANG: _00ao, _009V --> _00aq
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v345__00aq = v344__00ao+v329__009V

# op _003Q_single_tensor_sum_with_axis_eval
# LANG: _003P --> _003R
# SHAPES: (2, 400, 3) --> (2, 400)
# full namespace: SubAicBiotSavarts
v133__003R = np.sum(v132__003P, axis = (2,)).reshape((2, 400))

# op _003w_single_tensor_sum_with_axis_eval
# LANG: _003v --> _003x
# SHAPES: (2, 400, 3) --> (2, 400)
# full namespace: SubAicBiotSavarts
v123__003x = np.sum(v122__003v, axis = (2,)).reshape((2, 400))

# op _0047_power_combination_eval
# LANG: _0046 --> _0048
# SHAPES: (2, 400, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v142__0048 = (v141__0046**2)
v142__0048 = v142__0048.reshape((2, 400, 3))

# op _004p_linear_combination_eval
# LANG: _004i, _004o --> _004q
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v151__004q = v147__004i+-1*v150__004o

# op _00aV_indexed_passthrough_eval
# LANG: _00aU --> normal_concatenated_wake_rhs
# SHAPES: (2, 10, 3) --> (2, 10, 3)
# full namespace: ProjectionWake
v361_normal_concatenated_wake_rhs__temp[i_v363__00aU__00aV_indexed_passthrough_eval] = v363__00aU.flatten()
v361_normal_concatenated_wake_rhs = v361_normal_concatenated_wake_rhs__temp.copy()

# op _00ar_linear_combination_eval
# LANG: _00aq, _00ak --> _00as
# SHAPES: (2, 200, 3), (2, 200, 3) --> (2, 200, 3)
# full namespace: WakeSubAicBiotSavarts
v346__00as = v345__00aq+v342__00ak

# op _003S_power_combination_eval
# LANG: _003R --> _003T
# SHAPES: (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v134__003T = (v133__003R**0.5)
v134__003T = v134__003T.reshape((2, 400))

# op _003y_power_combination_eval
# LANG: _003x --> _003z
# SHAPES: (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v124__003z = (v123__003x**0.5)
v124__003z = v124__003z.reshape((2, 400))

# op _0049_single_tensor_sum_with_axis_eval
# LANG: _0048 --> _004a
# SHAPES: (2, 400, 3) --> (2, 400)
# full namespace: SubAicBiotSavarts
v143__004a = np.sum(v142__0048, axis = (2,)).reshape((2, 400))

# op _004B_power_combination_eval
# LANG: _003t, _003N --> _004C
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v157__004C = (v121__003t)*(v131__003N)
v157__004C = v157__004C.reshape((2, 400, 3))

# op _004r_power_combination_eval
# LANG: _004q --> _004s
# SHAPES: (2, 400, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v152__004s = (v151__004q**2)
v152__004s = v152__004s.reshape((2, 400, 3))

# op _00aX expand_array_eval
# LANG: normal_concatenated_wake_rhs --> _00aY
# SHAPES: (2, 10, 3) --> (2, 20, 10, 3)
# full namespace: ProjectionWake
v365__00aY = np.einsum('acd,b->abcd', v361_normal_concatenated_wake_rhs.reshape((2, 10, 3)) ,np.ones((20,))).reshape((2, 20, 10, 3))

# op _00at reshape_eval
# LANG: _00as --> wake_aic
# SHAPES: (2, 200, 3) --> (2, 20, 10, 3)
# full namespace: WakeSubAicBiotSavarts
v364_wake_aic = v346__00as.reshape((2, 20, 10, 3))

# op _004D_single_tensor_sum_with_axis_eval
# LANG: _004C --> _004E
# SHAPES: (2, 400, 3) --> (2, 400)
# full namespace: SubAicBiotSavarts
v158__004E = np.sum(v157__004C, axis = (2,)).reshape((2, 400))

# op _004F_power_combination_eval
# LANG: _003z, _003T --> _004G
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v159__004G = (v124__003z)*(v134__003T)
v159__004G = v159__004G.reshape((2, 400))

# op _004b_power_combination_eval
# LANG: _004a --> _004c
# SHAPES: (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v144__004c = (v143__004a**0.5)
v144__004c = v144__004c.reshape((2, 400))

# op _004t_single_tensor_sum_with_axis_eval
# LANG: _004s --> _004u
# SHAPES: (2, 400, 3) --> (2, 400)
# full namespace: SubAicBiotSavarts
v153__004u = np.sum(v152__004s, axis = (2,)).reshape((2, 400))

# op _0056_power_combination_eval
# LANG: _0046, _003N --> _0057
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v173__0057 = (v131__003N)*(v141__0046)
v173__0057 = v173__0057.reshape((2, 400, 3))

# op _00aZ_power_combination_eval
# LANG: _00aY, wake_aic --> _00a_
# SHAPES: (2, 20, 10, 3), (2, 20, 10, 3) --> (2, 20, 10, 3)
# full namespace: ProjectionWake
v366__00a_ = (v364_wake_aic)*(v365__00aY)
v366__00a_ = v366__00a_.reshape((2, 20, 10, 3))

# op _001p_decompose_eval
# LANG: surface --> _001v, _001q, _001r, _001u
# SHAPES: (2, 3, 11, 3) --> (2, 2, 10, 3), (2, 2, 10, 3), (2, 2, 10, 3), (2, 2, 10, 3)
# full namespace: ComputeNormals
v46__001q = ((v77_surface.flatten())[src_indices__001q__001p]).reshape((2, 2, 10, 3))
v47__001r = ((v77_surface.flatten())[src_indices__001r__001p]).reshape((2, 2, 10, 3))
v49__001u = ((v77_surface.flatten())[src_indices__001u__001p]).reshape((2, 2, 10, 3))
v50__001v = ((v77_surface.flatten())[src_indices__001v__001p]).reshape((2, 2, 10, 3))

# op _004H_linear_combination_eval
# LANG: _004G, _004E --> _004I
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v160__004I = v159__004G+v158__004E

# op _004N_linear_combination_eval
# LANG: _003z --> _004O
# SHAPES: (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v163__004O = _004N_constant+v124__003z

# op _004R_linear_combination_eval
# LANG: _003T --> _004S
# SHAPES: (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v165__004S = _004R_constant+v134__003T

# op _004v_power_combination_eval
# LANG: _004u --> _004w
# SHAPES: (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v154__004w = (v153__004u**0.5)
v154__004w = v154__004w.reshape((2, 400))

# op _0058_single_tensor_sum_with_axis_eval
# LANG: _0057 --> _0059
# SHAPES: (2, 400, 3) --> (2, 400)
# full namespace: SubAicBiotSavarts
v174__0059 = np.sum(v173__0057, axis = (2,)).reshape((2, 400))

# op _005C_power_combination_eval
# LANG: _004q, _0046 --> _005D
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v189__005D = (v141__0046)*(v151__004q)
v189__005D = v189__005D.reshape((2, 400, 3))

# op _005a_power_combination_eval
# LANG: _004c, _003T --> _005b
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v175__005b = (v134__003T)*(v144__004c)
v175__005b = v175__005b.reshape((2, 400))

# op _00b0_single_tensor_sum_with_axis_eval
# LANG: _00a_ --> wake_rhs
# SHAPES: (2, 20, 10, 3) --> (2, 20, 10)
# full namespace: ProjectionWake
v367_wake_rhs = np.sum(v366__00a_, axis = (3,)).reshape((2, 20, 10))

# op _000i_power_combination_eval
# LANG: wake_rhs --> M_mat
# SHAPES: (2, 20, 10) --> (2, 20, 10)
# full namespace: 
v6_M_mat = (v367_wake_rhs)
v6_M_mat = v6_M_mat.reshape((2, 20, 10))

# op _001s_linear_combination_eval
# LANG: _001q, _001r --> _001t
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: ComputeNormals
v48__001t = v46__001q+-1*v47__001r

# op _001w_linear_combination_eval
# LANG: _001u, _001v --> _001x
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: ComputeNormals
v51__001x = v49__001u+-1*v50__001v

# op _004J_linear_combination_eval
# LANG: _004I --> _004K
# SHAPES: (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v161__004K = _004J_constant+v160__004I

# op _004P_power_combination_eval
# LANG: _004O --> _004Q
# SHAPES: (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v164__004Q = (v163__004O**-1)
v164__004Q = v164__004Q.reshape((2, 400))

# op _004T_power_combination_eval
# LANG: _004S --> _004U
# SHAPES: (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v166__004U = (v165__004S**-1)
v166__004U = v166__004U.reshape((2, 400))

# op _005E_single_tensor_sum_with_axis_eval
# LANG: _005D --> _005F
# SHAPES: (2, 400, 3) --> (2, 400)
# full namespace: SubAicBiotSavarts
v190__005F = np.sum(v189__005D, axis = (2,)).reshape((2, 400))

# op _005G_power_combination_eval
# LANG: _004w, _004c --> _005H
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v191__005H = (v144__004c)*(v154__004w)
v191__005H = v191__005H.reshape((2, 400))

# op _005c_linear_combination_eval
# LANG: _005b, _0059 --> _005d
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v176__005d = v175__005b+v174__0059

# op _005i_linear_combination_eval
# LANG: _003T --> _005j
# SHAPES: (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v179__005j = _005i_constant+v134__003T

# op _005m_linear_combination_eval
# LANG: _004c --> _005n
# SHAPES: (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v181__005n = _005m_constant+v144__004c

# op _0067_power_combination_eval
# LANG: _004q, _003t --> _0068
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v205__0068 = (v151__004q)*(v121__003t)
v205__0068 = v205__0068.reshape((2, 400, 3))

# op _000k_custom_explicit_eval
# LANG: M_mat --> M_reshaped
# SHAPES: (2, 20, 10) --> (2, 20, 20)
# full namespace: 
temp = _000k_custom_explicit_func_M_reshaped.solve(v6_M_mat)
v7_M_reshaped = temp[0].copy()

# op _001y cross_product_eval
# LANG: _001t, _001x --> _001z
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: ComputeNormals
v52__001z = np.cross(v48__001t, v51__001x, axisa = 3, axisb = 3, axisc = 3)

# op _004L_power_combination_eval
# LANG: _004K --> _004M
# SHAPES: (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v162__004M = (v161__004K**-1)
v162__004M = v162__004M.reshape((2, 400))

# op _004V_linear_combination_eval
# LANG: _004Q, _004U --> _004W
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v167__004W = v164__004Q+v166__004U

# op _005I_linear_combination_eval
# LANG: _005H, _005F --> _005J
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v192__005J = v191__005H+v190__005F

# op _005O_linear_combination_eval
# LANG: _004c --> _005P
# SHAPES: (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v195__005P = _005O_constant+v144__004c

# op _005S_linear_combination_eval
# LANG: _004w --> _005T
# SHAPES: (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v197__005T = _005S_constant+v154__004w

# op _005e_linear_combination_eval
# LANG: _005d --> _005f
# SHAPES: (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v177__005f = _005e_constant+v176__005d

# op _005k_power_combination_eval
# LANG: _005j --> _005l
# SHAPES: (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v180__005l = (v179__005j**-1)
v180__005l = v180__005l.reshape((2, 400))

# op _005o_power_combination_eval
# LANG: _005n --> _005p
# SHAPES: (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v182__005p = (v181__005n**-1)
v182__005p = v182__005p.reshape((2, 400))

# op _0069_single_tensor_sum_with_axis_eval
# LANG: _0068 --> _006a
# SHAPES: (2, 400, 3) --> (2, 400)
# full namespace: SubAicBiotSavarts
v206__006a = np.sum(v205__0068, axis = (2,)).reshape((2, 400))

# op _006b_power_combination_eval
# LANG: _003z, _004w --> _006c
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v207__006c = (v154__004w)*(v124__003z)
v207__006c = v207__006c.reshape((2, 400))

# op _001A_power_combination_eval
# LANG: _001z --> _001B
# SHAPES: (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: ComputeNormals
v53__001B = (v52__001z**2)
v53__001B = v53__001B.reshape((2, 2, 10, 3))

# op _004X_power_combination_eval
# LANG: _004M, _004W --> num_004Y
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v168_num_004Y = (v162__004M)*(v167__004W)
v168_num_004Y = v168_num_004Y.reshape((2, 400))

# op _004x cross_product_eval
# LANG: _003t, _003N --> _004y
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v155__004y = np.cross(v121__003t, v131__003N, axisa = 2, axisb = 2, axisc = 2)

# op _005K_linear_combination_eval
# LANG: _005J --> _005L
# SHAPES: (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v193__005L = _005K_constant+v192__005J

# op _005Q_power_combination_eval
# LANG: _005P --> _005R
# SHAPES: (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v196__005R = (v195__005P**-1)
v196__005R = v196__005R.reshape((2, 400))

# op _005U_power_combination_eval
# LANG: _005T --> _005V
# SHAPES: (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v198__005V = (v197__005T**-1)
v198__005V = v198__005V.reshape((2, 400))

# op _005g_power_combination_eval
# LANG: _005f --> _005h
# SHAPES: (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v178__005h = (v177__005f**-1)
v178__005h = v178__005h.reshape((2, 400))

# op _005q_linear_combination_eval
# LANG: _005l, _005p --> _005r
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v183__005r = v180__005l+v182__005p

# op _006d_linear_combination_eval
# LANG: _006c, _006a --> _006e
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v208__006e = v207__006c+v206__006a

# op _006j_linear_combination_eval
# LANG: _004w --> _006k
# SHAPES: (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v211__006k = _006j_constant+v154__004w

# op _006n_linear_combination_eval
# LANG: _003z --> _006o
# SHAPES: (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v213__006o = _006n_constant+v124__003z

# op _001C_single_tensor_sum_with_axis_eval
# LANG: _001B --> _001D
# SHAPES: (2, 2, 10, 3) --> (2, 2, 10)
# full namespace: ComputeNormals
v54__001D = np.sum(v53__001B, axis = (3,)).reshape((2, 2, 10))

# op _004Z expand_array_eval
# LANG: num_004Y --> _004_
# SHAPES: (2, 400) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v169__004_ = np.einsum('ab,c->abc', v168_num_004Y.reshape((2, 400)) ,np.ones((3,))).reshape((2, 400, 3))

# op _004z_power_combination_eval
# LANG: _004y --> _004A
# SHAPES: (2, 400, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v156__004A = (v155__004y)
v156__004A = (v156__004A*_004z_coeff).reshape((2, 400, 3))

# op _0052 cross_product_eval
# LANG: _0046, _003N --> _0053
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v171__0053 = np.cross(v131__003N, v141__0046, axisa = 2, axisb = 2, axisc = 2)

# op _005M_power_combination_eval
# LANG: _005L --> _005N
# SHAPES: (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v194__005N = (v193__005L**-1)
v194__005N = v194__005N.reshape((2, 400))

# op _005W_linear_combination_eval
# LANG: _005R, _005V --> _005X
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v199__005X = v196__005R+v198__005V

# op _005s_power_combination_eval
# LANG: _005h, _005r --> num_005t
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v184_num_005t = (v178__005h)*(v183__005r)
v184_num_005t = v184_num_005t.reshape((2, 400))

# op _006f_linear_combination_eval
# LANG: _006e --> _006g
# SHAPES: (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v209__006g = _006f_constant+v208__006e

# op _006l_power_combination_eval
# LANG: _006k --> _006m
# SHAPES: (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v212__006m = (v211__006k**-1)
v212__006m = v212__006m.reshape((2, 400))

# op _006p_power_combination_eval
# LANG: _006o --> _006q
# SHAPES: (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v214__006q = (v213__006o**-1)
v214__006q = v214__006q.reshape((2, 400))

# op _001E_power_combination_eval
# LANG: _001D --> _001F
# SHAPES: (2, 2, 10) --> (2, 2, 10)
# full namespace: ComputeNormals
v55__001F = (v54__001D**0.5)
v55__001F = v55__001F.reshape((2, 2, 10))

# op _0050_power_combination_eval
# LANG: _004_, _004A --> _0051
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v170__0051 = (v169__004_)*(v156__004A)
v170__0051 = v170__0051.reshape((2, 400, 3))

# op _0054_power_combination_eval
# LANG: _0053 --> _0055
# SHAPES: (2, 400, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v172__0055 = (v171__0053)
v172__0055 = (v172__0055*_0054_coeff).reshape((2, 400, 3))

# op _005Y_power_combination_eval
# LANG: _005N, _005X --> num_005Z
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v200_num_005Z = (v194__005N)*(v199__005X)
v200_num_005Z = v200_num_005Z.reshape((2, 400))

# op _005u expand_array_eval
# LANG: num_005t --> _005v
# SHAPES: (2, 400) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v185__005v = np.einsum('ab,c->abc', v184_num_005t.reshape((2, 400)) ,np.ones((3,))).reshape((2, 400, 3))

# op _005y cross_product_eval
# LANG: _004q, _0046 --> _005z
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v187__005z = np.cross(v141__0046, v151__004q, axisa = 2, axisb = 2, axisc = 2)

# op _006h_power_combination_eval
# LANG: _006g --> _006i
# SHAPES: (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v210__006i = (v209__006g**-1)
v210__006i = v210__006i.reshape((2, 400))

# op _006r_linear_combination_eval
# LANG: _006m, _006q --> _006s
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v215__006s = v212__006m+v214__006q

# op _001G expand_array_eval
# LANG: _001F --> _001H
# SHAPES: (2, 2, 10) --> (2, 2, 10, 3)
# full namespace: ComputeNormals
v56__001H = np.einsum('abc,d->abcd', v55__001F.reshape((2, 2, 10)) ,np.ones((3,))).reshape((2, 2, 10, 3))

# op _005A_power_combination_eval
# LANG: _005z --> _005B
# SHAPES: (2, 400, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v188__005B = (v187__005z)
v188__005B = (v188__005B*_005A_coeff).reshape((2, 400, 3))

# op _005_ expand_array_eval
# LANG: num_005Z --> _0060
# SHAPES: (2, 400) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v201__0060 = np.einsum('ab,c->abc', v200_num_005Z.reshape((2, 400)) ,np.ones((3,))).reshape((2, 400, 3))

# op _005w_power_combination_eval
# LANG: _005v, _0055 --> _005x
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v186__005x = (v185__005v)*(v172__0055)
v186__005x = v186__005x.reshape((2, 400, 3))

# op _0063 cross_product_eval
# LANG: _004q, _003t --> _0064
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v203__0064 = np.cross(v151__004q, v121__003t, axisa = 2, axisb = 2, axisc = 2)

# op _006t_power_combination_eval
# LANG: _006i, _006s --> num_006u
# SHAPES: (2, 400), (2, 400) --> (2, 400)
# full namespace: SubAicBiotSavarts
v216_num_006u = (v210__006i)*(v215__006s)
v216_num_006u = v216_num_006u.reshape((2, 400))

# op _006z_linear_combination_eval
# LANG: _0051 --> _006A
# SHAPES: (2, 400, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v219__006A = v170__0051

# op _0005 expand_array_eval
# LANG: frame_vel --> _0006
# SHAPES: (2, 3) --> (2, 20, 3)
# full namespace: 
v2__0006 = np.einsum('ac,b->abc', v231_frame_vel.reshape((2, 3)) ,np.ones((20,))).reshape((2, 20, 3))

# op _001I_power_combination_eval
# LANG: _001z, _001H --> surface_normals
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: ComputeNormals
v225_surface_normals = (v52__001z)*(v56__001H**-1)
v225_surface_normals = v225_surface_normals.reshape((2, 2, 10, 3))

# op _0061_power_combination_eval
# LANG: _0060, _005B --> _0062
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v202__0062 = (v201__0060)*(v188__005B)
v202__0062 = v202__0062.reshape((2, 400, 3))

# op _0065_power_combination_eval
# LANG: _0064 --> _0066
# SHAPES: (2, 400, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v204__0066 = (v203__0064)
v204__0066 = (v204__0066*_0065_coeff).reshape((2, 400, 3))

# op _006B_linear_combination_eval
# LANG: _006A, _005x --> _006C
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v220__006C = v219__006A+v186__005x

# op _006v expand_array_eval
# LANG: num_006u --> _006w
# SHAPES: (2, 400) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v217__006w = np.einsum('ab,c->abc', v216_num_006u.reshape((2, 400)) ,np.ones((3,))).reshape((2, 400, 3))

# op _0007_linear_combination_eval
# LANG: _0006 --> surface_kinematic_vel
# SHAPES: (2, 20, 3) --> (2, 20, 3)
# full namespace: 
v100_surface_kinematic_vel = -1*v2__0006

# op _002V reshape_eval
# LANG: surface_normals --> _002W
# SHAPES: (2, 2, 10, 3) --> (2, 20, 3)
# full namespace: Projection_rhs
v102__002W = v225_surface_normals.reshape((2, 20, 3))

# op _006D_linear_combination_eval
# LANG: _006C, _0062 --> _006E
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v221__006E = v220__006C+v202__0062

# op _006L reshape_eval
# LANG: surface_normals --> _006M
# SHAPES: (2, 2, 10, 3) --> (2, 20, 3)
# full namespace: ProjectionAic
v226__006M = v225_surface_normals.reshape((2, 20, 3))

# op _006x_power_combination_eval
# LANG: _006w, _0066 --> _006y
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v218__006y = (v217__006w)*(v204__0066)
v218__006y = v218__006y.reshape((2, 400, 3))

# op _002X_power_combination_eval
# LANG: _002W, surface_kinematic_vel --> _002Y
# SHAPES: (2, 20, 3), (2, 20, 3) --> (2, 20, 3)
# full namespace: Projection_rhs
v103__002Y = (v100_surface_kinematic_vel)*(v102__002W)
v103__002Y = v103__002Y.reshape((2, 20, 3))

# op _006F_linear_combination_eval
# LANG: _006E, _006y --> _006G
# SHAPES: (2, 400, 3), (2, 400, 3) --> (2, 400, 3)
# full namespace: SubAicBiotSavarts
v222__006G = v221__006E+v218__006y

# op _006N_indexed_passthrough_eval
# LANG: _006M --> normal_concatenated_aic_projection
# SHAPES: (2, 20, 3) --> (2, 20, 3)
# full namespace: ProjectionAic
v224_normal_concatenated_aic_projection__temp[i_v226__006M__006N_indexed_passthrough_eval] = v226__006M.flatten()
v224_normal_concatenated_aic_projection = v224_normal_concatenated_aic_projection__temp.copy()

# op _002Z_single_tensor_sum_with_axis_eval
# LANG: _002Y --> _002_
# SHAPES: (2, 20, 3) --> (2, 20)
# full namespace: Projection_rhs
v104__002_ = np.sum(v103__002Y, axis = (2,)).reshape((2, 20))

# op _006H reshape_eval
# LANG: _006G --> aic
# SHAPES: (2, 400, 3) --> (2, 20, 20, 3)
# full namespace: SubAicBiotSavarts
v227_aic = v222__006G.reshape((2, 20, 20, 3))

# op _006P expand_array_eval
# LANG: normal_concatenated_aic_projection --> _006Q
# SHAPES: (2, 20, 3) --> (2, 20, 20, 3)
# full namespace: ProjectionAic
v228__006Q = np.einsum('acd,b->abcd', v224_normal_concatenated_aic_projection.reshape((2, 20, 3)) ,np.ones((20,))).reshape((2, 20, 20, 3))

# op _0030_indexed_passthrough_eval
# LANG: _002_ --> rhs
# SHAPES: (2, 20) --> (2, 20)
# full namespace: Projection_rhs
v99_rhs__temp[i_v104__002___0030_indexed_passthrough_eval] = v104__002_.flatten()
v99_rhs = v99_rhs__temp.copy()

# op _006R_power_combination_eval
# LANG: _006Q, aic --> _006S
# SHAPES: (2, 20, 20, 3), (2, 20, 20, 3) --> (2, 20, 20, 3)
# full namespace: ProjectionAic
v229__006S = (v227_aic)*(v228__006Q)
v229__006S = v229__006S.reshape((2, 20, 20, 3))

# op _000n reshape_eval
# LANG: M_reshaped --> _000o
# SHAPES: (2, 20, 20) --> (2, 20, 20)
# full namespace: 
v9__000o = v7_M_reshaped.reshape((2, 20, 20))

# op _000x_decompose_eval
# LANG: rhs --> _000R, _000y
# SHAPES: (2, 20) --> (1, 20), (1, 20)
# full namespace: 
v15__000y = ((v99_rhs.flatten())[src_indices__000y__000x]).reshape((1, 20))
v25__000R = ((v99_rhs.flatten())[src_indices__000R__000x]).reshape((1, 20))

# op _002f_decompose_eval
# LANG: surface --> _002t, _002g, _002j, _002o
# SHAPES: (2, 3, 11, 3) --> (2, 2, 10, 3), (2, 2, 10, 3), (2, 2, 10, 3), (2, 2, 10, 3)
# full namespace: GeometricPropertyExtraction
v78__002g = ((v77_surface.flatten())[src_indices__002g__002f]).reshape((2, 2, 10, 3))
v80__002j = ((v77_surface.flatten())[src_indices__002j__002f]).reshape((2, 2, 10, 3))
v83__002o = ((v77_surface.flatten())[src_indices__002o__002f]).reshape((2, 2, 10, 3))
v86__002t = ((v77_surface.flatten())[src_indices__002t__002f]).reshape((2, 2, 10, 3))

# op _006T_single_tensor_sum_with_axis_eval
# LANG: _006S --> aic_projection
# SHAPES: (2, 20, 20, 3) --> (2, 20, 20)
# full namespace: ProjectionAic
v230_aic_projection = np.sum(v229__006S, axis = (3,)).reshape((2, 20, 20))

# op _000S reshape_eval
# LANG: _000R --> _000T
# SHAPES: (1, 20) --> (20,)
# full namespace: 
v26__000T = v25__000R.reshape((20,))

# op _000p_linear_combination_eval
# LANG: _000o, aic_projection --> MTX
# SHAPES: (2, 20, 20), (2, 20, 20) --> (2, 20, 20)
# full namespace: 
v10_MTX = v230_aic_projection+v9__000o

# op _000z reshape_eval
# LANG: _000y --> _000A
# SHAPES: (1, 20) --> (20,)
# full namespace: 
v16__000A = v15__000y.reshape((20,))

# op _002B_power_combination_eval
# LANG: _002o --> _002C
# SHAPES: (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: GeometricPropertyExtraction
v91__002C = (v83__002o)
v91__002C = (v91__002C*_002B_coeff).reshape((2, 2, 10, 3))

# op _002z_power_combination_eval
# LANG: _002g --> _002A
# SHAPES: (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: GeometricPropertyExtraction
v90__002A = (v78__002g)
v90__002A = (v90__002A*_002z_coeff).reshape((2, 2, 10, 3))

# op _000B_linear_combination_eval
# LANG: _000A --> _000C
# SHAPES: (20,) --> (20,)
# full namespace: 
v17__000C = -1*v16__000A

# op _000U_linear_combination_eval
# LANG: _000T --> _000V
# SHAPES: (20,) --> (20,)
# full namespace: 
v27__000V = -1*v26__000T

# op _000t_decompose_eval
# LANG: MTX --> _000O, _000u
# SHAPES: (2, 20, 20) --> (1, 20, 20), (1, 20, 20)
# full namespace: 
v13__000u = ((v10_MTX.flatten())[src_indices__000u__000t]).reshape((1, 20, 20))
v23__000O = ((v10_MTX.flatten())[src_indices__000O__000t]).reshape((1, 20, 20))

# op _001__linear_combination_eval
# LANG: _001Y, _001Z --> _0020
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: GeometricPropertyExtraction
v69__0020 = v67__001Y+-1*v68__001Z

# op _0022_linear_combination_eval
# LANG: _0021, _001T --> _0023
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: GeometricPropertyExtraction
v71__0023 = v70__0021+-1*v64__001T

# op _002D_linear_combination_eval
# LANG: _002A, _002C --> _002E
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: GeometricPropertyExtraction
v92__002E = v90__002A+v91__002C

# op _002F_power_combination_eval
# LANG: _002j --> _002G
# SHAPES: (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: GeometricPropertyExtraction
v93__002G = (v80__002j)
v93__002G = (v93__002G*_002F_coeff).reshape((2, 2, 10, 3))

# op _000D reshape_eval
# LANG: _000C --> _000E
# SHAPES: (20,) --> (20, 1)
# full namespace: 
v18__000E = v17__000C.reshape((20, 1))

# op _000P reshape_eval
# LANG: _000O --> _000Q
# SHAPES: (1, 20, 20) --> (20, 20)
# full namespace: 
v24__000Q = v23__000O.reshape((20, 20))

# op _000W reshape_eval
# LANG: _000V --> _000X
# SHAPES: (20,) --> (20, 1)
# full namespace: 
v28__000X = v27__000V.reshape((20, 1))

# op _000v reshape_eval
# LANG: _000u --> _000w
# SHAPES: (1, 20, 20) --> (20, 20)
# full namespace: 
v14__000w = v13__000u.reshape((20, 20))

# op _0024 cross_product_eval
# LANG: _0020, _0023 --> _0025
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: GeometricPropertyExtraction
v72__0025 = np.cross(v69__0020, v71__0023, axisa = 3, axisb = 3, axisc = 3)

# op _002H_linear_combination_eval
# LANG: _002E, _002G --> _002I
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: GeometricPropertyExtraction
v94__002I = v92__002E+-1*v93__002G

# op _002J_power_combination_eval
# LANG: _002t --> _002K
# SHAPES: (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: GeometricPropertyExtraction
v95__002K = (v86__002t)
v95__002K = (v95__002K*_002J_coeff).reshape((2, 2, 10, 3))

# op _000F_solve_linear_system_eval
# LANG: _000w, _000E --> _000G
# SHAPES: (20, 20), (20, 1) --> (20, 1)
# full namespace: 
v19__000G = _000Fv19__000G_solver(v14__000w, v18__000E, False)

# op _000Y_solve_linear_system_eval
# LANG: _000Q, _000X --> _000Z
# SHAPES: (20, 20), (20, 1) --> (20, 1)
# full namespace: 
v29__000Z = _000Yv29__000Z_solver(v24__000Q, v28__000X, False)

# op _0026_power_combination_eval
# LANG: _0025 --> _0027
# SHAPES: (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: GeometricPropertyExtraction
v73__0027 = (v72__0025**2)
v73__0027 = v73__0027.reshape((2, 2, 10, 3))

# op _002L_linear_combination_eval
# LANG: _002I, _002K --> _002M
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: GeometricPropertyExtraction
v96__002M = v94__002I+-1*v95__002K

# op _002h_power_combination_eval
# LANG: _002g --> _002i
# SHAPES: (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: GeometricPropertyExtraction
v79__002i = (v78__002g)
v79__002i = (v79__002i*_002h_coeff).reshape((2, 2, 10, 3))

# op _002k_power_combination_eval
# LANG: _002j --> _002l
# SHAPES: (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: GeometricPropertyExtraction
v81__002l = (v80__002j)
v81__002l = (v81__002l*_002k_coeff).reshape((2, 2, 10, 3))

# op _000H reshape_eval
# LANG: _000G --> _000I
# SHAPES: (20, 1) --> (20,)
# full namespace: 
v20__000I = v19__000G.reshape((20,))

# op _000_ reshape_eval
# LANG: _000Z --> _0010
# SHAPES: (20, 1) --> (20,)
# full namespace: 
v30__0010 = v29__000Z.reshape((20,))

# op _0028_single_tensor_sum_with_axis_eval
# LANG: _0027 --> _0029
# SHAPES: (2, 2, 10, 3) --> (2, 2, 10)
# full namespace: GeometricPropertyExtraction
v74__0029 = np.sum(v73__0027, axis = (3,)).reshape((2, 2, 10))

# op _002N reshape_eval
# LANG: _002M --> _002O
# SHAPES: (2, 2, 10, 3) --> (2, 20, 3)
# full namespace: GeometricPropertyExtraction
v97__002O = v96__002M.reshape((2, 20, 3))

# op _002m_linear_combination_eval
# LANG: _002i, _002l --> _002n
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: GeometricPropertyExtraction
v82__002n = v79__002i+v81__002l

# op _002p_power_combination_eval
# LANG: _002o --> _002q
# SHAPES: (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: GeometricPropertyExtraction
v84__002q = (v83__002o)
v84__002q = (v84__002q*_002p_coeff).reshape((2, 2, 10, 3))

# op _000L reshape_eval
# LANG: _000I --> _000M
# SHAPES: (20,) --> (1, 20)
# full namespace: 
v22__000M = v20__000I.reshape((1, 20))

# op _0012 reshape_eval
# LANG: _0010 --> _0013
# SHAPES: (20,) --> (1, 20)
# full namespace: 
v32__0013 = v30__0010.reshape((1, 20))

# op _002P_linear_combination_eval
# LANG: _002O --> _002Q
# SHAPES: (2, 20, 3) --> (2, 20, 3)
# full namespace: GeometricPropertyExtraction
v98__002Q = -1*v97__002O

# op _002a_power_combination_eval
# LANG: _0029 --> _002b
# SHAPES: (2, 2, 10) --> (2, 2, 10)
# full namespace: GeometricPropertyExtraction
v75__002b = (v74__0029**0.5)
v75__002b = v75__002b.reshape((2, 2, 10))

# op _002r_linear_combination_eval
# LANG: _002n, _002q --> _002s
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: GeometricPropertyExtraction
v85__002s = v82__002n+v84__002q

# op _002u_power_combination_eval
# LANG: _002t --> _002v
# SHAPES: (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: GeometricPropertyExtraction
v87__002v = (v86__002t)
v87__002v = (v87__002v*_002u_coeff).reshape((2, 2, 10, 3))

# op _0033_linear_combination_eval
# LANG: surface_collocation_pts --> _0034
# SHAPES: (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: SubAicBiotSavarts
v107__0034 = v241_surface_collocation_pts

# op _0037_linear_combination_eval
# LANG: surface_bound_vtx_coords --> _0038
# SHAPES: (2, 3, 11, 3) --> (2, 3, 11, 3)
# full namespace: SubAicBiotSavarts
v109__0038 = v232_surface_bound_vtx_coords

# op _007d_linear_combination_eval
# LANG: surface_collocation_pts --> _007e
# SHAPES: (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: WakeSubAicBiotSavarts
v243__007e = v241_surface_collocation_pts

# op _007h_linear_combination_eval
# LANG: surface_wake_coords --> _007i
# SHAPES: (2, 2, 11, 3) --> (2, 2, 11, 3)
# full namespace: WakeSubAicBiotSavarts
v245__007i = v348_surface_wake_coords

# op _000N_indexed_passthrough_eval
# LANG: _000M, _0013 --> circulation_strength
# SHAPES: (1, 20), (1, 20) --> (2, 20)
# full namespace: 
v12_circulation_strength__temp[i_v22__000M__000N_indexed_passthrough_eval] = v22__000M.flatten()
v12_circulation_strength = v12_circulation_strength__temp.copy()
v12_circulation_strength__temp[i_v32__0013__000N_indexed_passthrough_eval] = v32__0013.flatten()
v12_circulation_strength = v12_circulation_strength__temp.copy()

# op _002R_indexed_passthrough_eval
# LANG: _002Q --> bound_vecs_all_surfaces
# SHAPES: (2, 20, 3) --> (2, 20, 3)
# full namespace: GeometricPropertyExtraction
v89_bound_vecs_all_surfaces__temp[i_v98__002Q__002R_indexed_passthrough_eval] = v98__002Q.flatten()
v89_bound_vecs_all_surfaces = v89_bound_vecs_all_surfaces__temp.copy()

# op _002c_power_combination_eval
# LANG: _002b --> surface_panel_areas
# SHAPES: (2, 2, 10) --> (2, 2, 10)
# full namespace: GeometricPropertyExtraction
v76_surface_panel_areas = (v75__002b)
v76_surface_panel_areas = (v76_surface_panel_areas*_002c_coeff).reshape((2, 2, 10))

# op _002w_linear_combination_eval
# LANG: _002s, _002v --> surface_force_evaluation_pts
# SHAPES: (2, 2, 10, 3), (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: GeometricPropertyExtraction
v88_surface_force_evaluation_pts = v85__002s+v87__002v

# op _0035_print_var_eval
# LANG: _0034 --> _0034_print
# SHAPES: (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: SubAicBiotSavarts
print()
print('printing ', 'v107__0034 (_0034)')
print(v107__0034)

# op _0039_print_var_eval
# LANG: _0038 --> _0038_print
# SHAPES: (2, 3, 11, 3) --> (2, 3, 11, 3)
# full namespace: SubAicBiotSavarts
print()
print('printing ', 'v109__0038 (_0038)')
print(v109__0038)

# op _007f_print_var_eval
# LANG: _007e --> _007e_print
# SHAPES: (2, 2, 10, 3) --> (2, 2, 10, 3)
# full namespace: WakeSubAicBiotSavarts
print()
print('printing ', 'v243__007e (_007e)')
print(v243__007e)

# op _007j_print_var_eval
# LANG: _007i --> _007i_print
# SHAPES: (2, 2, 11, 3) --> (2, 2, 11, 3)
# full namespace: WakeSubAicBiotSavarts
print()
print('printing ', 'v245__007i (_007i)')
print(v245__007i)