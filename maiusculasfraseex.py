def maiusculas(frase):
    maius = ""
    for i in frase:
        if ord(i) > 64 and ord(i) < 91:
            maius = maius + i
    return maius
    