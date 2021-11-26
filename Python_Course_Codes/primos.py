numero = int(input("Digite um número inteiro: "))

if numero == 1:
	print("não primo")
else:
	if numero == 2 or numero == 3 or numero == 5 or numero == 7 or numero == 11 or numero == 13 or numero == 17:
		print("primo")
	else:
		if numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0 or numero % 7 == 0 or numero % 11 == 0 or numero % 13 == 0 or numero % 17 == 0:
			print("não primo")
		else:
			print("primo")