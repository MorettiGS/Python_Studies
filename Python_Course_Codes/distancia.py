import math

x1 = int(input("Digite a abscissa de um ponto: "))
y1 = int(input("Digite a ordenada desse mesmo ponto: "))
x2 = int(input("Digite a abscissa de outro ponto: "))
y2 = int(input("Digite a ordenada desse outro ponto: "))

distancia = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

if distancia >= 10:
    print("longe")
else:
    print("perto")