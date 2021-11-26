import math
def zero (a,b):
	unica = (-b) / (2*a)
	print("a raiz dessa equação é",unica)
def maior(a,b):
	um= ((-b) - (math.sqrt(delta))) / (2*a)
	dois=((-b) + (math.sqrt(delta))) / (2*a)
	print("as raízes da equação são:",um,dois)
def funcdelta (a,b,c):
	delta = (b ** 2) - (4 * a * c)
	if delta<0:
		print("essa equação não possui raízes reais")
	else:
		if delta == 0:
			zero(a,b)
		else:
			maior(a,b,delta)
	