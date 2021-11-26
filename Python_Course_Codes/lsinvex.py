x = int(input("Digite um número: "))
ls = []
while x != 0:
	ls.append(x)
	x = int(input("Digite um número: "))
tam = len(ls) - 1
while tam >= 0:
    print(ls[tam])
    tam = tam - 1
