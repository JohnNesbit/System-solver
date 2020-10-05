

def rem_xtra(lest):
	for ii in lest:
		if ii == " " or "":
			lest.remove(ii)
		if ii == "+":
			lest.remove(ii)
	return lest


def sign_eval(list):
	list2 = []
	for x in list:
		if "--" in x:
			list2.append(x.replace("--", ""))
		else:
			list2.append(x)
	return list2

def like_terms(sidel):
	side = rem_xtra(sidel)
	xlist = []
	ylist = []
	constantlist = []
	for i in range(len(side)):
			ii = side[i]
			if "x" in ii:
				xlist.append(side[i])
			if "y" in ii:
				ylist.append(side[i])
			elif  "x" not in ii:
				constantlist.append(side[i])
	if len(xlist) > 1:
		nxlist = 0.0
		for x in xlist:
			side.remove(x)
			add = x.replace("x", "")
			if add == "-":
				add = "-1"
			if add == "":
				add = "1"
			nxlist += float(add)

		side.append(" " + str(nxlist))
	if len(ylist) > 1:
		nylist = 0.0
		for x in ylist:
			side.remove(x)
			add = x.replace("y", "")
			if add == "-":
				add = "-1"
			if add == "":
				add = "1"
			nylist += float(add)
		side.append(" " + str(nylist))
	if len(constantlist) > 1:
		nconstantlist = 0.0
		for x in constantlist:
			side.remove(x)
			nconstantlist += float(x)
		side.append(" " + str(nconstantlist))
	return side

def yform(unparsed):
	left, right = unparsed.split("=")
	rterms1 = right.split()
	lterms1 = left.split()
	lterms = []
	rterms = []
	for i in lterms1:
		if 'y' in i:
			lterms.append(i)
		if 'x' in i:
			rterms.append(" -" + i)
		if "y" not in i:
			if "x" not in i:
				rterms.append(" -" + i)
	for i in rterms1:
		if 'y' in i:
			i = i.replace("y", "")
			lterms.append(" -" + str(int(i)) + 'y')
		else:
			rterms.append(" " + i)

	rterms = rem_xtra(rterms)
	lterms = rem_xtra(lterms)

	# sign eval
	rterms = sign_eval(rterms)
	lterms = sign_eval(lterms)

	#like terms
	rterms = like_terms(rterms)
	lterms = like_terms(lterms)
	# division
	rterms = rem_xtra(rterms)
	lterms = rem_xtra(lterms)
	print(rterms)
	print(lterms)
	inter = []
	y_coefficient = "".join(lterms).replace("y", "")
	if y_coefficient == "":
		y_coefficient = 1
	if y_coefficient == "-":
		y_coefficient = -1
	if y_coefficient != "":
		y_coefficient = int(y_coefficient)
		lterms = ["y"]
		while len(rterms) != 0:
			iii = rterms[0]
			rterms.remove(iii)
			iii = iii.replace(" ", "")
			if "x" not in iii:
				res = float(iii)/y_coefficient
				inter.append( " " + str(res))
			if "x" in iii:
				iii = iii.replace("x", "")
				if iii == "":
					iii = "1"
				if iii == "-":
					iii = "-1"
				iii = int(iii)/y_coefficient
				iii = str(iii) + "x"
				inter.append(" " + iii)


	rterms = rem_xtra(inter)
	lterms = rem_xtra(lterms)
	print(rterms)
	print(lterms)
	yform = "".join(lterms) + " = " + "".join(rterms)
	print(yform)
	return rterms

def insert_y(unparsed, y):
	print("start exp")
	left, right = unparsed.split("=")
	rterms1 = right.split()
	lterms1 = left.split()
	lterms = []
	rterms = []
	print(lterms1, "lterms1")
	for i in lterms1:
		if 'y' in i:
			print("y instance ", i)
			if i == "-y":
				ni = -1
			elif i == "y":
				ni = 1
			else:
				ni = float(i.replace("y", ""))


			print(ni)
			for lv in y:
				if "x" in lv:
					lv = lv.replace("x", "")
					print(i)
					lv = float(lv)*ni
					lterms.append(" " + str(lv) + "x")
				else:
					lv = float(lv)*ni
					print(lv, "lv")
					rterms.append(" -" + str(lv))
		if 'x' in i:
			lterms.append(i)
		if "y" not in i:
			if "x" not in i:
				rterms.append(" -" + i)
	for i in rterms1:
		if 'y' in i:
			ni = float(i.replace("y", ""))
			if i == "y":
				ni = 1
			for lv in y:
				if "x" in lv:
					lv = lv.replace("x", "")
					print(i)
					lv = float(lv) * ni
					lterms.append(" " + str(lv) + "x")
				else:
					lv = float(lv) * ni
					rterms.append(" -" + str(i))
		if 'x' in i:
			i = i.replace("x", "")
			lterms.append(" -" + str(int(lv)) + 'x')
		else:
			rterms.append(i)

	print("final rs")
	print(rterms)
	print(lterms)
	rterms = rem_xtra(rterms)
	lterms = rem_xtra(lterms)


	# sign eval
	rterms = sign_eval(rterms)
	lterms = sign_eval(lterms)

	#like terms
	rterms = like_terms(rterms)
	lterms = like_terms(lterms)
	# division
	rterms = rem_xtra(rterms)
	lterms = rem_xtra(lterms)
	yform = "".join(lterms) + " = " + "".join(rterms)
	print(yform)
	inter = []

	y_coefficient = "".join(lterms).replace("x", "")
	if y_coefficient == "":
		y_coefficient = 1
	if y_coefficient == "-":
		y_coefficient = -1
	if y_coefficient != "":
		y_coefficient = float(y_coefficient)
		lterms = ["x"]
		while len(rterms) != 0:
			iii = rterms[0]
			rterms.remove(iii)
			iii = iii.replace(" ", "")
			res = float(iii) / y_coefficient
			inter.append(" " + str(res))

	rterms = rem_xtra(inter)
	lterms = rem_xtra(lterms)
	yform = "".join(lterms) + " = " + "".join(rterms)
	xf = float("".join(rterms))
	print(xf)
	yf = 0
	for i in y:
		if 'x' in i:
			i = i.replace("x", "")
			lv = float(i)*xf
			print(lv)
			yf += lv
		else:
			yf += float(i)
	return xf, yf

if __name__ == "__main__":
	unparsed1 = input("enter equation one: ")
	unparsed2 = input("enter equation two: ")
	print(unparsed1)

	try:
		y = yform(unparsed1)
		xf, yf = insert_y(unparsed2, y)
		print("(" + str(xf) + ", " + str(yf) + ")")
	except:
		y = yform(unparsed2)
		xf, yf = insert_y(unparsed1, y)
		print("(" + str(xf) + ", " + str(yf) + ")")

def solve_system_of_coefficents(systems): # gives 2 3 4 5 2 1 = result the fact terms are coefficents are implied
	print("idk")