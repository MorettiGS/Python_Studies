class Buscador:
    def busca_sequencial(self, lista, elemento):
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1

    def busca_binária(self, lista, elemento):
        assert self.esta_ordenada(lista)

        primeiro = 0
        ultimo = len(lista)-1

        while primeiro <= ultimo:
            meio = (primeiro + ultimo)//2
            if lista[meio] == elemento:
                return meio
            elif x < lista[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1
        return -1

    def esta_ordenada(self, l):
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                return False
        return True