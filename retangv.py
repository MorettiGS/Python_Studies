larg = int(input("digite a largura: "))
alt = int(input("digite a altura: "))
p = larg
v = alt
while alt > 0:
	if alt == 1 or alt == v:
		while p > 0:
			print("#", end = "")
			p = p - 1
	else:
		while p > 0:
			if p == 1 or p == larg:
				print("#", end = "")
				p = p - 1
			else:
				print(" ", end = "")
				p = p - 1
	print()
	p = larg
	alt = alt - 1