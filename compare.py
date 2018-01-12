import os
from getData import readData
from getData_AC import readData_AC
from numpy import array
from numpy import save, load
import numpy as np
import matplotlib.pyplot as plt

# Cds = load("vds_vbg_vtg_Cds_D2_AC.npy")
# Cdg = load("vds_vbg_vtg_Cdg_D2_AC.npy")
# Cdb = load("vds_vbg_vtg_Cdb_D2_AC.npy")
# Csd = load("vds_vbg_vtg_Csd_D2_AC.npy")
# Csg = load("vds_vbg_vtg_Csg_D2_AC.npy")
# Csb = load("vds_vbg_vtg_Csb_D2_AC.npy")
Cgd = load("vds_vbg_vtg_Cgd_D2_AC_w_SDgate.npy")
# Cgs = load("vds_vbg_vtg_Cgs_D2_AC.npy")
# Cgb = load("vds_vbg_vtg_Cgb_D2_AC.npy")
# Cbd = load("vds_vbg_vtg_Cbd_D2_AC.npy")
# Cbs = load("vds_vbg_vtg_Cbs_D2_AC.npy")
# Cbg = load("vds_vbg_vtg_Cbg_D2_AC.npy")

# print("Cds:",Cds[40,0,:])
# print("Csd:",Csd[40,0,:])
# # print(Cds.shape)
# print(np.allclose(Cds[40,0,:], Csd[40,0,:], atol=1e-30))
#
# i = 0
# while i<67:
#     if np.allclose(Cds[40,0,i], Csd[40,0,i], atol=1e-30)==False :
#         print("Cds[", i, "] is not equal to Csd!")
#         print("Cds:",Cds[40,0,i])
#         print("Csd:",Csd[40,0,i])
#     i = i+1
# elif np.array_equal(Cdg, Cgd)==False :
#     print("Cdg is not equal to Cgd!")
# elif np.array_equal(Cdb, Cbd)==False :
#     print("Cdb is not equal to Cbd!")
# elif np.array_equal(Csg, Cgs)==False :
#     print("Csg is not equal to Cgs!")
# elif np.array_equal(Csb, Cbs)==False :
#     print("Csb is not equal to Csb!")
# elif np.array_equal(Cgb, Cbg)==False :
#     print("Cgb is not equal to Cbg!")
# else:
#     print("All are equal!")
# print("Cgd:", Cgd)
# print(Cgd.shape)
Vds = np.linspace(0, 0.4, 41)
#print(Vds[20])
#Vtg = np.linspace(0,0.4,67)
#print(Vtg[33])
Cgd_lst = Cgd[:, 20, 33]
print(Cgd_lst)
plt.plot(Cgd_lst)
plt.show()