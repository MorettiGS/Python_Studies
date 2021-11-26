larg = int(input("digite a largura: "))
alt = int(input("digite a altura: "))
p = larg
while alt > 0:
	while p > 0:
		print("#", end = "")
		p = p - 1
	print()
	p = larg
	alt = alt - 1