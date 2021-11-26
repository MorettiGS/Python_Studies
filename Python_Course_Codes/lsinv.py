x = int(input("Digite uma sequência de números terminada em 0: "))
ls = []
while x != 0:
	ls.append(x)
	x = int(input("Digite o próximo número da sequência: "))
tam = len(ls) - 1
while tam >= 0:
    print(ls[tam], end=" ")
    tam = tam - 1
