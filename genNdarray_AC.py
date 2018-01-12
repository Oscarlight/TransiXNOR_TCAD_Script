import os
from getData import readData
from getData_AC import readData_AC
from numpy import array
from numpy import save, load
import matplotlib.pyplot as plt

# data_dir = 'D2/'
data_dir = 'D2_AC/'
files = os.listdir(data_dir)
# print(len(files) - 1)
vdsset = set()
vbgset = set()
vtgMap = {}
cddMap = {}
cdsMap = {}
cdgMap = {}
cdbMap = {}
csdMap = {}
cssMap = {}
csgMap = {}
csbMap = {}
cgdMap = {}
cgsMap = {}
cggMap = {}
cgbMap = {}
cbdMap = {}
cbsMap = {}
cbgMap = {}
cbbMap = {}
for f in files:
	if 'plt' in f:
		path = data_dir + f
		# print(path)
		vds, vbg, vtglst, cddlst, cdslst, cdglst, cdblst, csdlst, csslst, csglst, csblst, cgdlst, cgslst, cgglst, \
		cgblst, cbdlst, cbslst, cbglst, cbblst = readData_AC(path)
		vdsset.add(vds)
		vbgset.add(vbg)
		# print((vds, vbg))
		vtgMap[(vds, vbg)] = vtglst
		cddMap[(vds, vbg)] = cddlst
		cdsMap[(vds, vbg)] = cdslst
		cdgMap[(vds, vbg)] = cdglst
		cdbMap[(vds, vbg)] = cdblst
		csdMap[(vds, vbg)] = csdlst
		cssMap[(vds, vbg)] = csslst
		csgMap[(vds, vbg)] = csglst
		csbMap[(vds, vbg)] = csblst
		cgdMap[(vds, vbg)] = cgdlst
		cgsMap[(vds, vbg)] = cgslst
		cggMap[(vds, vbg)] = cgglst
		cgbMap[(vds, vbg)] = cgblst
		cbdMap[(vds, vbg)] = cbdlst
		cbsMap[(vds, vbg)] = cbslst
		cbgMap[(vds, vbg)] = cbglst
		cbbMap[(vds, vbg)] = cbblst

vdslst = list(vdsset)
vbglst = list(vbgset)
vdslst.sort()
vbglst.sort()
# print(vdslst)
# print(vbglst)
Cdd_map = []
for vds in vdslst:
	vbg_vtg_map = []
	for vbg in vbglst:
		vbg_vtg_map.append(cddMap[(vds, vbg)])
	Cdd_map.append(vbg_vtg_map)

Cds_map = []
for vds in vdslst:
	vbg_vtg_map = []
	for vbg in vbglst:
		vbg_vtg_map.append(cdsMap[(vds, vbg)])
	Cds_map.append(vbg_vtg_map)

Cdg_map = []
for vds in vdslst:
	vbg_vtg_map = []
	for vbg in vbglst:
		vbg_vtg_map.append(cdgMap[(vds, vbg)])
	Cdg_map.append(vbg_vtg_map)

Cdb_map = []
for vds in vdslst:
	vbg_vtg_map = []
	for vbg in vbglst:
		vbg_vtg_map.append(cdbMap[(vds, vbg)])
	Cdb_map.append(vbg_vtg_map)

Csd_map = []
for vds in vdslst:
	vbg_vtg_map = []
	for vbg in vbglst:
		vbg_vtg_map.append(csdMap[(vds, vbg)])
	Csd_map.append(vbg_vtg_map)

Css_map = []
for vds in vdslst:
	vbg_vtg_map = []
	for vbg in vbglst:
		vbg_vtg_map.append(cssMap[(vds, vbg)])
	Css_map.append(vbg_vtg_map)

Csg_map = []
for vds in vdslst:
	vbg_vtg_map = []
	for vbg in vbglst:
		vbg_vtg_map.append(csgMap[(vds, vbg)])
	Csg_map.append(vbg_vtg_map)

Csb_map = []
for vds in vdslst:
	vbg_vtg_map = []
	for vbg in vbglst:
		vbg_vtg_map.append(csbMap[(vds, vbg)])
	Csb_map.append(vbg_vtg_map)

Cgd_map = []
for vds in vdslst:
	vbg_vtg_map = []
	for vbg in vbglst:
		vbg_vtg_map.append(cgdMap[(vds, vbg)])
	Cgd_map.append(vbg_vtg_map)

Cgs_map = []
for vds in vdslst:
	vbg_vtg_map = []
	for vbg in vbglst:
		vbg_vtg_map.append(cgsMap[(vds, vbg)])
	Cgs_map.append(vbg_vtg_map)

Cgg_map = []
for vds in vdslst:
	vbg_vtg_map = []
	for vbg in vbglst:
		vbg_vtg_map.append(cggMap[(vds, vbg)])
	Cgg_map.append(vbg_vtg_map)

Cgb_map = []
for vds in vdslst:
	vbg_vtg_map = []
	for vbg in vbglst:
		vbg_vtg_map.append(cgbMap[(vds, vbg)])
	Cgb_map.append(vbg_vtg_map)

Cbd_map = []
for vds in vdslst:
	vbg_vtg_map = []
	for vbg in vbglst:
		vbg_vtg_map.append(cbdMap[(vds, vbg)])
	Cbd_map.append(vbg_vtg_map)

Cbs_map = []
for vds in vdslst:
	vbg_vtg_map = []
	for vbg in vbglst:
		vbg_vtg_map.append(cbsMap[(vds, vbg)])
	Cbs_map.append(vbg_vtg_map)

Cbg_map = []
for vds in vdslst:
	vbg_vtg_map = []
	for vbg in vbglst:
		vbg_vtg_map.append(cbgMap[(vds, vbg)])
	Cbg_map.append(vbg_vtg_map)

Cbb_map = []
for vds in vdslst:
	vbg_vtg_map = []
	for vbg in vbglst:
		vbg_vtg_map.append(cbbMap[(vds, vbg)])
	Cbb_map.append(vbg_vtg_map)

# Cdd_map = array(Cdd_map)
# Cds_map = array(Cds_map)
# Cdg_map = array(Cdg_map)
# Cdb_map = array(Cdb_map)
# Csd_map = array(Csd_map)
# Css_map = array(Css_map)
# Csg_map = array(Csd_map)
# Csb_map = array(Csb_map)
# Cgd_map = array(Cgb_map)
# Cgs_map = array(Cgs_map)
# Cgg_map = array(Cgg_map)
# Cgb_map = array(Cgb_map)
# Cbd_map = array(Cbd_map)
# Cbs_map = array(Cbs_map)
# Cbg_map = array(Cbg_map)
# Cbb_map = array(Cbb_map)
# print(vdsAsZ)
save("vds_vbg_vtg_Cdd_D2_AC.npy", Cdd_map)
save("vds_vbg_vtg_Cds_D2_AC.npy", Cds_map)
save("vds_vbg_vtg_Cdg_D2_AC.npy", Cdg_map)
save("vds_vbg_vtg_Cdb_D2_AC.npy", Cdb_map)
save("vds_vbg_vtg_Csd_D2_AC.npy", Csd_map)
save("vds_vbg_vtg_Css_D2_AC.npy", Css_map)
save("vds_vbg_vtg_Csg_D2_AC.npy", Csg_map)
save("vds_vbg_vtg_Csb_D2_AC.npy", Csb_map)
save("vds_vbg_vtg_Cgd_D2_AC.npy", Cgd_map)
save("vds_vbg_vtg_Cgs_D2_AC.npy", Cgs_map)
save("vds_vbg_vtg_Cgg_D2_AC.npy", Cgg_map)
save("vds_vbg_vtg_Cgb_D2_AC.npy", Cgb_map)
save("vds_vbg_vtg_Cbd_D2_AC.npy", Cbd_map)
save("vds_vbg_vtg_Cbs_D2_AC.npy", Cbs_map)
save("vds_vbg_vtg_Cbg_D2_AC.npy", Cbg_map)
save("vds_vbg_vtg_Cbb_D2_AC.npy", Cbb_map)
# J = load("vds_vbg_vtg_Cdd_D2_AC_w_SDgate.npy")
# print(J.shape)

# print(J.shape)
# idx = 40
# I = J[idx, :, :]
# print(I)
# fig, ax = plt.subplots(figsize=(6,6))
# idx/40 scale for Vds (see genData)
# ax.imshow(I, vmin=0, vmax=255*(idx/40), origin='lower', interpolation = 'gaussian')
# ax.imshow(I, origin='lower', interpolation = 'gaussian')
# plt.show()
