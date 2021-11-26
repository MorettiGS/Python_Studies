print()
print("Digite um número negativo se deseja parar.")
print()
numero = int(input("Digite um número para conseguir seu fatorial: "))
while numero >= 0:
	produto = 1
	if numero == 1 or numero == 0:
		print()
		print("O fatorial desse número é: 1")
	else:
		while numero > 1:
			produto = produto * numero
			numero = numero - 1
		print()
		print("O fatorial desse número é:",produto)
	print()
	numero = int(input("Digite um número para conseguir seu fatorial: "))
print()
print(":)")