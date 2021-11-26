def cria_matriz(nlinhas, ncolunas, valor):
    matriz = []
    for i in range(nlinhas):
        linha = []
        for j in range(ncolunas):
            linha.append(valor)
        matriz.append(linha)
    for d in matriz:
        print(d)
    return "feito"