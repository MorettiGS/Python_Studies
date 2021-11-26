def encontra_impares(lista):
    impares = []

    if len(lista) > 0:
        numero = lista.pop(0)

        if numero % 2 != 0:
            impares.append(numero)

        impares += encontra_impares(lista)

    return impares