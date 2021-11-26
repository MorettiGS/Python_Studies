def soma_matrizes(m1, m2):
    for x in m1:
        c1 = len(x)
    l1 = len(m1)
    for y in m2:
        c2 = len(y)
    l2 = len(m2)
    if l1 == l2 and c1 == c2:
        soma = []
        for p in range(l1):
            linha = []
            for t in range(c1):
                linha.append(0)
            soma.append(linha)
        h = 0
        for i in m1:
            k = 0
            for j in i:
                soma[h][k] = m1[h][k] + m2[h][k]
                k = k + 1
            h = h + 1
        return soma
    else:
        return False