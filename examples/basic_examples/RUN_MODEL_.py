

# RUN_MODEL_

# system evaluation block

# op _000u_decompose_eval
# LANG: surface --> _000F, _000v, _000y, _000E
# SHAPES: (2, 10, 11, 3) --> (2, 1, 11, 3), (2, 9, 11, 3), (2, 9, 11, 3), (2, 1, 11, 3)
# full namespace: MeshToVortexMesh
v14__000v = ((v56_surface.flatten())[src_indices__000v__000u]).reshape((2, 9, 11, 3))
v16__000y = ((v56_surface.flatten())[src_indices__000y__000u]).reshape((2, 9, 11, 3))
v19__000E = ((v56_surface.flatten())[src_indices__000E__000u]).reshape((2, 1, 11, 3))
v20__000F = ((v56_surface.flatten())[src_indices__000F__000u]).reshape((2, 1, 11, 3))

# op _000G_linear_combination_eval
# LANG: _000E, _000F --> _000H
# SHAPES: (2, 1, 11, 3), (2, 1, 11, 3) --> (2, 1, 11, 3)
# full namespace: MeshToVortexMesh
v21__000H = v19__000E+-1*v20__000F

# op _000I_power_combination_eval
# LANG: _000H --> _000J
# SHAPES: (2, 1, 11, 3) --> (2, 1, 11, 3)
# full namespace: MeshToVortexMesh
v22__000J = (v21__000H)
v22__000J = (v22__000J*_000I_coeff).reshape((2, 1, 11, 3))

# op _000w_power_combination_eval
# LANG: _000v --> _000x
# SHAPES: (2, 9, 11, 3) --> (2, 9, 11, 3)
# full namespace: MeshToVortexMesh
v15__000x = (v14__000v)
v15__000x = (v15__000x*_000w_coeff).reshape((2, 9, 11, 3))

# op _000z_power_combination_eval
# LANG: _000y --> _000A
# SHAPES: (2, 9, 11, 3) --> (2, 9, 11, 3)
# full namespace: MeshToVortexMesh
v17__000A = (v16__000y)
v17__000A = (v17__000A*_000z_coeff).reshape((2, 9, 11, 3))

# op _000B_linear_combination_eval
# LANG: _000x, _000A --> _000C
# SHAPES: (2, 9, 11, 3), (2, 9, 11, 3) --> (2, 9, 11, 3)
# full namespace: MeshToVortexMesh
v18__000C = v15__000x+v17__000A

# op _000K_linear_combination_eval
# LANG: _000E, _000J --> _000L
# SHAPES: (2, 1, 11, 3), (2, 1, 11, 3) --> (2, 1, 11, 3)
# full namespace: MeshToVortexMesh
v23__000L = v19__000E+v22__000J

# op _000D_indexed_passthrough_eval
# LANG: _000C, _000L --> surface_bound_vtx_coords
# SHAPES: (2, 9, 11, 3), (2, 1, 11, 3) --> (2, 10, 11, 3)
# full namespace: MeshToVortexMesh
v193_surface_bound_vtx_coords__temp[i_v18__000C__000D_indexed_passthrough_eval] = v18__000C.flatten()
v193_surface_bound_vtx_coords = v193_surface_bound_vtx_coords__temp.copy()
v193_surface_bound_vtx_coords__temp[i_v23__000L__000D_indexed_passthrough_eval] = v23__000L.flatten()
v193_surface_bound_vtx_coords = v193_surface_bound_vtx_coords__temp.copy()

# op _005L_decompose_eval
# LANG: surface_bound_vtx_coords --> _005M
# SHAPES: (2, 10, 11, 3) --> (2, 1, 11, 3)
# full namespace: GenerateFixedWake
v194__005M = ((v193_surface_bound_vtx_coords.flatten())[src_indices__005M__005L]).reshape((2, 1, 11, 3))

# op _005S_linear_combination_eval
# LANG: frame_vel --> _005T
# SHAPES: (2, 3) --> (2, 3)
# full namespace: GenerateFixedWake
v198__005T = -1*v192_frame_vel

# op _005N reshape_eval
# LANG: _005M --> _005O
# SHAPES: (2, 1, 11, 3) --> (2, 11, 3)
# full namespace: GenerateFixedWake
v195__005O = v194__005M.reshape((2, 11, 3))

# op _005U expand_array_eval
# LANG: _005T --> _005V
# SHAPES: (2, 3) --> (2, 2, 11, 3)
# full namespace: GenerateFixedWake
v199__005V = np.einsum('ad,bc->abcd', v198__005T.reshape((2, 3)) ,np.ones((2, 11))).reshape((2, 2, 11, 3))

# op _005P expand_array_eval
# LANG: _005O --> _005Q
# SHAPES: (2, 11, 3) --> (2, 2, 11, 3)
# full namespace: GenerateFixedWake
v196__005Q = np.einsum('acd,b->abcd', v195__005O.reshape((2, 11, 3)) ,np.ones((2,))).reshape((2, 2, 11, 3))

# op _005W_power_combination_eval
# LANG: surface_factor, _005V --> _005X
# SHAPES: (2, 2, 11, 3), (2, 2, 11, 3) --> (2, 2, 11, 3)
# full namespace: GenerateFixedWake
v200__005X = (v199__005V)*(v197_surface_factor)
v200__005X = v200__005X.reshape((2, 2, 11, 3))

# op _005Y_linear_combination_eval
# LANG: _005Q, _005X --> surface_wake_coords
# SHAPES: (2, 2, 11, 3), (2, 2, 11, 3) --> (2, 2, 11, 3)
# full namespace: GenerateFixedWake
v305_surface_wake_coords = v196__005Q+v200__005X

# op _0061_decompose_eval
# LANG: surface_wake_coords --> _0062, _0063, _0064, _0065
# SHAPES: (2, 2, 11, 3) --> (2, 1, 10, 3), (2, 1, 10, 3), (2, 1, 10, 3), (2, 1, 10, 3)
# full namespace: WakeSubAicBiotSavarts
v204__0062 = ((v305_surface_wake_coords.flatten())[src_indices__0062__0061]).reshape((2, 1, 10, 3))
v205__0063 = ((v305_surface_wake_coords.flatten())[src_indices__0063__0061]).reshape((2, 1, 10, 3))
v206__0064 = ((v305_surface_wake_coords.flatten())[src_indices__0064__0061]).reshape((2, 1, 10, 3))
v207__0065 = ((v305_surface_wake_coords.flatten())[src_indices__0065__0061]).reshape((2, 1, 10, 3))

# op _0066 reshape_eval
# LANG: surface_collocation_pts --> _0067
# SHAPES: (2, 9, 10, 3) --> (2, 90, 3)
# full namespace: WakeSubAicBiotSavarts
v208__0067 = v202_surface_collocation_pts.reshape((2, 90, 3))

# op _006c reshape_eval
# LANG: _0062 --> _006d
# SHAPES: (2, 1, 10, 3) --> (2, 10, 3)
# full namespace: WakeSubAicBiotSavarts
v211__006d = v204__0062.reshape((2, 10, 3))

# op _006q reshape_eval
# LANG: surface_collocation_pts --> _006r
# SHAPES: (2, 9, 10, 3) --> (2, 90, 3)
# full namespace: WakeSubAicBiotSavarts
v218__006r = v202_surface_collocation_pts.reshape((2, 90, 3))

# op _006w reshape_eval
# LANG: _0063 --> _006x
# SHAPES: (2, 1, 10, 3) --> (2, 10, 3)
# full namespace: WakeSubAicBiotSavarts
v221__006x = v205__0063.reshape((2, 10, 3))

# op _0068 expand_array_eval
# LANG: _0067 --> _0069
# SHAPES: (2, 90, 3) --> (2, 90, 10, 3)
# full namespace: WakeSubAicBiotSavarts
v209__0069 = np.einsum('abd,c->abcd', v208__0067.reshape((2, 90, 3)) ,np.ones((10,))).reshape((2, 90, 10, 3))

# op _006K reshape_eval
# LANG: surface_collocation_pts --> _006L
# SHAPES: (2, 9, 10, 3) --> (2, 90, 3)
# full namespace: WakeSubAicBiotSavarts
v228__006L = v202_surface_collocation_pts.reshape((2, 90, 3))

# op _006Q reshape_eval
# LANG: _0064 --> _006R
# SHAPES: (2, 1, 10, 3) --> (2, 10, 3)
# full namespace: WakeSubAicBiotSavarts
v231__006R = v206__0064.reshape((2, 10, 3))

# op _006e expand_array_eval
# LANG: _006d --> _006f
# SHAPES: (2, 10, 3) --> (2, 90, 10, 3)
# full namespace: WakeSubAicBiotSavarts
v212__006f = np.einsum('acd,b->abcd', v211__006d.reshape((2, 10, 3)) ,np.ones((90,))).reshape((2, 90, 10, 3))

# op _006s expand_array_eval
# LANG: _006r --> _006t
# SHAPES: (2, 90, 3) --> (2, 90, 10, 3)
# full namespace: WakeSubAicBiotSavarts
v219__006t = np.einsum('abd,c->abcd', v218__006r.reshape((2, 90, 3)) ,np.ones((10,))).reshape((2, 90, 10, 3))

# op _006y expand_array_eval
# LANG: _006x --> _006z
# SHAPES: (2, 10, 3) --> (2, 90, 10, 3)
# full namespace: WakeSubAicBiotSavarts
v222__006z = np.einsum('acd,b->abcd', v221__006x.reshape((2, 10, 3)) ,np.ones((90,))).reshape((2, 90, 10, 3))

# op _006A reshape_eval
# LANG: _006z --> _006B
# SHAPES: (2, 90, 10, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v223__006B = v222__006z.reshape((2, 900, 3))

# op _006M expand_array_eval
# LANG: _006L --> _006N
# SHAPES: (2, 90, 3) --> (2, 90, 10, 3)
# full namespace: WakeSubAicBiotSavarts
v229__006N = np.einsum('abd,c->abcd', v228__006L.reshape((2, 90, 3)) ,np.ones((10,))).reshape((2, 90, 10, 3))

# op _006S expand_array_eval
# LANG: _006R --> _006T
# SHAPES: (2, 10, 3) --> (2, 90, 10, 3)
# full namespace: WakeSubAicBiotSavarts
v232__006T = np.einsum('acd,b->abcd', v231__006R.reshape((2, 10, 3)) ,np.ones((90,))).reshape((2, 90, 10, 3))

# op _006a reshape_eval
# LANG: _0069 --> _006b
# SHAPES: (2, 90, 10, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v210__006b = v209__0069.reshape((2, 900, 3))

# op _006g reshape_eval
# LANG: _006f --> _006h
# SHAPES: (2, 90, 10, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v213__006h = v212__006f.reshape((2, 900, 3))

# op _006u reshape_eval
# LANG: _006t --> _006v
# SHAPES: (2, 90, 10, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v220__006v = v219__006t.reshape((2, 900, 3))

# op _0073 reshape_eval
# LANG: surface_collocation_pts --> _0074
# SHAPES: (2, 9, 10, 3) --> (2, 90, 3)
# full namespace: WakeSubAicBiotSavarts
v238__0074 = v202_surface_collocation_pts.reshape((2, 90, 3))

# op _0079 reshape_eval
# LANG: _0065 --> _007a
# SHAPES: (2, 1, 10, 3) --> (2, 10, 3)
# full namespace: WakeSubAicBiotSavarts
v241__007a = v207__0065.reshape((2, 10, 3))

# op _006C_linear_combination_eval
# LANG: _006v, _006B --> _006D
# SHAPES: (2, 900, 3), (2, 900, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v224__006D = v220__006v+-1*v223__006B

# op _006O reshape_eval
# LANG: _006N --> _006P
# SHAPES: (2, 90, 10, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v230__006P = v229__006N.reshape((2, 900, 3))

# op _006U reshape_eval
# LANG: _006T --> _006V
# SHAPES: (2, 90, 10, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v233__006V = v232__006T.reshape((2, 900, 3))

# op _006i_linear_combination_eval
# LANG: _006b, _006h --> _006j
# SHAPES: (2, 900, 3), (2, 900, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v214__006j = v210__006b+-1*v213__006h

# op _0075 expand_array_eval
# LANG: _0074 --> _0076
# SHAPES: (2, 90, 3) --> (2, 90, 10, 3)
# full namespace: WakeSubAicBiotSavarts
v239__0076 = np.einsum('abd,c->abcd', v238__0074.reshape((2, 90, 3)) ,np.ones((10,))).reshape((2, 90, 10, 3))

# op _007b expand_array_eval
# LANG: _007a --> _007c
# SHAPES: (2, 10, 3) --> (2, 90, 10, 3)
# full namespace: WakeSubAicBiotSavarts
v242__007c = np.einsum('acd,b->abcd', v241__007a.reshape((2, 10, 3)) ,np.ones((90,))).reshape((2, 90, 10, 3))

# op _006E_power_combination_eval
# LANG: _006D --> _006F
# SHAPES: (2, 900, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v225__006F = (v224__006D**2)
v225__006F = v225__006F.reshape((2, 900, 3))

# op _006W_linear_combination_eval
# LANG: _006P, _006V --> _006X
# SHAPES: (2, 900, 3), (2, 900, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v234__006X = v230__006P+-1*v233__006V

# op _006k_power_combination_eval
# LANG: _006j --> _006l
# SHAPES: (2, 900, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v215__006l = (v214__006j**2)
v215__006l = v215__006l.reshape((2, 900, 3))

# op _0077 reshape_eval
# LANG: _0076 --> _0078
# SHAPES: (2, 90, 10, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v240__0078 = v239__0076.reshape((2, 900, 3))

# op _007d reshape_eval
# LANG: _007c --> _007e
# SHAPES: (2, 90, 10, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v243__007e = v242__007c.reshape((2, 900, 3))

# op _006G_single_tensor_sum_with_axis_eval
# LANG: _006F --> _006H
# SHAPES: (2, 900, 3) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v226__006H = np.sum(v225__006F, axis = (2,)).reshape((2, 900))

# op _006Y_power_combination_eval
# LANG: _006X --> _006Z
# SHAPES: (2, 900, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v235__006Z = (v234__006X**2)
v235__006Z = v235__006Z.reshape((2, 900, 3))

# op _006m_single_tensor_sum_with_axis_eval
# LANG: _006l --> _006n
# SHAPES: (2, 900, 3) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v216__006n = np.sum(v215__006l, axis = (2,)).reshape((2, 900))

# op _007f_linear_combination_eval
# LANG: _0078, _007e --> _007g
# SHAPES: (2, 900, 3), (2, 900, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v244__007g = v240__0078+-1*v243__007e

# op _006I_power_combination_eval
# LANG: _006H --> _006J
# SHAPES: (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v227__006J = (v226__006H**0.5)
v227__006J = v227__006J.reshape((2, 900))

# op _006__single_tensor_sum_with_axis_eval
# LANG: _006Z --> _0070
# SHAPES: (2, 900, 3) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v236__0070 = np.sum(v235__006Z, axis = (2,)).reshape((2, 900))

# op _006o_power_combination_eval
# LANG: _006n --> _006p
# SHAPES: (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v217__006p = (v216__006n**0.5)
v217__006p = v217__006p.reshape((2, 900))

# op _007h_power_combination_eval
# LANG: _007g --> _007i
# SHAPES: (2, 900, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v245__007i = (v244__007g**2)
v245__007i = v245__007i.reshape((2, 900, 3))

# op _007r_power_combination_eval
# LANG: _006j, _006D --> _007s
# SHAPES: (2, 900, 3), (2, 900, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v250__007s = (v214__006j)*(v224__006D)
v250__007s = v250__007s.reshape((2, 900, 3))

# op _0071_power_combination_eval
# LANG: _0070 --> _0072
# SHAPES: (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v237__0072 = (v236__0070**0.5)
v237__0072 = v237__0072.reshape((2, 900))

# op _007R_power_combination_eval
# LANG: _006X, _006D --> _007S
# SHAPES: (2, 900, 3), (2, 900, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v263__007S = (v224__006D)*(v234__006X)
v263__007S = v263__007S.reshape((2, 900, 3))

# op _007j_single_tensor_sum_with_axis_eval
# LANG: _007i --> _007k
# SHAPES: (2, 900, 3) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v246__007k = np.sum(v245__007i, axis = (2,)).reshape((2, 900))

# op _007t_single_tensor_sum_with_axis_eval
# LANG: _007s --> _007u
# SHAPES: (2, 900, 3) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v251__007u = np.sum(v250__007s, axis = (2,)).reshape((2, 900))

# op _007v_power_combination_eval
# LANG: _006p, _006J --> _007w
# SHAPES: (2, 900), (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v252__007w = (v217__006p)*(v227__006J)
v252__007w = v252__007w.reshape((2, 900))

# op _007B_power_combination_eval
# LANG: _006p --> _007C
# SHAPES: (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v255__007C = (v217__006p**-1)
v255__007C = v255__007C.reshape((2, 900))

# op _007D_power_combination_eval
# LANG: _006J --> _007E
# SHAPES: (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v256__007E = (v227__006J**-1)
v256__007E = v256__007E.reshape((2, 900))

# op _007T_single_tensor_sum_with_axis_eval
# LANG: _007S --> _007U
# SHAPES: (2, 900, 3) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v264__007U = np.sum(v263__007S, axis = (2,)).reshape((2, 900))

# op _007V_power_combination_eval
# LANG: _0072, _006J --> _007W
# SHAPES: (2, 900), (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v265__007W = (v227__006J)*(v237__0072)
v265__007W = v265__007W.reshape((2, 900))

# op _007l_power_combination_eval
# LANG: _007k --> _007m
# SHAPES: (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v247__007m = (v246__007k**0.5)
v247__007m = v247__007m.reshape((2, 900))

# op _007x_linear_combination_eval
# LANG: _007w, _007u --> _007y
# SHAPES: (2, 900), (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v253__007y = v252__007w+v251__007u

# op _008g_power_combination_eval
# LANG: _007g, _006X --> _008h
# SHAPES: (2, 900, 3), (2, 900, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v276__008h = (v234__006X)*(v244__007g)
v276__008h = v276__008h.reshape((2, 900, 3))

# op _009c_decompose_eval
# LANG: surface_wake_coords --> _009i, _009d, _009e, _009h
# SHAPES: (2, 2, 11, 3) --> (2, 1, 10, 3), (2, 1, 10, 3), (2, 1, 10, 3), (2, 1, 10, 3)
# full namespace: ComputeNormalsWake
v306__009d = ((v305_surface_wake_coords.flatten())[src_indices__009d__009c]).reshape((2, 1, 10, 3))
v307__009e = ((v305_surface_wake_coords.flatten())[src_indices__009e__009c]).reshape((2, 1, 10, 3))
v309__009h = ((v305_surface_wake_coords.flatten())[src_indices__009h__009c]).reshape((2, 1, 10, 3))
v310__009i = ((v305_surface_wake_coords.flatten())[src_indices__009i__009c]).reshape((2, 1, 10, 3))

# op _007F_linear_combination_eval
# LANG: _007C, _007E --> _007G
# SHAPES: (2, 900), (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v257__007G = v255__007C+v256__007E

# op _007X_linear_combination_eval
# LANG: _007W, _007U --> _007Y
# SHAPES: (2, 900), (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v266__007Y = v265__007W+v264__007U

# op _007z_power_combination_eval
# LANG: _007y --> _007A
# SHAPES: (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v254__007A = (v253__007y**-1)
v254__007A = v254__007A.reshape((2, 900))

# op _0080_power_combination_eval
# LANG: _006J --> _0081
# SHAPES: (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v268__0081 = (v227__006J**-1)
v268__0081 = v268__0081.reshape((2, 900))

# op _0082_power_combination_eval
# LANG: _0072 --> _0083
# SHAPES: (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v269__0083 = (v237__0072**-1)
v269__0083 = v269__0083.reshape((2, 900))

# op _008G_power_combination_eval
# LANG: _007g, _006j --> _008H
# SHAPES: (2, 900, 3), (2, 900, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v289__008H = (v244__007g)*(v214__006j)
v289__008H = v289__008H.reshape((2, 900, 3))

# op _008i_single_tensor_sum_with_axis_eval
# LANG: _008h --> _008j
# SHAPES: (2, 900, 3) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v277__008j = np.sum(v276__008h, axis = (2,)).reshape((2, 900))

# op _008k_power_combination_eval
# LANG: _007m, _0072 --> _008l
# SHAPES: (2, 900), (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v278__008l = (v237__0072)*(v247__007m)
v278__008l = v278__008l.reshape((2, 900))

# op _009f_linear_combination_eval
# LANG: _009d, _009e --> _009g
# SHAPES: (2, 1, 10, 3), (2, 1, 10, 3) --> (2, 1, 10, 3)
# full namespace: ComputeNormalsWake
v308__009g = v306__009d+-1*v307__009e

# op _009j_linear_combination_eval
# LANG: _009h, _009i --> _009k
# SHAPES: (2, 1, 10, 3), (2, 1, 10, 3) --> (2, 1, 10, 3)
# full namespace: ComputeNormalsWake
v311__009k = v309__009h+-1*v310__009i

# op _007H_power_combination_eval
# LANG: _007A, _007G --> _007I
# SHAPES: (2, 900), (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v258__007I = (v254__007A)*(v257__007G)
v258__007I = v258__007I.reshape((2, 900))

# op _007Z_power_combination_eval
# LANG: _007Y --> _007_
# SHAPES: (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v267__007_ = (v266__007Y**-1)
v267__007_ = v267__007_.reshape((2, 900))

# op _007n cross_product_eval
# LANG: _006j, _006D --> _007o
# SHAPES: (2, 900, 3), (2, 900, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v248__007o = np.cross(v214__006j, v224__006D, axisa = 2, axisb = 2, axisc = 2)

# op _0084_linear_combination_eval
# LANG: _0081, _0083 --> _0085
# SHAPES: (2, 900), (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v270__0085 = v268__0081+v269__0083

# op _008I_single_tensor_sum_with_axis_eval
# LANG: _008H --> _008J
# SHAPES: (2, 900, 3) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v290__008J = np.sum(v289__008H, axis = (2,)).reshape((2, 900))

# op _008K_power_combination_eval
# LANG: _006p, _007m --> _008L
# SHAPES: (2, 900), (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v291__008L = (v247__007m)*(v217__006p)
v291__008L = v291__008L.reshape((2, 900))

# op _008m_linear_combination_eval
# LANG: _008l, _008j --> _008n
# SHAPES: (2, 900), (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v279__008n = v278__008l+v277__008j

# op _008q_power_combination_eval
# LANG: _0072 --> _008r
# SHAPES: (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v281__008r = (v237__0072**-1)
v281__008r = v281__008r.reshape((2, 900))

# op _008s_power_combination_eval
# LANG: _007m --> _008t
# SHAPES: (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v282__008t = (v247__007m**-1)
v282__008t = v282__008t.reshape((2, 900))

# op _009l cross_product_eval
# LANG: _009g, _009k --> _009m
# SHAPES: (2, 1, 10, 3), (2, 1, 10, 3) --> (2, 1, 10, 3)
# full namespace: ComputeNormalsWake
v312__009m = np.cross(v308__009g, v311__009k, axisa = 3, axisb = 3, axisc = 3)

# op _002r_decompose_eval
# LANG: surface_bound_vtx_coords --> _002s, _002t, _002u, _002v
# SHAPES: (2, 10, 11, 3) --> (2, 9, 10, 3), (2, 9, 10, 3), (2, 9, 10, 3), (2, 9, 10, 3)
# full namespace: SubAicBiotSavarts
v86__002s = ((v193_surface_bound_vtx_coords.flatten())[src_indices__002s__002r]).reshape((2, 9, 10, 3))
v87__002t = ((v193_surface_bound_vtx_coords.flatten())[src_indices__002t__002r]).reshape((2, 9, 10, 3))
v88__002u = ((v193_surface_bound_vtx_coords.flatten())[src_indices__002u__002r]).reshape((2, 9, 10, 3))
v89__002v = ((v193_surface_bound_vtx_coords.flatten())[src_indices__002v__002r]).reshape((2, 9, 10, 3))

# op _007J expand_array_eval
# LANG: _007I --> _007K
# SHAPES: (2, 900) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v259__007K = np.einsum('ab,c->abc', v258__007I.reshape((2, 900)) ,np.ones((3,))).reshape((2, 900, 3))

# op _007N cross_product_eval
# LANG: _006X, _006D --> _007O
# SHAPES: (2, 900, 3), (2, 900, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v261__007O = np.cross(v224__006D, v234__006X, axisa = 2, axisb = 2, axisc = 2)

# op _007p_power_combination_eval
# LANG: _007o --> _007q
# SHAPES: (2, 900, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v249__007q = (v248__007o)
v249__007q = (v249__007q*_007p_coeff).reshape((2, 900, 3))

# op _0086_power_combination_eval
# LANG: _007_, _0085 --> _0087
# SHAPES: (2, 900), (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v271__0087 = (v267__007_)*(v270__0085)
v271__0087 = v271__0087.reshape((2, 900))

# op _008M_linear_combination_eval
# LANG: _008L, _008J --> _008N
# SHAPES: (2, 900), (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v292__008N = v291__008L+v290__008J

# op _008Q_power_combination_eval
# LANG: _007m --> _008R
# SHAPES: (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v294__008R = (v247__007m**-1)
v294__008R = v294__008R.reshape((2, 900))

# op _008S_power_combination_eval
# LANG: _006p --> _008T
# SHAPES: (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v295__008T = (v217__006p**-1)
v295__008T = v295__008T.reshape((2, 900))

# op _008o_power_combination_eval
# LANG: _008n --> _008p
# SHAPES: (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v280__008p = (v279__008n**-1)
v280__008p = v280__008p.reshape((2, 900))

# op _008u_linear_combination_eval
# LANG: _008r, _008t --> _008v
# SHAPES: (2, 900), (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v283__008v = v281__008r+v282__008t

# op _009n_power_combination_eval
# LANG: _009m --> _009o
# SHAPES: (2, 1, 10, 3) --> (2, 1, 10, 3)
# full namespace: ComputeNormalsWake
v313__009o = (v312__009m**2)
v313__009o = v313__009o.reshape((2, 1, 10, 3))

# op _002C reshape_eval
# LANG: _002s --> _002D
# SHAPES: (2, 9, 10, 3) --> (2, 90, 3)
# full namespace: SubAicBiotSavarts
v93__002D = v86__002s.reshape((2, 90, 3))

# op _002Q reshape_eval
# LANG: surface_collocation_pts --> _002R
# SHAPES: (2, 9, 10, 3) --> (2, 90, 3)
# full namespace: SubAicBiotSavarts
v100__002R = v202_surface_collocation_pts.reshape((2, 90, 3))

# op _002W reshape_eval
# LANG: _002t --> _002X
# SHAPES: (2, 9, 10, 3) --> (2, 90, 3)
# full namespace: SubAicBiotSavarts
v103__002X = v87__002t.reshape((2, 90, 3))

# op _002w reshape_eval
# LANG: surface_collocation_pts --> _002x
# SHAPES: (2, 9, 10, 3) --> (2, 90, 3)
# full namespace: SubAicBiotSavarts
v90__002x = v202_surface_collocation_pts.reshape((2, 90, 3))

# op _007L_power_combination_eval
# LANG: _007K, _007q --> _007M
# SHAPES: (2, 900, 3), (2, 900, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v260__007M = (v259__007K)*(v249__007q)
v260__007M = v260__007M.reshape((2, 900, 3))

# op _007P_power_combination_eval
# LANG: _007O --> _007Q
# SHAPES: (2, 900, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v262__007Q = (v261__007O)
v262__007Q = (v262__007Q*_007P_coeff).reshape((2, 900, 3))

# op _0088 expand_array_eval
# LANG: _0087 --> _0089
# SHAPES: (2, 900) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v272__0089 = np.einsum('ab,c->abc', v271__0087.reshape((2, 900)) ,np.ones((3,))).reshape((2, 900, 3))

# op _008O_power_combination_eval
# LANG: _008N --> _008P
# SHAPES: (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v293__008P = (v292__008N**-1)
v293__008P = v293__008P.reshape((2, 900))

# op _008U_linear_combination_eval
# LANG: _008R, _008T --> _008V
# SHAPES: (2, 900), (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v296__008V = v294__008R+v295__008T

# op _008c cross_product_eval
# LANG: _007g, _006X --> _008d
# SHAPES: (2, 900, 3), (2, 900, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v274__008d = np.cross(v234__006X, v244__007g, axisa = 2, axisb = 2, axisc = 2)

# op _008w_power_combination_eval
# LANG: _008p, _008v --> _008x
# SHAPES: (2, 900), (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v284__008x = (v280__008p)*(v283__008v)
v284__008x = v284__008x.reshape((2, 900))

# op _009p_single_tensor_sum_with_axis_eval
# LANG: _009o --> _009q
# SHAPES: (2, 1, 10, 3) --> (2, 1, 10)
# full namespace: ComputeNormalsWake
v314__009q = np.sum(v313__009o, axis = (3,)).reshape((2, 1, 10))

# op _002E expand_array_eval
# LANG: _002D --> _002F
# SHAPES: (2, 90, 3) --> (2, 90, 90, 3)
# full namespace: SubAicBiotSavarts
v94__002F = np.einsum('acd,b->abcd', v93__002D.reshape((2, 90, 3)) ,np.ones((90,))).reshape((2, 90, 90, 3))

# op _002S expand_array_eval
# LANG: _002R --> _002T
# SHAPES: (2, 90, 3) --> (2, 90, 90, 3)
# full namespace: SubAicBiotSavarts
v101__002T = np.einsum('abd,c->abcd', v100__002R.reshape((2, 90, 3)) ,np.ones((90,))).reshape((2, 90, 90, 3))

# op _002Y expand_array_eval
# LANG: _002X --> _002Z
# SHAPES: (2, 90, 3) --> (2, 90, 90, 3)
# full namespace: SubAicBiotSavarts
v104__002Z = np.einsum('acd,b->abcd', v103__002X.reshape((2, 90, 3)) ,np.ones((90,))).reshape((2, 90, 90, 3))

# op _002y expand_array_eval
# LANG: _002x --> _002z
# SHAPES: (2, 90, 3) --> (2, 90, 90, 3)
# full namespace: SubAicBiotSavarts
v91__002z = np.einsum('abd,c->abcd', v90__002x.reshape((2, 90, 3)) ,np.ones((90,))).reshape((2, 90, 90, 3))

# op _0039 reshape_eval
# LANG: surface_collocation_pts --> _003a
# SHAPES: (2, 9, 10, 3) --> (2, 90, 3)
# full namespace: SubAicBiotSavarts
v110__003a = v202_surface_collocation_pts.reshape((2, 90, 3))

# op _003f reshape_eval
# LANG: _002u --> _003g
# SHAPES: (2, 9, 10, 3) --> (2, 90, 3)
# full namespace: SubAicBiotSavarts
v113__003g = v88__002u.reshape((2, 90, 3))

# op _008C cross_product_eval
# LANG: _007g, _006j --> _008D
# SHAPES: (2, 900, 3), (2, 900, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v287__008D = np.cross(v244__007g, v214__006j, axisa = 2, axisb = 2, axisc = 2)

# op _008W_power_combination_eval
# LANG: _008P, _008V --> _008X
# SHAPES: (2, 900), (2, 900) --> (2, 900)
# full namespace: WakeSubAicBiotSavarts
v297__008X = (v293__008P)*(v296__008V)
v297__008X = v297__008X.reshape((2, 900))

# op _008a_power_combination_eval
# LANG: _0089, _007Q --> _008b
# SHAPES: (2, 900, 3), (2, 900, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v273__008b = (v272__0089)*(v262__007Q)
v273__008b = v273__008b.reshape((2, 900, 3))

# op _008e_power_combination_eval
# LANG: _008d --> _008f
# SHAPES: (2, 900, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v275__008f = (v274__008d)
v275__008f = (v275__008f*_008e_coeff).reshape((2, 900, 3))

# op _008y expand_array_eval
# LANG: _008x --> _008z
# SHAPES: (2, 900) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v285__008z = np.einsum('ab,c->abc', v284__008x.reshape((2, 900)) ,np.ones((3,))).reshape((2, 900, 3))

# op _0091_linear_combination_eval
# LANG: _007M --> _0092
# SHAPES: (2, 900, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v300__0092 = v260__007M

# op _009r_power_combination_eval
# LANG: _009q --> _009s
# SHAPES: (2, 1, 10) --> (2, 1, 10)
# full namespace: ComputeNormalsWake
v315__009s = (v314__009q**0.5)
v315__009s = v315__009s.reshape((2, 1, 10))

# op _002A reshape_eval
# LANG: _002z --> _002B
# SHAPES: (2, 90, 90, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v92__002B = v91__002z.reshape((2, 8100, 3))

# op _002G reshape_eval
# LANG: _002F --> _002H
# SHAPES: (2, 90, 90, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v95__002H = v94__002F.reshape((2, 8100, 3))

# op _002U reshape_eval
# LANG: _002T --> _002V
# SHAPES: (2, 90, 90, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v102__002V = v101__002T.reshape((2, 8100, 3))

# op _002_ reshape_eval
# LANG: _002Z --> _0030
# SHAPES: (2, 90, 90, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v105__0030 = v104__002Z.reshape((2, 8100, 3))

# op _003b expand_array_eval
# LANG: _003a --> _003c
# SHAPES: (2, 90, 3) --> (2, 90, 90, 3)
# full namespace: SubAicBiotSavarts
v111__003c = np.einsum('abd,c->abcd', v110__003a.reshape((2, 90, 3)) ,np.ones((90,))).reshape((2, 90, 90, 3))

# op _003h expand_array_eval
# LANG: _003g --> _003i
# SHAPES: (2, 90, 3) --> (2, 90, 90, 3)
# full namespace: SubAicBiotSavarts
v114__003i = np.einsum('acd,b->abcd', v113__003g.reshape((2, 90, 3)) ,np.ones((90,))).reshape((2, 90, 90, 3))

# op _003t reshape_eval
# LANG: surface_collocation_pts --> _003u
# SHAPES: (2, 9, 10, 3) --> (2, 90, 3)
# full namespace: SubAicBiotSavarts
v120__003u = v202_surface_collocation_pts.reshape((2, 90, 3))

# op _003z reshape_eval
# LANG: _002v --> _003A
# SHAPES: (2, 9, 10, 3) --> (2, 90, 3)
# full namespace: SubAicBiotSavarts
v123__003A = v89__002v.reshape((2, 90, 3))

# op _008A_power_combination_eval
# LANG: _008z, _008f --> _008B
# SHAPES: (2, 900, 3), (2, 900, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v286__008B = (v285__008z)*(v275__008f)
v286__008B = v286__008B.reshape((2, 900, 3))

# op _008E_power_combination_eval
# LANG: _008D --> _008F
# SHAPES: (2, 900, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v288__008F = (v287__008D)
v288__008F = (v288__008F*_008E_coeff).reshape((2, 900, 3))

# op _008Y expand_array_eval
# LANG: _008X --> _008Z
# SHAPES: (2, 900) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v298__008Z = np.einsum('ab,c->abc', v297__008X.reshape((2, 900)) ,np.ones((3,))).reshape((2, 900, 3))

# op _0093_linear_combination_eval
# LANG: _0092, _008b --> _0094
# SHAPES: (2, 900, 3), (2, 900, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v301__0094 = v300__0092+v273__008b

# op _009t expand_array_eval
# LANG: _009s --> _009u
# SHAPES: (2, 1, 10) --> (2, 1, 10, 3)
# full namespace: ComputeNormalsWake
v316__009u = np.einsum('abc,d->abcd', v315__009s.reshape((2, 1, 10)) ,np.ones((3,))).reshape((2, 1, 10, 3))

# op _002I_linear_combination_eval
# LANG: _002B, _002H --> _002J
# SHAPES: (2, 8100, 3), (2, 8100, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v96__002J = v92__002B+-1*v95__002H

# op _0031_linear_combination_eval
# LANG: _002V, _0030 --> _0032
# SHAPES: (2, 8100, 3), (2, 8100, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v106__0032 = v102__002V+-1*v105__0030

# op _003B expand_array_eval
# LANG: _003A --> _003C
# SHAPES: (2, 90, 3) --> (2, 90, 90, 3)
# full namespace: SubAicBiotSavarts
v124__003C = np.einsum('acd,b->abcd', v123__003A.reshape((2, 90, 3)) ,np.ones((90,))).reshape((2, 90, 90, 3))

# op _003d reshape_eval
# LANG: _003c --> _003e
# SHAPES: (2, 90, 90, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v112__003e = v111__003c.reshape((2, 8100, 3))

# op _003j reshape_eval
# LANG: _003i --> _003k
# SHAPES: (2, 90, 90, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v115__003k = v114__003i.reshape((2, 8100, 3))

# op _003v expand_array_eval
# LANG: _003u --> _003w
# SHAPES: (2, 90, 3) --> (2, 90, 90, 3)
# full namespace: SubAicBiotSavarts
v121__003w = np.einsum('abd,c->abcd', v120__003u.reshape((2, 90, 3)) ,np.ones((90,))).reshape((2, 90, 90, 3))

# op _008__power_combination_eval
# LANG: _008Z, _008F --> _0090
# SHAPES: (2, 900, 3), (2, 900, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v299__0090 = (v298__008Z)*(v288__008F)
v299__0090 = v299__0090.reshape((2, 900, 3))

# op _0095_linear_combination_eval
# LANG: _0094, _008B --> _0096
# SHAPES: (2, 900, 3), (2, 900, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v302__0096 = v301__0094+v286__008B

# op _009v_power_combination_eval
# LANG: _009m, _009u --> surface_wake_coords_normals
# SHAPES: (2, 1, 10, 3), (2, 1, 10, 3) --> (2, 1, 10, 3)
# full namespace: ComputeNormalsWake
v320_surface_wake_coords_normals = (v312__009m)*(v316__009u**-1)
v320_surface_wake_coords_normals = v320_surface_wake_coords_normals.reshape((2, 1, 10, 3))

# op _002K_power_combination_eval
# LANG: _002J --> _002L
# SHAPES: (2, 8100, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v97__002L = (v96__002J**2)
v97__002L = v97__002L.reshape((2, 8100, 3))

# op _0033_power_combination_eval
# LANG: _0032 --> _0034
# SHAPES: (2, 8100, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v107__0034 = (v106__0032**2)
v107__0034 = v107__0034.reshape((2, 8100, 3))

# op _003D reshape_eval
# LANG: _003C --> _003E
# SHAPES: (2, 90, 90, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v125__003E = v124__003C.reshape((2, 8100, 3))

# op _003l_linear_combination_eval
# LANG: _003e, _003k --> _003m
# SHAPES: (2, 8100, 3), (2, 8100, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v116__003m = v112__003e+-1*v115__003k

# op _003x reshape_eval
# LANG: _003w --> _003y
# SHAPES: (2, 90, 90, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v122__003y = v121__003w.reshape((2, 8100, 3))

# op _0097_linear_combination_eval
# LANG: _0096, _0090 --> _0098
# SHAPES: (2, 900, 3), (2, 900, 3) --> (2, 900, 3)
# full namespace: WakeSubAicBiotSavarts
v303__0098 = v302__0096+v299__0090

# op _009A reshape_eval
# LANG: surface_wake_coords_normals --> _009B
# SHAPES: (2, 1, 10, 3) --> (2, 10, 3)
# full namespace: ProjectionWake
v321__009B = v320_surface_wake_coords_normals.reshape((2, 10, 3))

# op _002M_single_tensor_sum_with_axis_eval
# LANG: _002L --> _002N
# SHAPES: (2, 8100, 3) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v98__002N = np.sum(v97__002L, axis = (2,)).reshape((2, 8100))

# op _0035_single_tensor_sum_with_axis_eval
# LANG: _0034 --> _0036
# SHAPES: (2, 8100, 3) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v108__0036 = np.sum(v107__0034, axis = (2,)).reshape((2, 8100))

# op _003F_linear_combination_eval
# LANG: _003y, _003E --> _003G
# SHAPES: (2, 8100, 3), (2, 8100, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v126__003G = v122__003y+-1*v125__003E

# op _003n_power_combination_eval
# LANG: _003m --> _003o
# SHAPES: (2, 8100, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v117__003o = (v116__003m**2)
v117__003o = v117__003o.reshape((2, 8100, 3))

# op _0099 reshape_eval
# LANG: _0098 --> wake_aic
# SHAPES: (2, 900, 3) --> (2, 90, 10, 3)
# full namespace: WakeSubAicBiotSavarts
v319_wake_aic = v303__0098.reshape((2, 90, 10, 3))

# op _009C_indexed_passthrough_eval
# LANG: _009B --> normal_concatenated_wake_rhs
# SHAPES: (2, 10, 3) --> (2, 10, 3)
# full namespace: ProjectionWake
v318_normal_concatenated_wake_rhs__temp[i_v321__009B__009C_indexed_passthrough_eval] = v321__009B.flatten()
v318_normal_concatenated_wake_rhs = v318_normal_concatenated_wake_rhs__temp.copy()

# op _002O_power_combination_eval
# LANG: _002N --> _002P
# SHAPES: (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v99__002P = (v98__002N**0.5)
v99__002P = v99__002P.reshape((2, 8100))

# op _0037_power_combination_eval
# LANG: _0036 --> _0038
# SHAPES: (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v109__0038 = (v108__0036**0.5)
v109__0038 = v109__0038.reshape((2, 8100))

# op _003H_power_combination_eval
# LANG: _003G --> _003I
# SHAPES: (2, 8100, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v127__003I = (v126__003G**2)
v127__003I = v127__003I.reshape((2, 8100, 3))

# op _003R_power_combination_eval
# LANG: _002J, _0032 --> _003S
# SHAPES: (2, 8100, 3), (2, 8100, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v132__003S = (v96__002J)*(v106__0032)
v132__003S = v132__003S.reshape((2, 8100, 3))

# op _003p_single_tensor_sum_with_axis_eval
# LANG: _003o --> _003q
# SHAPES: (2, 8100, 3) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v118__003q = np.sum(v117__003o, axis = (2,)).reshape((2, 8100))

# op _009D einsum_eval
# LANG: normal_concatenated_wake_rhs, wake_aic --> wake_rhs
# SHAPES: (2, 10, 3), (2, 90, 10, 3) --> (2, 90, 10)
# full namespace: ProjectionWake
v322_wake_rhs = np.einsum('lijk,ljk->lij' , v319_wake_aic, v318_normal_concatenated_wake_rhs)

# op _000i_power_combination_eval
# LANG: wake_rhs --> M_mat
# SHAPES: (2, 90, 10) --> (2, 90, 10)
# full namespace: 
v6_M_mat = (v322_wake_rhs)
v6_M_mat = v6_M_mat.reshape((2, 90, 10))

# op _003J_single_tensor_sum_with_axis_eval
# LANG: _003I --> _003K
# SHAPES: (2, 8100, 3) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v128__003K = np.sum(v127__003I, axis = (2,)).reshape((2, 8100))

# op _003T_single_tensor_sum_with_axis_eval
# LANG: _003S --> _003U
# SHAPES: (2, 8100, 3) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v133__003U = np.sum(v132__003S, axis = (2,)).reshape((2, 8100))

# op _003V_power_combination_eval
# LANG: _002P, _0038 --> _003W
# SHAPES: (2, 8100), (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v134__003W = (v99__002P)*(v109__0038)
v134__003W = v134__003W.reshape((2, 8100))

# op _003r_power_combination_eval
# LANG: _003q --> _003s
# SHAPES: (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v119__003s = (v118__003q**0.5)
v119__003s = v119__003s.reshape((2, 8100))

# op _004g_power_combination_eval
# LANG: _003m, _0032 --> _004h
# SHAPES: (2, 8100, 3), (2, 8100, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v145__004h = (v106__0032)*(v116__003m)
v145__004h = v145__004h.reshape((2, 8100, 3))

# op _000N_decompose_eval
# LANG: surface --> _000T, _000O, _000P, _000S
# SHAPES: (2, 10, 11, 3) --> (2, 9, 10, 3), (2, 9, 10, 3), (2, 9, 10, 3), (2, 9, 10, 3)
# full namespace: ComputeNormals
v25__000O = ((v56_surface.flatten())[src_indices__000O__000N]).reshape((2, 9, 10, 3))
v26__000P = ((v56_surface.flatten())[src_indices__000P__000N]).reshape((2, 9, 10, 3))
v28__000S = ((v56_surface.flatten())[src_indices__000S__000N]).reshape((2, 9, 10, 3))
v29__000T = ((v56_surface.flatten())[src_indices__000T__000N]).reshape((2, 9, 10, 3))

# op _000k_custom_explicit_eval
# LANG: M_mat --> M_reshaped
# SHAPES: (2, 90, 10) --> (2, 90, 90)
# full namespace: 
temp = _000k_custom_explicit_func_M_reshaped.solve(v6_M_mat)
v7_M_reshaped = temp[0].copy()

# op _003L_power_combination_eval
# LANG: _003K --> _003M
# SHAPES: (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v129__003M = (v128__003K**0.5)
v129__003M = v129__003M.reshape((2, 8100))

# op _003X_linear_combination_eval
# LANG: _003W, _003U --> _003Y
# SHAPES: (2, 8100), (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v135__003Y = v134__003W+v133__003U

# op _0040_power_combination_eval
# LANG: _002P --> _0041
# SHAPES: (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v137__0041 = (v99__002P**-1)
v137__0041 = v137__0041.reshape((2, 8100))

# op _0042_power_combination_eval
# LANG: _0038 --> _0043
# SHAPES: (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v138__0043 = (v109__0038**-1)
v138__0043 = v138__0043.reshape((2, 8100))

# op _004G_power_combination_eval
# LANG: _003G, _003m --> _004H
# SHAPES: (2, 8100, 3), (2, 8100, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v158__004H = (v116__003m)*(v126__003G)
v158__004H = v158__004H.reshape((2, 8100, 3))

# op _004i_single_tensor_sum_with_axis_eval
# LANG: _004h --> _004j
# SHAPES: (2, 8100, 3) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v146__004j = np.sum(v145__004h, axis = (2,)).reshape((2, 8100))

# op _004k_power_combination_eval
# LANG: _003s, _0038 --> _004l
# SHAPES: (2, 8100), (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v147__004l = (v109__0038)*(v119__003s)
v147__004l = v147__004l.reshape((2, 8100))

# op _000Q_linear_combination_eval
# LANG: _000O, _000P --> _000R
# SHAPES: (2, 9, 10, 3), (2, 9, 10, 3) --> (2, 9, 10, 3)
# full namespace: ComputeNormals
v27__000R = v25__000O+-1*v26__000P

# op _000U_linear_combination_eval
# LANG: _000S, _000T --> _000V
# SHAPES: (2, 9, 10, 3), (2, 9, 10, 3) --> (2, 9, 10, 3)
# full namespace: ComputeNormals
v30__000V = v28__000S+-1*v29__000T

# op _003Z_power_combination_eval
# LANG: _003Y --> _003_
# SHAPES: (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v136__003_ = (v135__003Y**-1)
v136__003_ = v136__003_.reshape((2, 8100))

# op _0044_linear_combination_eval
# LANG: _0041, _0043 --> _0045
# SHAPES: (2, 8100), (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v139__0045 = v137__0041+v138__0043

# op _004I_single_tensor_sum_with_axis_eval
# LANG: _004H --> _004J
# SHAPES: (2, 8100, 3) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v159__004J = np.sum(v158__004H, axis = (2,)).reshape((2, 8100))

# op _004K_power_combination_eval
# LANG: _003M, _003s --> _004L
# SHAPES: (2, 8100), (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v160__004L = (v119__003s)*(v129__003M)
v160__004L = v160__004L.reshape((2, 8100))

# op _004m_linear_combination_eval
# LANG: _004l, _004j --> _004n
# SHAPES: (2, 8100), (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v148__004n = v147__004l+v146__004j

# op _004q_power_combination_eval
# LANG: _0038 --> _004r
# SHAPES: (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v150__004r = (v109__0038**-1)
v150__004r = v150__004r.reshape((2, 8100))

# op _004s_power_combination_eval
# LANG: _003s --> _004t
# SHAPES: (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v151__004t = (v119__003s**-1)
v151__004t = v151__004t.reshape((2, 8100))

# op _0055_power_combination_eval
# LANG: _003G, _002J --> _0056
# SHAPES: (2, 8100, 3), (2, 8100, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v171__0056 = (v126__003G)*(v96__002J)
v171__0056 = v171__0056.reshape((2, 8100, 3))

# op _000W cross_product_eval
# LANG: _000R, _000V --> _000X
# SHAPES: (2, 9, 10, 3), (2, 9, 10, 3) --> (2, 9, 10, 3)
# full namespace: ComputeNormals
v31__000X = np.cross(v27__000R, v30__000V, axisa = 3, axisb = 3, axisc = 3)

# op _003N cross_product_eval
# LANG: _002J, _0032 --> _003O
# SHAPES: (2, 8100, 3), (2, 8100, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v130__003O = np.cross(v96__002J, v106__0032, axisa = 2, axisb = 2, axisc = 2)

# op _0046_power_combination_eval
# LANG: _003_, _0045 --> _0047
# SHAPES: (2, 8100), (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v140__0047 = (v136__003_)*(v139__0045)
v140__0047 = v140__0047.reshape((2, 8100))

# op _004M_linear_combination_eval
# LANG: _004L, _004J --> _004N
# SHAPES: (2, 8100), (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v161__004N = v160__004L+v159__004J

# op _004Q_power_combination_eval
# LANG: _003s --> _004R
# SHAPES: (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v163__004R = (v119__003s**-1)
v163__004R = v163__004R.reshape((2, 8100))

# op _004S_power_combination_eval
# LANG: _003M --> _004T
# SHAPES: (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v164__004T = (v129__003M**-1)
v164__004T = v164__004T.reshape((2, 8100))

# op _004o_power_combination_eval
# LANG: _004n --> _004p
# SHAPES: (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v149__004p = (v148__004n**-1)
v149__004p = v149__004p.reshape((2, 8100))

# op _004u_linear_combination_eval
# LANG: _004r, _004t --> _004v
# SHAPES: (2, 8100), (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v152__004v = v150__004r+v151__004t

# op _0057_single_tensor_sum_with_axis_eval
# LANG: _0056 --> _0058
# SHAPES: (2, 8100, 3) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v172__0058 = np.sum(v171__0056, axis = (2,)).reshape((2, 8100))

# op _0059_power_combination_eval
# LANG: _002P, _003M --> _005a
# SHAPES: (2, 8100), (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v173__005a = (v129__003M)*(v99__002P)
v173__005a = v173__005a.reshape((2, 8100))

# op _000Y_power_combination_eval
# LANG: _000X --> _000Z
# SHAPES: (2, 9, 10, 3) --> (2, 9, 10, 3)
# full namespace: ComputeNormals
v32__000Z = (v31__000X**2)
v32__000Z = v32__000Z.reshape((2, 9, 10, 3))

# op _003P_power_combination_eval
# LANG: _003O --> _003Q
# SHAPES: (2, 8100, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v131__003Q = (v130__003O)
v131__003Q = (v131__003Q*_003P_coeff).reshape((2, 8100, 3))

# op _0048 expand_array_eval
# LANG: _0047 --> _0049
# SHAPES: (2, 8100) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v141__0049 = np.einsum('ab,c->abc', v140__0047.reshape((2, 8100)) ,np.ones((3,))).reshape((2, 8100, 3))

# op _004O_power_combination_eval
# LANG: _004N --> _004P
# SHAPES: (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v162__004P = (v161__004N**-1)
v162__004P = v162__004P.reshape((2, 8100))

# op _004U_linear_combination_eval
# LANG: _004R, _004T --> _004V
# SHAPES: (2, 8100), (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v165__004V = v163__004R+v164__004T

# op _004c cross_product_eval
# LANG: _003m, _0032 --> _004d
# SHAPES: (2, 8100, 3), (2, 8100, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v143__004d = np.cross(v106__0032, v116__003m, axisa = 2, axisb = 2, axisc = 2)

# op _004w_power_combination_eval
# LANG: _004p, _004v --> _004x
# SHAPES: (2, 8100), (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v153__004x = (v149__004p)*(v152__004v)
v153__004x = v153__004x.reshape((2, 8100))

# op _005b_linear_combination_eval
# LANG: _005a, _0058 --> _005c
# SHAPES: (2, 8100), (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v174__005c = v173__005a+v172__0058

# op _005f_power_combination_eval
# LANG: _003M --> _005g
# SHAPES: (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v176__005g = (v129__003M**-1)
v176__005g = v176__005g.reshape((2, 8100))

# op _005h_power_combination_eval
# LANG: _002P --> _005i
# SHAPES: (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v177__005i = (v99__002P**-1)
v177__005i = v177__005i.reshape((2, 8100))

# op _000__single_tensor_sum_with_axis_eval
# LANG: _000Z --> _0010
# SHAPES: (2, 9, 10, 3) --> (2, 9, 10)
# full namespace: ComputeNormals
v33__0010 = np.sum(v32__000Z, axis = (3,)).reshape((2, 9, 10))

# op _001D_decompose_eval
# LANG: surface --> _001R, _001E, _001H, _001M
# SHAPES: (2, 10, 11, 3) --> (2, 9, 10, 3), (2, 9, 10, 3), (2, 9, 10, 3), (2, 9, 10, 3)
# full namespace: GeometricPropertyExtraction
v57__001E = ((v56_surface.flatten())[src_indices__001E__001D]).reshape((2, 9, 10, 3))
v59__001H = ((v56_surface.flatten())[src_indices__001H__001D]).reshape((2, 9, 10, 3))
v62__001M = ((v56_surface.flatten())[src_indices__001M__001D]).reshape((2, 9, 10, 3))
v65__001R = ((v56_surface.flatten())[src_indices__001R__001D]).reshape((2, 9, 10, 3))

# op _004C cross_product_eval
# LANG: _003G, _003m --> _004D
# SHAPES: (2, 8100, 3), (2, 8100, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v156__004D = np.cross(v116__003m, v126__003G, axisa = 2, axisb = 2, axisc = 2)

# op _004W_power_combination_eval
# LANG: _004P, _004V --> _004X
# SHAPES: (2, 8100), (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v166__004X = (v162__004P)*(v165__004V)
v166__004X = v166__004X.reshape((2, 8100))

# op _004a_power_combination_eval
# LANG: _0049, _003Q --> _004b
# SHAPES: (2, 8100, 3), (2, 8100, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v142__004b = (v141__0049)*(v131__003Q)
v142__004b = v142__004b.reshape((2, 8100, 3))

# op _004e_power_combination_eval
# LANG: _004d --> _004f
# SHAPES: (2, 8100, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v144__004f = (v143__004d)
v144__004f = (v144__004f*_004e_coeff).reshape((2, 8100, 3))

# op _004y expand_array_eval
# LANG: _004x --> _004z
# SHAPES: (2, 8100) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v154__004z = np.einsum('ab,c->abc', v153__004x.reshape((2, 8100)) ,np.ones((3,))).reshape((2, 8100, 3))

# op _005d_power_combination_eval
# LANG: _005c --> _005e
# SHAPES: (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v175__005e = (v174__005c**-1)
v175__005e = v175__005e.reshape((2, 8100))

# op _005j_linear_combination_eval
# LANG: _005g, _005i --> _005k
# SHAPES: (2, 8100), (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v178__005k = v176__005g+v177__005i

# op _0011_power_combination_eval
# LANG: _0010 --> _0012
# SHAPES: (2, 9, 10) --> (2, 9, 10)
# full namespace: ComputeNormals
v34__0012 = (v33__0010**0.5)
v34__0012 = v34__0012.reshape((2, 9, 10))

# op _0018_decompose_eval
# LANG: surface_bound_vtx_coords --> _001g, _0019, _001a, _001d, _001l, _001m, _001p
# SHAPES: (2, 10, 11, 3) --> (2, 9, 10, 3), (2, 9, 10, 3), (2, 9, 10, 3), (2, 9, 10, 3), (2, 9, 10, 3), (2, 9, 10, 3), (2, 9, 10, 3)
# full namespace: GeometricPropertyExtraction
v38__0019 = ((v193_surface_bound_vtx_coords.flatten())[src_indices__0019__0018]).reshape((2, 9, 10, 3))
v39__001a = ((v193_surface_bound_vtx_coords.flatten())[src_indices__001a__0018]).reshape((2, 9, 10, 3))
v41__001d = ((v193_surface_bound_vtx_coords.flatten())[src_indices__001d__0018]).reshape((2, 9, 10, 3))
v43__001g = ((v193_surface_bound_vtx_coords.flatten())[src_indices__001g__0018]).reshape((2, 9, 10, 3))
v46__001l = ((v193_surface_bound_vtx_coords.flatten())[src_indices__001l__0018]).reshape((2, 9, 10, 3))
v47__001m = ((v193_surface_bound_vtx_coords.flatten())[src_indices__001m__0018]).reshape((2, 9, 10, 3))
v49__001p = ((v193_surface_bound_vtx_coords.flatten())[src_indices__001p__0018]).reshape((2, 9, 10, 3))

# op _001X_power_combination_eval
# LANG: _001E --> _001Y
# SHAPES: (2, 9, 10, 3) --> (2, 9, 10, 3)
# full namespace: GeometricPropertyExtraction
v69__001Y = (v57__001E)
v69__001Y = (v69__001Y*_001X_coeff).reshape((2, 9, 10, 3))

# op _001Z_power_combination_eval
# LANG: _001M --> _001_
# SHAPES: (2, 9, 10, 3) --> (2, 9, 10, 3)
# full namespace: GeometricPropertyExtraction
v70__001_ = (v62__001M)
v70__001_ = (v70__001_*_001Z_coeff).reshape((2, 9, 10, 3))

# op _004A_power_combination_eval
# LANG: _004z, _004f --> _004B
# SHAPES: (2, 8100, 3), (2, 8100, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v155__004B = (v154__004z)*(v144__004f)
v155__004B = v155__004B.reshape((2, 8100, 3))

# op _004E_power_combination_eval
# LANG: _004D --> _004F
# SHAPES: (2, 8100, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v157__004F = (v156__004D)
v157__004F = (v157__004F*_004E_coeff).reshape((2, 8100, 3))

# op _004Y expand_array_eval
# LANG: _004X --> _004Z
# SHAPES: (2, 8100) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v167__004Z = np.einsum('ab,c->abc', v166__004X.reshape((2, 8100)) ,np.ones((3,))).reshape((2, 8100, 3))

# op _0051 cross_product_eval
# LANG: _003G, _002J --> _0052
# SHAPES: (2, 8100, 3), (2, 8100, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v169__0052 = np.cross(v126__003G, v96__002J, axisa = 2, axisb = 2, axisc = 2)

# op _005l_power_combination_eval
# LANG: _005e, _005k --> _005m
# SHAPES: (2, 8100), (2, 8100) --> (2, 8100)
# full namespace: SubAicBiotSavarts
v179__005m = (v175__005e)*(v178__005k)
v179__005m = v179__005m.reshape((2, 8100))

# op _005r_linear_combination_eval
# LANG: _004b --> _005s
# SHAPES: (2, 8100, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v182__005s = v142__004b

# op _0013 expand_array_eval
# LANG: _0012 --> _0014
# SHAPES: (2, 9, 10) --> (2, 9, 10, 3)
# full namespace: ComputeNormals
v35__0014 = np.einsum('abc,d->abcd', v34__0012.reshape((2, 9, 10)) ,np.ones((3,))).reshape((2, 9, 10, 3))

# op _001n_linear_combination_eval
# LANG: _001l, _001m --> _001o
# SHAPES: (2, 9, 10, 3), (2, 9, 10, 3) --> (2, 9, 10, 3)
# full namespace: GeometricPropertyExtraction
v48__001o = v46__001l+-1*v47__001m

# op _001q_linear_combination_eval
# LANG: _001p, _001g --> _001r
# SHAPES: (2, 9, 10, 3), (2, 9, 10, 3) --> (2, 9, 10, 3)
# full namespace: GeometricPropertyExtraction
v50__001r = v49__001p+-1*v43__001g

# op _0020_linear_combination_eval
# LANG: _001Y, _001_ --> _0021
# SHAPES: (2, 9, 10, 3), (2, 9, 10, 3) --> (2, 9, 10, 3)
# full namespace: GeometricPropertyExtraction
v71__0021 = v69__001Y+v70__001_

# op _0022_power_combination_eval
# LANG: _001H --> _0023
# SHAPES: (2, 9, 10, 3) --> (2, 9, 10, 3)
# full namespace: GeometricPropertyExtraction
v72__0023 = (v59__001H)
v72__0023 = (v72__0023*_0022_coeff).reshape((2, 9, 10, 3))

# op _004__power_combination_eval
# LANG: _004Z, _004F --> _0050
# SHAPES: (2, 8100, 3), (2, 8100, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v168__0050 = (v167__004Z)*(v157__004F)
v168__0050 = v168__0050.reshape((2, 8100, 3))

# op _0053_power_combination_eval
# LANG: _0052 --> _0054
# SHAPES: (2, 8100, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v170__0054 = (v169__0052)
v170__0054 = (v170__0054*_0053_coeff).reshape((2, 8100, 3))

# op _005n expand_array_eval
# LANG: _005m --> _005o
# SHAPES: (2, 8100) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v180__005o = np.einsum('ab,c->abc', v179__005m.reshape((2, 8100)) ,np.ones((3,))).reshape((2, 8100, 3))

# op _005t_linear_combination_eval
# LANG: _005s, _004B --> _005u
# SHAPES: (2, 8100, 3), (2, 8100, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v183__005u = v182__005s+v155__004B

# op _0015_power_combination_eval
# LANG: _000X, _0014 --> surface_normals
# SHAPES: (2, 9, 10, 3), (2, 9, 10, 3) --> (2, 9, 10, 3)
# full namespace: ComputeNormals
v189_surface_normals = (v31__000X)*(v35__0014**-1)
v189_surface_normals = v189_surface_normals.reshape((2, 9, 10, 3))

# op _001s cross_product_eval
# LANG: _001o, _001r --> _001t
# SHAPES: (2, 9, 10, 3), (2, 9, 10, 3) --> (2, 9, 10, 3)
# full namespace: GeometricPropertyExtraction
v51__001t = np.cross(v48__001o, v50__001r, axisa = 3, axisb = 3, axisc = 3)

# op _0024_linear_combination_eval
# LANG: _0021, _0023 --> _0025
# SHAPES: (2, 9, 10, 3), (2, 9, 10, 3) --> (2, 9, 10, 3)
# full namespace: GeometricPropertyExtraction
v73__0025 = v71__0021+-1*v72__0023

# op _0026_power_combination_eval
# LANG: _001R --> _0027
# SHAPES: (2, 9, 10, 3) --> (2, 9, 10, 3)
# full namespace: GeometricPropertyExtraction
v74__0027 = (v65__001R)
v74__0027 = (v74__0027*_0026_coeff).reshape((2, 9, 10, 3))

# op _005p_power_combination_eval
# LANG: _005o, _0054 --> _005q
# SHAPES: (2, 8100, 3), (2, 8100, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v181__005q = (v180__005o)*(v170__0054)
v181__005q = v181__005q.reshape((2, 8100, 3))

# op _005v_linear_combination_eval
# LANG: _005u, _0050 --> _005w
# SHAPES: (2, 8100, 3), (2, 8100, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v184__005w = v183__005u+v168__0050

# op _0005 expand_array_eval
# LANG: frame_vel --> _0006
# SHAPES: (2, 3) --> (2, 90, 3)
# full namespace: 
v2__0006 = np.einsum('ac,b->abc', v192_frame_vel.reshape((2, 3)) ,np.ones((90,))).reshape((2, 90, 3))

# op _001F_power_combination_eval
# LANG: _001E --> _001G
# SHAPES: (2, 9, 10, 3) --> (2, 9, 10, 3)
# full namespace: GeometricPropertyExtraction
v58__001G = (v57__001E)
v58__001G = (v58__001G*_001F_coeff).reshape((2, 9, 10, 3))

# op _001I_power_combination_eval
# LANG: _001H --> _001J
# SHAPES: (2, 9, 10, 3) --> (2, 9, 10, 3)
# full namespace: GeometricPropertyExtraction
v60__001J = (v59__001H)
v60__001J = (v60__001J*_001I_coeff).reshape((2, 9, 10, 3))

# op _001b_linear_combination_eval
# LANG: _0019, _001a --> _001c
# SHAPES: (2, 9, 10, 3), (2, 9, 10, 3) --> (2, 9, 10, 3)
# full namespace: GeometricPropertyExtraction
v40__001c = v38__0019+v39__001a

# op _001u_power_combination_eval
# LANG: _001t --> _001v
# SHAPES: (2, 9, 10, 3) --> (2, 9, 10, 3)
# full namespace: GeometricPropertyExtraction
v52__001v = (v51__001t**2)
v52__001v = v52__001v.reshape((2, 9, 10, 3))

# op _0028_linear_combination_eval
# LANG: _0025, _0027 --> _0029
# SHAPES: (2, 9, 10, 3), (2, 9, 10, 3) --> (2, 9, 10, 3)
# full namespace: GeometricPropertyExtraction
v75__0029 = v73__0025+-1*v74__0027

# op _005E reshape_eval
# LANG: surface_normals --> _005F
# SHAPES: (2, 9, 10, 3) --> (2, 90, 3)
# full namespace: ProjectionAic
v190__005F = v189_surface_normals.reshape((2, 90, 3))

# op _005x_linear_combination_eval
# LANG: _005w, _005q --> _005y
# SHAPES: (2, 8100, 3), (2, 8100, 3) --> (2, 8100, 3)
# full namespace: SubAicBiotSavarts
v185__005y = v184__005w+v181__005q

# op _0007_linear_combination_eval
# LANG: _0006 --> surface_kinematic_vel
# SHAPES: (2, 90, 3) --> (2, 90, 3)
# full namespace: 
v79_surface_kinematic_vel = -1*v2__0006

# op _001K_linear_combination_eval
# LANG: _001G, _001J --> _001L
# SHAPES: (2, 9, 10, 3), (2, 9, 10, 3) --> (2, 9, 10, 3)
# full namespace: GeometricPropertyExtraction
v61__001L = v58__001G+v60__001J

# op _001N_power_combination_eval
# LANG: _001M --> _001O
# SHAPES: (2, 9, 10, 3) --> (2, 9, 10, 3)
# full namespace: GeometricPropertyExtraction
v63__001O = (v62__001M)
v63__001O = (v63__001O*_001N_coeff).reshape((2, 9, 10, 3))

# op _001e_linear_combination_eval
# LANG: _001d, _001c --> _001f
# SHAPES: (2, 9, 10, 3), (2, 9, 10, 3) --> (2, 9, 10, 3)
# full namespace: GeometricPropertyExtraction
v42__001f = v40__001c+v41__001d

# op _001w_single_tensor_sum_with_axis_eval
# LANG: _001v --> _001x
# SHAPES: (2, 9, 10, 3) --> (2, 9, 10)
# full namespace: GeometricPropertyExtraction
v53__001x = np.sum(v52__001v, axis = (3,)).reshape((2, 9, 10))

# op _002a reshape_eval
# LANG: _0029 --> _002b
# SHAPES: (2, 9, 10, 3) --> (2, 90, 3)
# full namespace: GeometricPropertyExtraction
v76__002b = v75__0029.reshape((2, 90, 3))

# op _002i reshape_eval
# LANG: surface_normals --> _002j
# SHAPES: (2, 9, 10, 3) --> (2, 90, 3)
# full namespace: Projection
v81__002j = v189_surface_normals.reshape((2, 90, 3))

# op _005G_indexed_passthrough_eval
# LANG: _005F --> normal_concatenated_aic_projection
# SHAPES: (2, 90, 3) --> (2, 90, 3)
# full namespace: ProjectionAic
v187_normal_concatenated_aic_projection__temp[i_v190__005F__005G_indexed_passthrough_eval] = v190__005F.flatten()
v187_normal_concatenated_aic_projection = v187_normal_concatenated_aic_projection__temp.copy()

# op _005z reshape_eval
# LANG: _005y --> aic
# SHAPES: (2, 8100, 3) --> (2, 90, 90, 3)
# full namespace: SubAicBiotSavarts
v188_aic = v185__005y.reshape((2, 90, 90, 3))

# op _000n reshape_eval
# LANG: M_reshaped --> _000o
# SHAPES: (2, 90, 90) --> (2, 90, 90)
# full namespace: 
v9__000o = v7_M_reshaped.reshape((2, 90, 90))

# op _001P_linear_combination_eval
# LANG: _001L, _001O --> _001Q
# SHAPES: (2, 9, 10, 3), (2, 9, 10, 3) --> (2, 9, 10, 3)
# full namespace: GeometricPropertyExtraction
v64__001Q = v61__001L+v63__001O

# op _001S_power_combination_eval
# LANG: _001R --> _001T
# SHAPES: (2, 9, 10, 3) --> (2, 9, 10, 3)
# full namespace: GeometricPropertyExtraction
v66__001T = (v65__001R)
v66__001T = (v66__001T*_001S_coeff).reshape((2, 9, 10, 3))

# op _001h_linear_combination_eval
# LANG: _001g, _001f --> _001i
# SHAPES: (2, 9, 10, 3), (2, 9, 10, 3) --> (2, 9, 10, 3)
# full namespace: GeometricPropertyExtraction
v44__001i = v42__001f+v43__001g

# op _001y_power_combination_eval
# LANG: _001x --> _001z
# SHAPES: (2, 9, 10) --> (2, 9, 10)
# full namespace: GeometricPropertyExtraction
v54__001z = (v53__001x**0.5)
v54__001z = v54__001z.reshape((2, 9, 10))

# op _002c_linear_combination_eval
# LANG: _002b --> _002d
# SHAPES: (2, 90, 3) --> (2, 90, 3)
# full namespace: GeometricPropertyExtraction
v77__002d = -1*v76__002b

# op _002k_power_combination_eval
# LANG: _002j, surface_kinematic_vel --> _002l
# SHAPES: (2, 90, 3), (2, 90, 3) --> (2, 90, 3)
# full namespace: Projection
v82__002l = (v79_surface_kinematic_vel)*(v81__002j)
v82__002l = v82__002l.reshape((2, 90, 3))

# op _005H einsum_eval
# LANG: normal_concatenated_aic_projection, aic --> aic_projection
# SHAPES: (2, 90, 3), (2, 90, 90, 3) --> (2, 90, 90)
# full namespace: ProjectionAic
v191_aic_projection = np.einsum('lijk,ljk->lij' , v188_aic, v187_normal_concatenated_aic_projection)

# op _000p_linear_combination_eval
# LANG: _000o, aic_projection --> MTX
# SHAPES: (2, 90, 90), (2, 90, 90) --> (2, 90, 90)
# full namespace: 
v10_MTX = v191_aic_projection+v9__000o

# op _001A_power_combination_eval
# LANG: _001z --> surface_panel_areas
# SHAPES: (2, 9, 10) --> (2, 9, 10)
# full namespace: GeometricPropertyExtraction
v55_surface_panel_areas = (v54__001z)
v55_surface_panel_areas = (v55_surface_panel_areas*_001A_coeff).reshape((2, 9, 10))

# op _001U_linear_combination_eval
# LANG: _001Q, _001T --> surface_force_evaluation_pts
# SHAPES: (2, 9, 10, 3), (2, 9, 10, 3) --> (2, 9, 10, 3)
# full namespace: GeometricPropertyExtraction
v67_surface_force_evaluation_pts = v64__001Q+v66__001T

# op _001j_power_combination_eval
# LANG: _001i --> surface_collocation_points
# SHAPES: (2, 9, 10, 3) --> (2, 9, 10, 3)
# full namespace: GeometricPropertyExtraction
v45_surface_collocation_points = (v44__001i)
v45_surface_collocation_points = (v45_surface_collocation_points*_001j_coeff).reshape((2, 9, 10, 3))

# op _002e_indexed_passthrough_eval
# LANG: _002d --> bound_vecs_all_surfaces
# SHAPES: (2, 90, 3) --> (2, 90, 3)
# full namespace: GeometricPropertyExtraction
v68_bound_vecs_all_surfaces__temp[i_v77__002d__002e_indexed_passthrough_eval] = v77__002d.flatten()
v68_bound_vecs_all_surfaces = v68_bound_vecs_all_surfaces__temp.copy()

# op _002m_single_tensor_sum_with_axis_eval
# LANG: _002l --> rhs
# SHAPES: (2, 90, 3) --> (2, 90)
# full namespace: Projection
v83_rhs = np.sum(v82__002l, axis = (2,)).reshape((2, 90))

# op _002o_indexed_passthrough_eval
# LANG: _002j --> normal_concatenated_rhs
# SHAPES: (2, 90, 3) --> (2, 90, 3)
# full namespace: Projection
v78_normal_concatenated_rhs__temp[i_v81__002j__002o_indexed_passthrough_eval] = v81__002j.flatten()
v78_normal_concatenated_rhs = v78_normal_concatenated_rhs__temp.copy()