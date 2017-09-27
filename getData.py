import matplotlib.pyplot as plt
from math import exp

def readData(fn, vth, amp):
	with open(fn, 'r') as f:
		lines = f.readlines()

	vds = float(fn.split('_')[2])
	vbg = float(fn.split('_')[4])
	start = False
	valid = False
	vtglst = []
	idlst = []
	idx = 0
	for l in lines:
		idx = (idx % 8) + 1
		if (l == 'Data {\n'):
			start = True
			idx = 0
		if l == '}':
			start = False
		if start:
			if idx == 3:
				vtg = float(l.split()[4])
				if len(vtglst) == 0 or vtg > vtglst[-1]:
					vtglst.append(vtg)
					valid = True
			if idx == 6:
				idtotal = float(l.split()[2])
				# print(l.split()[2])
				# print(idtotal)
				# idtotal = idtotal * vds * amp if idtotal > vth else 0 
				idtotal = exp(idtotal * vds * amp - vth * vds * amp) - 1
				if valid:
					valid = False
					idlst.append(idtotal)

	return (vds, vbg, vtglst, idlst)


if __name__ == "__main__":
	vds, vbg, vtglst, idlst = readData('TransiXOR/D2/IV_Vds_0.4_Vbg_0.2_n3_des.plt', 1.5e-11, 1e11)
	print("{}, {}".format(vds, vbg))
	print(idlst)   
	plt.plot(vtglst, idlst)
	plt.show()