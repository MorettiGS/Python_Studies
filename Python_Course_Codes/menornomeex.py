def menor_nome(nomes):
    x = []
    tam = 100000000
    for i in nomes:
        i = i.strip()
        i = i.lower()
        i = i.capitalize()
        x.append(i)
    for y in x:
        tamant = tam
        tam = len(y)
        if tam < tamant:
            menortam = tam
    pos = len(x) - 1
    while pos >= 0:
        if menortam == len(x[pos]):
            menor = x[pos]
        pos = pos - 1
    return menor
    