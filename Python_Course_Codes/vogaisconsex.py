def conta_letras(frase, contar="vogais"):
    vog = 0
    cons = 0
    frase = frase.lower()
    for i in frase:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            vog += 1
        if i != "a" and i != "e" and i != "i" and i != "o" and i != "u" and ord(i) < 123 and ord(i) > 96:
            cons += 1
    if contar == "vogais":
        return vog
    else:
        if contar == "consoantes":
            return cons