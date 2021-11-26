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
            