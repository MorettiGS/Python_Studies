def ordena(lista):
    fim = len(lista)

    for i in range(fim - 1):
        pos_minimo = i

        for j in range(i+1, fim):
            if lista[j] < lista[pos_minimo]:
                pos_minimo = j

        lista[i], lista[pos_minimo] = lista[pos_minimo], lista[i]

    return lista