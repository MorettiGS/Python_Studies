print("Somarei os algarismos de um número.")
numero = int(input("Digite o número que deseja somar: "))
soma = 0

while numero != 0:
	algarismo = numero % 10
	soma = soma + algarismo
	numero = numero // 10
print("A soma desses algarismos é",soma)
