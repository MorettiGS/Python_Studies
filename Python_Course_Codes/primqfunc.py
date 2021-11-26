def n_primos(n):
	p = 1
	q = 0
	x = 2
	while n >= p:
		while x < p and p % x != 0:
			if p == x:
				break
			else:
				x = x + 1
		if p == x:
			q = q + 1
			p = p + 1
		else:
			p = p + 1
		x = 2
	return q