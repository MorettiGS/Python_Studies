def primeiro_lex(lista):
    primeiro = lista[0].strip()
    for i in lista:
        i = i.strip()
        if i < primeiro:
            primeiro = i
    return primeiro