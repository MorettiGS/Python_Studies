numero = int(input("Digite um número inteiro maior que um: "))
fator = 2
mult = 0
while numero <= 1:
	if numero > 1:
		break
	else:
		print()
		numero = int(input("Digite um número inteiro maior que um: "))
print()
print(numero,"=", end = " ")
while numero > 1:
	while numero % fator == 0:
		mult = mult + 1
		numero = numero / fator
	if mult == 0:
		print(end = "")
	else:
		print("(",fator,"^",mult,")", end = " ")
	mult = 0
	fator = fator + 1
print()