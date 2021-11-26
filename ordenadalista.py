def ordenada(lista):
    lista_crescente = []
    for i in lista:
        lista_crescente.append(i)
    lista_crescente.sort()
    if lista == lista_crescente:
        return True
    else:
        return False