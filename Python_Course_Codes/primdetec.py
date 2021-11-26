print("Caso deseje acabar, digite um número menor que 1.")
numero = int(input("Digite um número inteiro maior que 1: "))
p = 2
while numero > 1:
	while p < numero and numero % p != 0:
		if numero == p:
			break
		else:
			p = p + 1
	if numero == p:
		print()
		print("True.")
		print()
	else:
		print()
		print("False.")
		print()
	p = 2
	numero = int(input("Digite um número inteiro maior que 1: "))
print()
print(":)")
