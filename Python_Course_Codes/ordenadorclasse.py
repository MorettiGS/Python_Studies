class Ordenador:
    def selecao_direta(self, lista):
        fim = len(lista)

        for i in range(fim - 1):
            pos_minimo = i

        for j in range(i+1, fim):
            if lista[j] < lista[pos_minimo]:
                pos_minimo = j

        lista[i], lista[pos_minimo] = lista[pos_minimo], lista[i]

    def bolha (self, lista):
        fim = len(lista)

        for i in range(fim-1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j],lista[j+1] = lista[j+1],lista[j]

    def bolha_curta (self, lista):
        fim = len(lista)

        for i in range(fim-1, 0, -1):
            trocou = False
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j],lista[j+1] = lista[j+1],lista[j]
                    trocou = True
            if not trocou:
                return

    def insertion_sort(self, lista):
        for x in range(1, len(lista)):
            valor = lista[x]

            while x > 0 and lista[x - 1]>valor:
                lista[pos]=lista[pos - 1]
                x = x - 1
            lista[pos] = valor