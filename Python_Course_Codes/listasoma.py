def soma_elementos(x):
	tam = len(x) - 1
	s = 0
	while tam >= 0:
		s = s + x[tam]
		tam = tam - 1
	return s