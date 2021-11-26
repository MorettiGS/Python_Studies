def é_hipotenusa(x):
	p = 1
	q = 1
	while q < x:
		while p < x:
			if (q ** 2) + (p ** 2) == (x ** 2):
				break
			else:
				p = p + 1
		if (q ** 2) + (p ** 2) == (x ** 2):
			break
		else:
			q = q + 1
			p = 1
	if (q ** 2) + (p ** 2) == (x ** 2):
		return x
	else:
		return 0

def soma_hipotenusas(n):
	k = 1
	total = 0
	while k <= n:
		x = é_hipotenusa(k)
		total = total + x
		k = k + 1
	return total