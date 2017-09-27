from numpy import linspace

fileNames = []
# provent skip Vtg = 0, topGate start from -0.01 in the .cmd file
vlst = linspace(0, 0.4, 41)
# print(vlst)
vol = [[(vds, vbg) for vbg in vlst] for vds in vlst]
Vtg = 0.4
step = 0.015
with open('batchRun.txt', 'a') as outputfile:
	for vl in vol:
		for Vds, Vbg in vl:  
			comVds =  "Quasistationary( InitialStep= 5e-2 Increment= 1.25 \n Minstep= 1e-5 MaxStep= " \
			          + str(Vds + step) + " \n Goal{ Name=\"drain\" Voltage = " + str(Vds) \
			          + " }) \n { Coupled{ Poisson Electron Hole } }\n"

			comVbg =  "Quasistationary( InitialStep= 5e-2 Increment= 1.25 \n Minstep= 1e-5 MaxStep= " \
			          + str(Vbg + step) + " \n Goal{ Name=\"bottomGate\" Voltage = " + str(Vbg) \
			          + " }) \n { Coupled{ Poisson Electron Hole } }\n"

			genFile =  "NewCurrentFile=\"IV_Vds_{}_Vbg_{}_\"\n".format(Vds, Vbg)

			fileNames.append("IV_Vds_{}_Vbg_{}_n3_des.plt".format(Vds, Vbg))

			comVtg =  "Quasistationary( InitialStep= 5e-2 Increment= 1.25 \n Minstep= 1e-5 MaxStep= " \
			         + str(step) + "\n Goal{ Name=\"topGate\"  Voltage= " + str(Vtg) \
			         + " }) \n { Coupled{ Poisson Electron Hole } }\n"

			reset =  "Quasistationary( InitialStep= 5e-2 Increment= 1.25 \n Minstep= 1e-5 MaxStep= " \
			         + str(0.4) + "\n Goal{ Name=\"topGate\"  Voltage= " + str(0.0) \
			         + " }) \n { Coupled{ Poisson Electron Hole } }\n"

			line = "# --------------------------------------------------------------------\n"
			#outputfile.write(comVds + comVbg + genFile + comVtg + reset + line + '\n')

## write move.sh

pwd = "/home/ml888/sentaurus_home/XOR/TransiXOR/"

with open("move.sh", 'a') as bash:
	for fn in fileNames:
		bash.write('mv ' + pwd + fn + ' ./TransiXOR/D2/' + fn + '\n')
