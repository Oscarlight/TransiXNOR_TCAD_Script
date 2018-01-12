import matplotlib.pyplot as plt
from math import exp

def readData_AC(fn):
	with open(fn, 'r') as f:
		lines = f.readlines()

	vds = float(fn.split('_')[3])
	vbg = float(fn.split('_')[5])
	start = False
	valid = False
	vtglst = []
	cddlst = []
	cdslst = []
	cdglst = []
	cdblst = []
	csdlst = []
	csslst = []
	csglst = []
	csblst = []
	cgdlst = []
	cgslst = []
	cgglst = []
	cgblst = []
	cbdlst = []
	cbslst = []
	cbglst = []
	cbblst = []
	idx = 0
	for l in lines:
		idx = (idx % 9) + 1
		if (l == 'Data {\n'):
			start = True
			idx = 0
		if l == '}':
			start = False
		if start:
			if idx == 2:
				vtg = float(l.split()[2])
				if len(vtglst) == 0 or vtg > vtglst[-1]:
					vtglst.append(vtg)
					valid = True
			if idx == 3:
				cdd = float(l.split()[0])*1e15
				cds = float(l.split()[2])*1e15
				cdg = float(l.split()[4])*1e15
				if valid:
					cddlst.append(cdd)
					cdslst.append(cds)
					cdglst.append(cdg)
			if idx == 4:
				cdb = float(l.split()[1])*1e15
				csd = float(l.split()[3])*1e15
				if valid:
					cdblst.append(cdb)
					csdlst.append(csd)
			if idx == 5:
				css = float(l.split()[0])*1e15
				csg = float(l.split()[2])*1e15
				csb = float(l.split()[4])*1e15
				if valid:
					csslst.append(css)
					csglst.append(csg)
					csblst.append(csb)
			if idx == 6:
				cgd = float(l.split()[1])*1e15
				cgs = float(l.split()[3])*1e15
				if valid:
					cgdlst.append(cgd)
					cgslst.append(cgs)
			if idx == 7:
				cgg = float(l.split()[0])*1e15
				cgb = float(l.split()[2])*1e15
				cbd = float(l.split()[4])*1e15
				if valid:
					cgglst.append(cgg)
					cgblst.append(cgb)
					cbdlst.append(cbd)
			if idx == 8:
				cbs = float(l.split()[1])*1e15
				cbg = float(l.split()[3])*1e15
				if valid:
					cbslst.append(cbs)
					cbglst.append(cbg)
			if idx == 9:
				cbb = float(l.split()[0])*1e15
				if valid:
					valid = False
					cbblst.append(cbb)

	return (vds, vbg, vtglst, cddlst, cdslst, cdglst, cdblst, csdlst, csslst,
			csglst, csblst, cgdlst, cgslst, cgglst, cgblst, cbdlst, cbslst, cbglst, cbblst)


if __name__ == "__main__":
	vds, vbg, vtglst, cddlst, cdslst, cdglst, cdblst, csdlst, csslst, \
	csglst, csblst, cgdlst, cgslst, cgglst, cgblst, cbdlst, cbslst, cbglst, cbblst\
		= readData_AC('D2wSDgate/D2_AC/IV_Vds_0.40_Vbg_0.00_n3_ac_des.plt')
	# print('vds, vbg = ', "{}, {}".format(vds, vbg))
	# print('vtglst:', vtglst)
	# print('cdd:', cddlst)
	# print('cds:', cdslst)
	# print('cdb:', cdblst)
	# print('css:', csslst)
	# print('csb:', csblst)
	print('cgd:', cgdlst)
	# print('cgs:', cgslst)
	# print('cgg:', cgglst)
	# print('cgb:', cgblst)
	# print('cbb:', cbblst)
	# plt.plot(vtglst, cgglst)
	# plt.savefig('Vds_0.0_Vbg_0.0.pdf')
	# plt.show()