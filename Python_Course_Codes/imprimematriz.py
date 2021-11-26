def imprime_matriz(matriz):
    h = 0
    for i in matriz:
        k = 0
        for j in i:
            if k + 1 == len(i):
                print(j)
            else:
                print(j, end = " ")
            k = k + 1
    