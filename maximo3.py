def maximo(x, y, z):
	if x>=y>=z or x>=z>=y:
		return x
	else:
		if z>=y>=x or z>=x>=y:
			return z
		else:
			return y