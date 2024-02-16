

# RUN_MODEL

# system evaluation block

# op _0006_decompose_eval
# REP:  v01_vtx_pts --> v03__0007, v04__0008, v05__000b, v06__000c
# LANG: vtx_pts --> _0007, _0008, _000b, _000c
# full namespace: ComputeNormal
v03__0007 = ((v01_vtx_pts.flatten())[src_indices__0007__0006]).reshape((1, 9, 10, 3))
v04__0008 = ((v01_vtx_pts.flatten())[src_indices__0008__0006]).reshape((1, 9, 10, 3))
v05__000b = ((v01_vtx_pts.flatten())[src_indices__000b__0006]).reshape((1, 9, 10, 3))
v06__000c = ((v01_vtx_pts.flatten())[src_indices__000c__0006]).reshape((1, 9, 10, 3))

# op _000t_decompose_eval
# REP:  v01_vtx_pts --> v020__000u, v021__000v, v022__000w, v023__000x
# LANG: vtx_pts --> _000u, _000v, _000w, _000x
# full namespace: SubAicBiotSavarts
v020__000u = ((v01_vtx_pts.flatten())[src_indices__000u__000t]).reshape((1, 9, 10, 3))
v021__000v = ((v01_vtx_pts.flatten())[src_indices__000v__000t]).reshape((1, 9, 10, 3))
v022__000w = ((v01_vtx_pts.flatten())[src_indices__000w__000t]).reshape((1, 9, 10, 3))
v023__000x = ((v01_vtx_pts.flatten())[src_indices__000x__000t]).reshape((1, 9, 10, 3))

# op _000y_decompose_eval
# REP:  v02_coll_pts --> v015__000z
# LANG: coll_pts --> _000z
# full namespace: SubAicBiotSavarts
v015__000z = ((v02_coll_pts.flatten())[src_indices__000z__000y]).reshape((1, 9, 5, 3))

# op _0009_linear_combination_eval
# REP:  v03__0007, v04__0008 --> v07__000a
# LANG: _0007, _0008 --> _000a
# full namespace: ComputeNormal
v07__000a = _0009_constant+1*v03__0007+-1*v04__0008

# op _000d_linear_combination_eval
# REP:  v05__000b, v06__000c --> v09__000e
# LANG: _000b, _000c --> _000e
# full namespace: ComputeNormal
v09__000e = _000d_constant+1*v05__000b+-1*v06__000c

# op _000G reshape_eval
# REP:  v020__000u --> v024__000H
# LANG: _000u --> _000H
# full namespace: SubAicBiotSavarts
v024__000H = v020__000u.reshape((1, 90, 3))

# op _000_ reshape_eval
# REP:  v021__000v --> v035__0010
# LANG: _000v --> _0010
# full namespace: SubAicBiotSavarts
v035__0010 = v021__000v.reshape((1, 90, 3))

# op _001j reshape_eval
# REP:  v022__000w --> v057__001k
# LANG: _000w --> _001k
# full namespace: SubAicBiotSavarts
v057__001k = v022__000w.reshape((1, 90, 3))

# op _001D reshape_eval
# REP:  v023__000x --> v079__001E
# LANG: _000x --> _001E
# full namespace: SubAicBiotSavarts
v079__001E = v023__000x.reshape((1, 90, 3))

# op _000A reshape_eval
# REP:  v015__000z --> v016__000B
# LANG: _000z --> _000B
# full namespace: SubAicBiotSavarts
v016__000B = v015__000z.reshape((1, 45, 3))

# op _000U reshape_eval
# REP:  v015__000z --> v031__000V
# LANG: _000z --> _000V
# full namespace: SubAicBiotSavarts
v031__000V = v015__000z.reshape((1, 45, 3))

# op _001d reshape_eval
# REP:  v015__000z --> v053__001e
# LANG: _000z --> _001e
# full namespace: SubAicBiotSavarts
v053__001e = v015__000z.reshape((1, 45, 3))

# op _001x reshape_eval
# REP:  v015__000z --> v075__001y
# LANG: _000z --> _001y
# full namespace: SubAicBiotSavarts
v075__001y = v015__000z.reshape((1, 45, 3))

# op _000f cross_product_eval
# REP:  v07__000a, v09__000e --> v08__000g
# LANG: _000a, _000e --> _000g
# full namespace: ComputeNormal
v08__000g = np.cross(v07__000a, v09__000e, axisa = 3, axisb = 3, axisc = 3)

# op _000I expand_array_eval
# REP:  v024__000H --> v025__000J
# LANG: _000H --> _000J
# full namespace: SubAicBiotSavarts
v025__000J = np.einsum('acd,b->abcd', v024__000H.reshape((1, 90, 3)) ,np.ones((45,))).reshape((1, 45, 90, 3))

# op _0011 expand_array_eval
# REP:  v035__0010 --> v036__0012
# LANG: _0010 --> _0012
# full namespace: SubAicBiotSavarts
v036__0012 = np.einsum('acd,b->abcd', v035__0010.reshape((1, 90, 3)) ,np.ones((45,))).reshape((1, 45, 90, 3))

# op _001l expand_array_eval
# REP:  v057__001k --> v058__001m
# LANG: _001k --> _001m
# full namespace: SubAicBiotSavarts
v058__001m = np.einsum('acd,b->abcd', v057__001k.reshape((1, 90, 3)) ,np.ones((45,))).reshape((1, 45, 90, 3))

# op _001F expand_array_eval
# REP:  v079__001E --> v080__001G
# LANG: _001E --> _001G
# full namespace: SubAicBiotSavarts
v080__001G = np.einsum('acd,b->abcd', v079__001E.reshape((1, 90, 3)) ,np.ones((45,))).reshape((1, 45, 90, 3))

# op _000C expand_array_eval
# REP:  v016__000B --> v017__000D
# LANG: _000B --> _000D
# full namespace: SubAicBiotSavarts
v017__000D = np.einsum('abd,c->abcd', v016__000B.reshape((1, 45, 3)) ,np.ones((90,))).reshape((1, 45, 90, 3))

# op _000W expand_array_eval
# REP:  v031__000V --> v032__000X
# LANG: _000V --> _000X
# full namespace: SubAicBiotSavarts
v032__000X = np.einsum('abd,c->abcd', v031__000V.reshape((1, 45, 3)) ,np.ones((90,))).reshape((1, 45, 90, 3))

# op _001f expand_array_eval
# REP:  v053__001e --> v054__001g
# LANG: _001e --> _001g
# full namespace: SubAicBiotSavarts
v054__001g = np.einsum('abd,c->abcd', v053__001e.reshape((1, 45, 3)) ,np.ones((90,))).reshape((1, 45, 90, 3))

# op _001z expand_array_eval
# REP:  v075__001y --> v076__001A
# LANG: _001y --> _001A
# full namespace: SubAicBiotSavarts
v076__001A = np.einsum('abd,c->abcd', v075__001y.reshape((1, 45, 3)) ,np.ones((90,))).reshape((1, 45, 90, 3))

# op _000h_power_combination_eval
# REP:  v08__000g --> v011__000i
# LANG: _000g --> _000i
# full namespace: ComputeNormal
v011__000i = (v08__000g**2)
v011__000i = (v011__000i*_000h_coeff).reshape((1, 9, 10, 3))

# op _000K reshape_eval
# REP:  v025__000J --> v026__000L
# LANG: _000J --> _000L
# full namespace: SubAicBiotSavarts
v026__000L = v025__000J.reshape((1, 4050, 3))

# op _0013 reshape_eval
# REP:  v036__0012 --> v037__0014
# LANG: _0012 --> _0014
# full namespace: SubAicBiotSavarts
v037__0014 = v036__0012.reshape((1, 4050, 3))

# op _001n reshape_eval
# REP:  v058__001m --> v059__001o
# LANG: _001m --> _001o
# full namespace: SubAicBiotSavarts
v059__001o = v058__001m.reshape((1, 4050, 3))

# op _001H reshape_eval
# REP:  v080__001G --> v081__001I
# LANG: _001G --> _001I
# full namespace: SubAicBiotSavarts
v081__001I = v080__001G.reshape((1, 4050, 3))

# op _000E reshape_eval
# REP:  v017__000D --> v018__000F
# LANG: _000D --> _000F
# full namespace: SubAicBiotSavarts
v018__000F = v017__000D.reshape((1, 4050, 3))

# op _000Y reshape_eval
# REP:  v032__000X --> v033__000Z
# LANG: _000X --> _000Z
# full namespace: SubAicBiotSavarts
v033__000Z = v032__000X.reshape((1, 4050, 3))

# op _001h reshape_eval
# REP:  v054__001g --> v055__001i
# LANG: _001g --> _001i
# full namespace: SubAicBiotSavarts
v055__001i = v054__001g.reshape((1, 4050, 3))

# op _001B reshape_eval
# REP:  v076__001A --> v077__001C
# LANG: _001A --> _001C
# full namespace: SubAicBiotSavarts
v077__001C = v076__001A.reshape((1, 4050, 3))

# op _000j_single_tensor_sum_with_axis_eval
# REP:  v011__000i --> v012__000k
# LANG: _000i --> _000k
# full namespace: ComputeNormal
v012__000k = np.sum(v011__000i, axis = (3,)).reshape((1, 9, 10))

# op _000M_linear_combination_eval
# REP:  v018__000F, v026__000L --> v019__000N
# LANG: _000F, _000L --> _000N
# full namespace: SubAicBiotSavarts
v019__000N = _000M_constant+1*v018__000F+-1*v026__000L

# op _0015_linear_combination_eval
# REP:  v033__000Z, v037__0014 --> v034__0016
# LANG: _000Z, _0014 --> _0016
# full namespace: SubAicBiotSavarts
v034__0016 = _0015_constant+1*v033__000Z+-1*v037__0014

# op _001p_linear_combination_eval
# REP:  v055__001i, v059__001o --> v056__001q
# LANG: _001i, _001o --> _001q
# full namespace: SubAicBiotSavarts
v056__001q = _001p_constant+1*v055__001i+-1*v059__001o

# op _001J_linear_combination_eval
# REP:  v077__001C, v081__001I --> v078__001K
# LANG: _001C, _001I --> _001K
# full namespace: SubAicBiotSavarts
v078__001K = _001J_constant+1*v077__001C+-1*v081__001I

# op _000l_power_combination_eval
# REP:  v012__000k --> v013__000m
# LANG: _000k --> _000m
# full namespace: ComputeNormal
v013__000m = (v012__000k**0.5)
v013__000m = (v013__000m*_000l_coeff).reshape((1, 9, 10))

# op _000O_power_combination_eval
# REP:  v019__000N --> v027__000P
# LANG: _000N --> _000P
# full namespace: SubAicBiotSavarts
v027__000P = (v019__000N**2)
v027__000P = (v027__000P*_000O_coeff).reshape((1, 4050, 3))

# op _0017_power_combination_eval
# REP:  v034__0016 --> v038__0018
# LANG: _0016 --> _0018
# full namespace: SubAicBiotSavarts
v038__0018 = (v034__0016**2)
v038__0018 = (v038__0018*_0017_coeff).reshape((1, 4050, 3))

# op _001V_power_combination_eval
# REP:  v019__000N, v034__0016 --> v042__001W
# LANG: _000N, _0016 --> _001W
# full namespace: SubAicBiotSavarts
v042__001W = (v019__000N**1)*(v034__0016**1)
v042__001W = (v042__001W*_001V_coeff).reshape((1, 4050, 3))

# op _001R cross_product_eval
# REP:  v019__000N, v034__0016 --> v0110__001S
# LANG: _000N, _0016 --> _001S
# full namespace: SubAicBiotSavarts
v0110__001S = np.cross(v019__000N, v034__0016, axisa = 2, axisb = 2, axisc = 2)

# op _001r_power_combination_eval
# REP:  v056__001q --> v060__001s
# LANG: _001q --> _001s
# full namespace: SubAicBiotSavarts
v060__001s = (v056__001q**2)
v060__001s = (v060__001s*_001r_coeff).reshape((1, 4050, 3))

# op _002q_power_combination_eval
# REP:  v034__0016, v056__001q --> v064__002r
# LANG: _0016, _001q --> _002r
# full namespace: SubAicBiotSavarts
v064__002r = (v034__0016**1)*(v056__001q**1)
v064__002r = (v064__002r*_002q_coeff).reshape((1, 4050, 3))

# op _002m cross_product_eval
# REP:  v034__0016, v056__001q --> v0116__002n
# LANG: _0016, _001q --> _002n
# full namespace: SubAicBiotSavarts
v0116__002n = np.cross(v034__0016, v056__001q, axisa = 2, axisb = 2, axisc = 2)

# op _001L_power_combination_eval
# REP:  v078__001K --> v082__001M
# LANG: _001K --> _001M
# full namespace: SubAicBiotSavarts
v082__001M = (v078__001K**2)
v082__001M = (v082__001M*_001L_coeff).reshape((1, 4050, 3))

# op _002W_power_combination_eval
# REP:  v056__001q, v078__001K --> v086__002X
# LANG: _001q, _001K --> _002X
# full namespace: SubAicBiotSavarts
v086__002X = (v056__001q**1)*(v078__001K**1)
v086__002X = (v086__002X*_002W_coeff).reshape((1, 4050, 3))

# op _003r_power_combination_eval
# REP:  v019__000N, v078__001K --> v098__003s
# LANG: _000N, _001K --> _003s
# full namespace: SubAicBiotSavarts
v098__003s = (v078__001K**1)*(v019__000N**1)
v098__003s = (v098__003s*_003r_coeff).reshape((1, 4050, 3))

# op _002S cross_product_eval
# REP:  v056__001q, v078__001K --> v0121__002T
# LANG: _001q, _001K --> _002T
# full namespace: SubAicBiotSavarts
v0121__002T = np.cross(v056__001q, v078__001K, axisa = 2, axisb = 2, axisc = 2)

# op _003n cross_product_eval
# REP:  v019__000N, v078__001K --> v0126__003o
# LANG: _000N, _001K --> _003o
# full namespace: SubAicBiotSavarts
v0126__003o = np.cross(v078__001K, v019__000N, axisa = 2, axisb = 2, axisc = 2)

# op _000n expand_array_eval
# REP:  v013__000m --> v014__000o
# LANG: _000m --> _000o
# full namespace: ComputeNormal
v014__000o = np.einsum('abc,d->abcd', v013__000m.reshape((1, 9, 10)) ,np.ones((3,))).reshape((1, 9, 10, 3))

# op _000Q_single_tensor_sum_with_axis_eval
# REP:  v027__000P --> v028__000R
# LANG: _000P --> _000R
# full namespace: SubAicBiotSavarts
v028__000R = np.sum(v027__000P, axis = (2,)).reshape((1, 4050))

# op _0019_single_tensor_sum_with_axis_eval
# REP:  v038__0018 --> v039__001a
# LANG: _0018 --> _001a
# full namespace: SubAicBiotSavarts
v039__001a = np.sum(v038__0018, axis = (2,)).reshape((1, 4050))

# op _001X_single_tensor_sum_with_axis_eval
# REP:  v042__001W --> v043__001Y
# LANG: _001W --> _001Y
# full namespace: SubAicBiotSavarts
v043__001Y = np.sum(v042__001W, axis = (2,)).reshape((1, 4050))

# op _001T_power_combination_eval
# REP:  v0110__001S --> v0111__001U
# LANG: _001S --> _001U
# full namespace: SubAicBiotSavarts
v0111__001U = (v0110__001S**1)
v0111__001U = (v0111__001U*_001T_coeff).reshape((1, 4050, 3))

# op _001t_single_tensor_sum_with_axis_eval
# REP:  v060__001s --> v061__001u
# LANG: _001s --> _001u
# full namespace: SubAicBiotSavarts
v061__001u = np.sum(v060__001s, axis = (2,)).reshape((1, 4050))

# op _002s_single_tensor_sum_with_axis_eval
# REP:  v064__002r --> v065__002t
# LANG: _002r --> _002t
# full namespace: SubAicBiotSavarts
v065__002t = np.sum(v064__002r, axis = (2,)).reshape((1, 4050))

# op _002o_power_combination_eval
# REP:  v0116__002n --> v0117__002p
# LANG: _002n --> _002p
# full namespace: SubAicBiotSavarts
v0117__002p = (v0116__002n**1)
v0117__002p = (v0117__002p*_002o_coeff).reshape((1, 4050, 3))

# op _001N_single_tensor_sum_with_axis_eval
# REP:  v082__001M --> v083__001O
# LANG: _001M --> _001O
# full namespace: SubAicBiotSavarts
v083__001O = np.sum(v082__001M, axis = (2,)).reshape((1, 4050))

# op _002Y_single_tensor_sum_with_axis_eval
# REP:  v086__002X --> v087__002Z
# LANG: _002X --> _002Z
# full namespace: SubAicBiotSavarts
v087__002Z = np.sum(v086__002X, axis = (2,)).reshape((1, 4050))

# op _003t_single_tensor_sum_with_axis_eval
# REP:  v098__003s --> v099__003u
# LANG: _003s --> _003u
# full namespace: SubAicBiotSavarts
v099__003u = np.sum(v098__003s, axis = (2,)).reshape((1, 4050))

# op _002U_power_combination_eval
# REP:  v0121__002T --> v0122__002V
# LANG: _002T --> _002V
# full namespace: SubAicBiotSavarts
v0122__002V = (v0121__002T**1)
v0122__002V = (v0122__002V*_002U_coeff).reshape((1, 4050, 3))

# op _003p_power_combination_eval
# REP:  v0126__003o --> v0127__003q
# LANG: _003o --> _003q
# full namespace: SubAicBiotSavarts
v0127__003q = (v0126__003o**1)
v0127__003q = (v0127__003q*_003p_coeff).reshape((1, 4050, 3))

# op _000p_power_combination_eval
# REP:  v08__000g, v014__000o --> v010_vtx_pts_normals
# LANG: _000g, _000o --> vtx_pts_normals
# full namespace: ComputeNormal
v010_vtx_pts_normals = (v08__000g**1)*(v014__000o**-1)
v010_vtx_pts_normals = (v010_vtx_pts_normals*_000p_coeff).reshape((1, 9, 10, 3))

# op _000S_power_combination_eval
# REP:  v028__000R --> v029__000T
# LANG: _000R --> _000T
# full namespace: SubAicBiotSavarts
v029__000T = (v028__000R**0.5)
v029__000T = (v029__000T*_000S_coeff).reshape((1, 4050))

# op _001b_power_combination_eval
# REP:  v039__001a --> v040__001c
# LANG: _001a --> _001c
# full namespace: SubAicBiotSavarts
v040__001c = (v039__001a**0.5)
v040__001c = (v040__001c*_001b_coeff).reshape((1, 4050))

# op _001v_power_combination_eval
# REP:  v061__001u --> v062__001w
# LANG: _001u --> _001w
# full namespace: SubAicBiotSavarts
v062__001w = (v061__001u**0.5)
v062__001w = (v062__001w*_001v_coeff).reshape((1, 4050))

# op _001P_power_combination_eval
# REP:  v083__001O --> v084__001Q
# LANG: _001O --> _001Q
# full namespace: SubAicBiotSavarts
v084__001Q = (v083__001O**0.5)
v084__001Q = (v084__001Q*_001P_coeff).reshape((1, 4050))

# op _0047 reshape_eval
# REP:  v010_vtx_pts_normals --> v0130__0048
# LANG: vtx_pts_normals --> _0048
# full namespace: Projection
v0130__0048 = v010_vtx_pts_normals.reshape((1, 90, 3))

# op _0026_linear_combination_eval
# REP:  v029__000T --> v047__0027
# LANG: _000T --> _0027
# full namespace: SubAicBiotSavarts
v047__0027 = _0026_constant+1*v029__000T

# op _003H_linear_combination_eval
# REP:  v029__000T --> v0106__003I
# LANG: _000T --> _003I
# full namespace: SubAicBiotSavarts
v0106__003I = _003H_constant+1*v029__000T

# op _001Z_power_combination_eval
# REP:  v029__000T, v040__001c --> v030__001_
# LANG: _000T, _001c --> _001_
# full namespace: SubAicBiotSavarts
v030__001_ = (v029__000T**1)*(v040__001c**1)
v030__001_ = (v030__001_*_001Z_coeff).reshape((1, 4050))

# op _002a_linear_combination_eval
# REP:  v040__001c --> v050__002b
# LANG: _001c --> _002b
# full namespace: SubAicBiotSavarts
v050__002b = _002a_constant+1*v040__001c

# op _002C_linear_combination_eval
# REP:  v040__001c --> v069__002D
# LANG: _001c --> _002D
# full namespace: SubAicBiotSavarts
v069__002D = _002C_constant+1*v040__001c

# op _002u_power_combination_eval
# REP:  v040__001c, v062__001w --> v052__002v
# LANG: _001c, _001w --> _002v
# full namespace: SubAicBiotSavarts
v052__002v = (v040__001c**1)*(v062__001w**1)
v052__002v = (v052__002v*_002u_coeff).reshape((1, 4050))

# op _002G_linear_combination_eval
# REP:  v062__001w --> v072__002H
# LANG: _001w --> _002H
# full namespace: SubAicBiotSavarts
v072__002H = _002G_constant+1*v062__001w

# op _0037_linear_combination_eval
# REP:  v062__001w --> v091__0038
# LANG: _001w --> _0038
# full namespace: SubAicBiotSavarts
v091__0038 = _0037_constant+1*v062__001w

# op _002__power_combination_eval
# REP:  v062__001w, v084__001Q --> v074__0030
# LANG: _001w, _001Q --> _0030
# full namespace: SubAicBiotSavarts
v074__0030 = (v062__001w**1)*(v084__001Q**1)
v074__0030 = (v074__0030*_002__coeff).reshape((1, 4050))

# op _003b_linear_combination_eval
# REP:  v084__001Q --> v094__003c
# LANG: _001Q --> _003c
# full namespace: SubAicBiotSavarts
v094__003c = _003b_constant+1*v084__001Q

# op _003v_power_combination_eval
# REP:  v029__000T, v084__001Q --> v096__003w
# LANG: _000T, _001Q --> _003w
# full namespace: SubAicBiotSavarts
v096__003w = (v084__001Q**1)*(v029__000T**1)
v096__003w = (v096__003w*_003v_coeff).reshape((1, 4050))

# op _003D_linear_combination_eval
# REP:  v084__001Q --> v0103__003E
# LANG: _001Q --> _003E
# full namespace: SubAicBiotSavarts
v0103__003E = _003D_constant+1*v084__001Q

# op _0049_indexed_passthrough_eval
# REP:  v0130__0048 --> v0131_normal_concatenated_aic_projection
# LANG: _0048 --> normal_concatenated_aic_projection
# full namespace: Projection
v0131_normal_concatenated_aic_projection__temp[i_v0130__0048__0049_indexed_passthrough_eval] = v0130__0048.flatten()
v0131_normal_concatenated_aic_projection = v0131_normal_concatenated_aic_projection__temp.copy()

# op _0028_power_combination_eval
# REP:  v047__0027 --> v048__0029
# LANG: _0027 --> _0029
# full namespace: SubAicBiotSavarts
v048__0029 = (v047__0027**-1)
v048__0029 = (v048__0029*_0028_coeff).reshape((1, 4050))

# op _003J_power_combination_eval
# REP:  v0106__003I --> v0107__003K
# LANG: _003I --> _003K
# full namespace: SubAicBiotSavarts
v0107__003K = (v0106__003I**-1)
v0107__003K = (v0107__003K*_003J_coeff).reshape((1, 4050))

# op _0020_linear_combination_eval
# REP:  v030__001_, v043__001Y --> v041__0021
# LANG: _001_, _001Y --> _0021
# full namespace: SubAicBiotSavarts
v041__0021 = _0020_constant+1*v030__001_+1*v043__001Y

# op _002c_power_combination_eval
# REP:  v050__002b --> v051__002d
# LANG: _002b --> _002d
# full namespace: SubAicBiotSavarts
v051__002d = (v050__002b**-1)
v051__002d = (v051__002d*_002c_coeff).reshape((1, 4050))

# op _002E_power_combination_eval
# REP:  v069__002D --> v070__002F
# LANG: _002D --> _002F
# full namespace: SubAicBiotSavarts
v070__002F = (v069__002D**-1)
v070__002F = (v070__002F*_002E_coeff).reshape((1, 4050))

# op _002w_linear_combination_eval
# REP:  v052__002v, v065__002t --> v063__002x
# LANG: _002v, _002t --> _002x
# full namespace: SubAicBiotSavarts
v063__002x = _002w_constant+1*v052__002v+1*v065__002t

# op _002I_power_combination_eval
# REP:  v072__002H --> v073__002J
# LANG: _002H --> _002J
# full namespace: SubAicBiotSavarts
v073__002J = (v072__002H**-1)
v073__002J = (v073__002J*_002I_coeff).reshape((1, 4050))

# op _0039_power_combination_eval
# REP:  v091__0038 --> v092__003a
# LANG: _0038 --> _003a
# full namespace: SubAicBiotSavarts
v092__003a = (v091__0038**-1)
v092__003a = (v092__003a*_0039_coeff).reshape((1, 4050))

# op _0031_linear_combination_eval
# REP:  v074__0030, v087__002Z --> v085__0032
# LANG: _0030, _002Z --> _0032
# full namespace: SubAicBiotSavarts
v085__0032 = _0031_constant+1*v074__0030+1*v087__002Z

# op _003d_power_combination_eval
# REP:  v094__003c --> v095__003e
# LANG: _003c --> _003e
# full namespace: SubAicBiotSavarts
v095__003e = (v094__003c**-1)
v095__003e = (v095__003e*_003d_coeff).reshape((1, 4050))

# op _003x_linear_combination_eval
# REP:  v096__003w, v099__003u --> v097__003y
# LANG: _003w, _003u --> _003y
# full namespace: SubAicBiotSavarts
v097__003y = _003x_constant+1*v096__003w+1*v099__003u

# op _003F_power_combination_eval
# REP:  v0103__003E --> v0104__003G
# LANG: _003E --> _003G
# full namespace: SubAicBiotSavarts
v0104__003G = (v0103__003E**-1)
v0104__003G = (v0104__003G*_003F_coeff).reshape((1, 4050))

# op _0022_linear_combination_eval
# REP:  v041__0021 --> v044__0023
# LANG: _0021 --> _0023
# full namespace: SubAicBiotSavarts
v044__0023 = _0022_constant+1*v041__0021

# op _002e_linear_combination_eval
# REP:  v048__0029, v051__002d --> v049__002f
# LANG: _0029, _002d --> _002f
# full namespace: SubAicBiotSavarts
v049__002f = _002e_constant+1*v048__0029+1*v051__002d

# op _002y_linear_combination_eval
# REP:  v063__002x --> v066__002z
# LANG: _002x --> _002z
# full namespace: SubAicBiotSavarts
v066__002z = _002y_constant+1*v063__002x

# op _002K_linear_combination_eval
# REP:  v070__002F, v073__002J --> v071__002L
# LANG: _002F, _002J --> _002L
# full namespace: SubAicBiotSavarts
v071__002L = _002K_constant+1*v070__002F+1*v073__002J

# op _0033_linear_combination_eval
# REP:  v085__0032 --> v088__0034
# LANG: _0032 --> _0034
# full namespace: SubAicBiotSavarts
v088__0034 = _0033_constant+1*v085__0032

# op _003f_linear_combination_eval
# REP:  v092__003a, v095__003e --> v093__003g
# LANG: _003a, _003e --> _003g
# full namespace: SubAicBiotSavarts
v093__003g = _003f_constant+1*v092__003a+1*v095__003e

# op _003z_linear_combination_eval
# REP:  v097__003y --> v0100__003A
# LANG: _003y --> _003A
# full namespace: SubAicBiotSavarts
v0100__003A = _003z_constant+1*v097__003y

# op _003L_linear_combination_eval
# REP:  v0104__003G, v0107__003K --> v0105__003M
# LANG: _003G, _003K --> _003M
# full namespace: SubAicBiotSavarts
v0105__003M = _003L_constant+1*v0104__003G+1*v0107__003K

# op _0024_power_combination_eval
# REP:  v044__0023 --> v045__0025
# LANG: _0023 --> _0025
# full namespace: SubAicBiotSavarts
v045__0025 = (v044__0023**-1)
v045__0025 = (v045__0025*_0024_coeff).reshape((1, 4050))

# op _002A_power_combination_eval
# REP:  v066__002z --> v067__002B
# LANG: _002z --> _002B
# full namespace: SubAicBiotSavarts
v067__002B = (v066__002z**-1)
v067__002B = (v067__002B*_002A_coeff).reshape((1, 4050))

# op _0035_power_combination_eval
# REP:  v088__0034 --> v089__0036
# LANG: _0034 --> _0036
# full namespace: SubAicBiotSavarts
v089__0036 = (v088__0034**-1)
v089__0036 = (v089__0036*_0035_coeff).reshape((1, 4050))

# op _003B_power_combination_eval
# REP:  v0100__003A --> v0101__003C
# LANG: _003A --> _003C
# full namespace: SubAicBiotSavarts
v0101__003C = (v0100__003A**-1)
v0101__003C = (v0101__003C*_003B_coeff).reshape((1, 4050))

# op _002g_power_combination_eval
# REP:  v045__0025, v049__002f --> v046_num_002h
# LANG: _0025, _002f --> num_002h
# full namespace: SubAicBiotSavarts
v046_num_002h = (v045__0025**1)*(v049__002f**1)
v046_num_002h = (v046_num_002h*_002g_coeff).reshape((1, 4050))

# op _002M_power_combination_eval
# REP:  v067__002B, v071__002L --> v068_num_002N
# LANG: _002B, _002L --> num_002N
# full namespace: SubAicBiotSavarts
v068_num_002N = (v067__002B**1)*(v071__002L**1)
v068_num_002N = (v068_num_002N*_002M_coeff).reshape((1, 4050))

# op _003h_power_combination_eval
# REP:  v089__0036, v093__003g --> v090_num_003i
# LANG: _0036, _003g --> num_003i
# full namespace: SubAicBiotSavarts
v090_num_003i = (v089__0036**1)*(v093__003g**1)
v090_num_003i = (v090_num_003i*_003h_coeff).reshape((1, 4050))

# op _003N_power_combination_eval
# REP:  v0101__003C, v0105__003M --> v0102_num_003O
# LANG: _003C, _003M --> num_003O
# full namespace: SubAicBiotSavarts
v0102_num_003O = (v0101__003C**1)*(v0105__003M**1)
v0102_num_003O = (v0102_num_003O*_003N_coeff).reshape((1, 4050))

# op _002i expand_array_eval
# REP:  v046_num_002h --> v0108__002j
# LANG: num_002h --> _002j
# full namespace: SubAicBiotSavarts
v0108__002j = np.einsum('ab,c->abc', v046_num_002h.reshape((1, 4050)) ,np.ones((3,))).reshape((1, 4050, 3))

# op _002O expand_array_eval
# REP:  v068_num_002N --> v0114__002P
# LANG: num_002N --> _002P
# full namespace: SubAicBiotSavarts
v0114__002P = np.einsum('ab,c->abc', v068_num_002N.reshape((1, 4050)) ,np.ones((3,))).reshape((1, 4050, 3))

# op _003j expand_array_eval
# REP:  v090_num_003i --> v0119__003k
# LANG: num_003i --> _003k
# full namespace: SubAicBiotSavarts
v0119__003k = np.einsum('ab,c->abc', v090_num_003i.reshape((1, 4050)) ,np.ones((3,))).reshape((1, 4050, 3))

# op _003P expand_array_eval
# REP:  v0102_num_003O --> v0124__003Q
# LANG: num_003O --> _003Q
# full namespace: SubAicBiotSavarts
v0124__003Q = np.einsum('ab,c->abc', v0102_num_003O.reshape((1, 4050)) ,np.ones((3,))).reshape((1, 4050, 3))

# op _002k_power_combination_eval
# REP:  v0108__002j, v0111__001U --> v0109__002l
# LANG: _002j, _001U --> _002l
# full namespace: SubAicBiotSavarts
v0109__002l = (v0108__002j**1)*(v0111__001U**1)
v0109__002l = (v0109__002l*_002k_coeff).reshape((1, 4050, 3))

# op _002Q_power_combination_eval
# REP:  v0114__002P, v0117__002p --> v0115__002R
# LANG: _002P, _002p --> _002R
# full namespace: SubAicBiotSavarts
v0115__002R = (v0114__002P**1)*(v0117__002p**1)
v0115__002R = (v0115__002R*_002Q_coeff).reshape((1, 4050, 3))

# op _003l_power_combination_eval
# REP:  v0119__003k, v0122__002V --> v0120__003m
# LANG: _003k, _002V --> _003m
# full namespace: SubAicBiotSavarts
v0120__003m = (v0119__003k**1)*(v0122__002V**1)
v0120__003m = (v0120__003m*_003l_coeff).reshape((1, 4050, 3))

# op _003R_power_combination_eval
# REP:  v0124__003Q, v0127__003q --> v0125__003S
# LANG: _003Q, _003q --> _003S
# full namespace: SubAicBiotSavarts
v0125__003S = (v0124__003Q**1)*(v0127__003q**1)
v0125__003S = (v0125__003S*_003R_coeff).reshape((1, 4050, 3))

# op _003T_linear_combination_eval
# REP:  v0109__002l --> v0112__003U
# LANG: _002l --> _003U
# full namespace: SubAicBiotSavarts
v0112__003U = _003T_constant+1*v0109__002l

# op _003V_linear_combination_eval
# REP:  v0112__003U, v0115__002R --> v0113__003W
# LANG: _003U, _002R --> _003W
# full namespace: SubAicBiotSavarts
v0113__003W = _003V_constant+1*v0112__003U+1*v0115__002R

# op _003X_linear_combination_eval
# REP:  v0113__003W, v0120__003m --> v0118__003Y
# LANG: _003W, _003m --> _003Y
# full namespace: SubAicBiotSavarts
v0118__003Y = _003X_constant+1*v0113__003W+1*v0120__003m

# op _003Z_linear_combination_eval
# REP:  v0118__003Y, v0125__003S --> v0123__003_
# LANG: _003Y, _003S --> _003_
# full namespace: SubAicBiotSavarts
v0123__003_ = _003Z_constant+1*v0118__003Y+1*v0125__003S

# op _0040_custom_explicit_eval
# REP:  v0123__003_ --> v0128_aic_flattened
# LANG: _003_ --> aic_flattened
# full namespace: SubAicBiotSavarts
temp = _0040_custom_explicit_func_aic_flattened.solve(v0123__003_)
v0128_aic_flattened = temp[0].copy()

# op _0042 reshape_eval
# REP:  v0128_aic_flattened --> v0129_aic
# LANG: aic_flattened --> aic
# full namespace: SubAicBiotSavarts
v0129_aic = v0128_aic_flattened.reshape((1, 90, 90, 3))

# op _004a einsum_eval
# REP:  v0131_normal_concatenated_aic_projection, v0129_aic --> v0132_aic_projection
# LANG: normal_concatenated_aic_projection, aic --> aic_projection
# full namespace: Projection
v0132_aic_projection = np.einsum('lijk,lik->lij' , v0129_aic, v0131_normal_concatenated_aic_projection)