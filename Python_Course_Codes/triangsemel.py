class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if self.b == self.c == self.a:
            return "equilátero"
        elif self.b == self.c or self.c == self.a or self.a == self.b:
            return "isósceles"
        else:
            return "escaleno"

    def retangulo(self):
        if self.a **2 + self.b **2 == self.c **2 or self.c**2 + self.b**2 == self.a**2 or self.b**2 + self.a**2 == self.c**2:
            return True
        else:
            return False

    def semelhantes(self, triangulo):
        lista1 = [self.a, self.b, self.c]
        lista2 = [triangulo.a, triangulo.b, triangulo.c]
        lista1.sort()
        lista2.sort()
        if lista1[0]%lista2[0] == 0 and lista1[1]%lista2[1] == 0 and lista1[2]%lista2[2] == 0:
            return True
        elif lista2[0]%lista1[0] == 0 and lista2[1]%lista1[1] == 0 and lista2[2]%lista1[2] == 0:
            return True
        else:
            return False