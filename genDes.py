from numpy import linspace

fileNames = []
# prevent skip Vtg = 0, topGate start from -0.01 in the .cmd file
vlst = linspace(0, 0.4, 41)
# print(vlst)
vol = [[(vds, vbg) for vbg in vlst] for vds in vlst]
Vtg = 0.40
step = 0.015
with open('batchRun_AC.txt', 'a') as outputfile:
	for vl in vol:
		for Vds, Vbg in vl:  
			comVds =  "Quasistationary( InitialStep= 5e-2 Increment= 1.25 \n Minstep= 1e-5 MaxStep= " \
			          + str(Vds + step) + " \n Goal{ Parameter=vd.dc Voltage = " + str('%.2f' % Vds) \
			          + " }) \n { Coupled{ Poisson Electron Hole } }\n"

			comVbg =  "Quasistationary( InitialStep= 5e-2 Increment= 1.25 \n Minstep= 1e-5 MaxStep= " \
			          + str(Vbg + step) + " \n Goal{ Parameter=vb.dc Voltage = " + str('%.2f' % Vbg) \
			          + " }) \n { Coupled{ Poisson Electron Hole } }\n"

			genFile =  "NewCurrentFile=\"IV_Vds_{}_Vbg_{}_\"\n".format('%.2f' % Vds, '%.2f' % Vbg)

			fileNames.append("IV_Vds_{}_Vbg_{}_trans_n3_des.plt".format('%.2f' % Vds, '%.2f' % Vbg))

			comVtg =  "Quasistationary( InitialStep= 5e-2 Increment= 1.25 \n Minstep= 1e-5 MaxStep= " \
			         + str(step) + "\n Goal{ Parameter=vg.dc  Voltage= " + str('%.2f' % Vtg) \
			         # + " }) \n { ACCoupled ( \n StartFrequency=1e7 EndFrequency=1e7 \n " \
					 # + "NumberOfPoints=1 Decade \n Node (d s g b) Exclude (vd vs vg vb) \n ) \n " \
					 # + "{ Poisson Electron Hole } }\n"
					 + " }) \n { Coupled{ Poisson Electron Hole } }\n"

			reset =  "Quasistationary( InitialStep= 5e-2 Increment= 1.25 \n Minstep= 1e-5 MaxStep= " \
			         + str(0.40) + "\n Goal{ Parameter=vg.dc  Voltage= " + str('%.2f' % 0.00) \
			         + " }) \n { Coupled{ Poisson Electron Hole } }\n"

			line = "# --------------------------------------------------------------------\n"
			# outputfile.write(comVds + comVbg + genFile + comVtg + reset + line + '\n')

## write move.sh

pwd = "/home/ml888/sentaurus_home/XOR/TransiXOR/"

with open("move_trans.sh", 'a') as bash:
	for fn in fileNames:
		bash.write('mv ' + pwd + fn + ' ./D2_w_SDgate/' + fn + '\n')
