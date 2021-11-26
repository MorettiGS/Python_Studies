numero = int(input("Digite o valor de n: "))
produto = 1
if numero == 0 or numero == 1:
	print("1")
else:
	while numero > 1:
		produto = produto * numero
		numero = numero - 1
	print(produto)