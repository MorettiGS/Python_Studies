def menor_nome(x):
    nomes = []
    tam = 100000000
    for i in x:
        i = i.strip()
        i = i.capitalize()
        nomes.append(i)
    for y in nomes:
        tamant = tam
        tam = len(y)
        if tam < tamant:
            menortam = tam
    for m in nomes:
        if menortam = len(m):
            menor = m
    return menor
    