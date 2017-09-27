import os
from getData import readData
from numpy import array
from numpy import save, load
import matplotlib.pyplot as plt

data_dir = 'TransiXOR/D2/'
files = os.listdir(data_dir)
print(len(files) - 1)
vdsset = set()
vbgset = set()
idMap = {}
vtgMap = {}
for f in files:
	if 'plt' in f:
		path = data_dir + f
		# print(path)
		vds, vbg, vtglst, idlst = readData(path, 8e-11, 1e11)
		vdsset.add(vds)
		vbgset.add(vbg)
		# print((vds, vbg))
		idMap[(vds, vbg)] = idlst
		vtgMap[(vds, vbg)] = vtglst

vdslst = list(vdsset)
vbglst = list(vbgset)
vdslst.sort()
vbglst.sort()
# print(vdslst)
vdsAsZ = []
for vds in vdslst:
	vbg_vtg_map = []
	for vbg in vbglst:
		vbg_vtg_map.append(idMap[(vds, vbg)])
	vdsAsZ.append(vbg_vtg_map)

vdsAsZ = array(vdsAsZ)

save("vds_vbg_vtg_id_D2.npy", vdsAsZ)
J = load("vds_vbg_vtg_id_D2.npy")

print(J.shape)
idx = 40
I = J[idx, :, :]
fig, ax = plt.subplots(figsize=(6,6))
# idx/40 scale for Vds (see genData)
ax.imshow(I, vmin=0, vmax=255*(idx/40), origin='lower', interpolation = 'gaussian')
plt.show()
