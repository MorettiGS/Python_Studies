def menor_lexi(x):
    primeiro = x[0].strip().lower()
    for i in x:
        i = i.strip().lower()
        if i < primeiro:
            primeiro = i
    return primeiro