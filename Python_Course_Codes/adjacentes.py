numero = int(input("Digite um número inteiro: "))
adjacente = False
while adjacente == False and numero != 0:
	primeiro = numero % 10
	segundo = (numero // 10) % 10
	if primeiro == segundo:
		adjacente = True
	else:
		numero = numero // 10
if adjacente:
	print("sim")
else:
	print("não")