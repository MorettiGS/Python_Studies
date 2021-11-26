def eprimo(k):
	while k % 2 == 0 or k % 3 == 0 or k % 5 == 0 or k % 7 == 0 or k % 11 == 0 or k % 13 == 0 or k %31 == 0:
		if k < 32:
			if k == 2 or k == 3 or k == 5 or k == 7 or k == 11 or k == 13 or k == 31:
				break
			else:
				k = k - 1
		else:
			k = k - 1
	x = k
	return x
def maior_primo(x):
	return eprimo(x)

	
	
