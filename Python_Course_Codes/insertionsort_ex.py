def insertion_sort(lista):
    for x in range(1, len(lista)):
        valor = lista[x]

        while x > 0 and lista[x - 1]>valor:
            lista[x]=lista[x - 1]
            x = x - 1
        lista[x] = valor

    return lista