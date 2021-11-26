import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))
    assin = [wal, ttr, hlr, sal, sac, pal]
    return assin

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = separa_sentencas(texto)
    frases = []
    pala = []
    for sentenca in sentencas:
        frasesent = separa_frases(sentenca)
        frases.append(frasesent)
    for frase in frases:
        palafrase = separa_palavras(frase)
        pala.append(palafrase)
    
    palaunicas = n_palavras_unicas(pala)
    paladif = n_palavras_diferentes(pala)
    nsent = len(sentencas)
    nfrases = len(frases)
    npala = len(pala)
    tamtotsent = 0
    tamtotfrase = 0
    tamtotpala = 0
    
    for tam in sentencas:
        tamsent = len(tam)
        tamtotsent = tamtotsent + tamsent
    for tam in frases:
        tamfrase = len(tam)
        tamtotfrase = tamtotfrase + tamfrase
    for tam in pala:
        tampala = len(tam)
        tamtotpala = tamtotpala + tampala

    tammedpala = tamtotpala / npala
    reltt = paladif / npala
    razhl = palaunicas / npala
    tammedsent = tamtotsent / nsent
    compsent = nfrases / nsent
    tammedfrase = tamtotfrase / nfrases

    ass_a = [tammedpala, reltt, razhl, tammedsent, compsent, tammedfrase]
