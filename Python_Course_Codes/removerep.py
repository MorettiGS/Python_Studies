def remove_repetidos(x):
	r = len(x) - 1
	t = r - 1
	while r >= 0:
		while t >= 0:
			if x[r] == x[t]:
				del x[t]
			else:
				t = t - 1
		r = r - 1
		t = r - 1
	x.sort()
	return x