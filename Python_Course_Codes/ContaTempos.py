import ordenadorclasse
import random
import time

class ContaTempos:
    def lista_aleatoria(self, n):
        lista = [random.randrange(1000) for x in range(n)]
        return lista

    def lista_quase_ordenada(self, n):
        lista = [x for x in range(n)]
        lista[n//10] = -500
        return lista

    def compara (self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]
        lista3 = lista1[:]
        o = ordenadorclasse.Ordenador()

        print("Comparando com listas aleatórias:")

        antes = time.time()
        o.selecao_direta(lista1)
        depois = time.time()
        print("A seleção direta demorou", depois - antes, "segundos para executar.")

        antes = time.time()
        o.bolha(lista2)
        depois = time.time()
        print("A bolha demorou", depois - antes, "segundos para executar.")

        print("\nComparando com listas quase ordenadas:")

        lista1 = self.lista_quase_ordenada(n)
        lista2 = lista1[:]

        antes = time.time()
        o.selecao_direta(lista1)
        depois = time.time()
        print("A seleção direta demorou", depois - antes, "segundos para executar.")

        antes = time.time()
        o.bolha_curta(lista2)
        depois = time.time()
        print("A bolha demorou", depois - antes, "segundos para executar.")

        