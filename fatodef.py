def fat(n):
	y = 1
	while n > 1:
		y = y * n
		n = n - 1
	return y
def numerofat(n,k):
	return fat(n) / (fat(k) * fat(n - k))
