import random

def lista_grande(n):
    aleatorio_lista = []
    for i in range(n):
        numero = random.randint(-10000, 50000)
        aleatorio_lista.append(numero)
    return aleatorio_lista