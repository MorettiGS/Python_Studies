import ordenadorclasse
import pytest
import ContaTempos

class TestaOrdenador:
    @pytest.fixture
    def o(self):
        return ordenadorclasse.Ordenador()

    @pytest.fixture
    def l_quase(self):
        c = ContaTempos()
        return c.lista_quase_ordenada(100)
    
    @pytest.fixture
    def l_aleatoria(self):
        c = ContaTempos()
        return c.lista_aleatoria(100)

    def esta_ordenada(self, l):
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                return False
        return True

    def teste_bolha_curta_aleatoria(self, o, l_aleat):
        o.bolha_curta(l_aleat)
        assert self.esta_ordenada(l_aleat)

    def teste_bolha_curta_quase(self, o, l_quase):
        o.bolha_curta(l_quase)
        assert self.esta_ordenada(l_quase)

    def teste_selecao_aleatoria(self, o, l_aleat):
        o.selecao_direta(l_aleat)
        assert self.esta_ordenada(l_aleat)

    def teste_selecao_quase(self, o, l_quase):
        o.selecao_direta(l_quase)
        assert self.esta_ordenada(l_quase)

    def teste_bolha_aleat(self, o, l_aleat):
        o.bolha(l_aleat)
        assert self.esta_ordenada(l_aleat)

    def teste_bolha_quase(self, o, l_quase):
        o.bolha(l_quase)
        assert self.esta_ordenada(l_quase)