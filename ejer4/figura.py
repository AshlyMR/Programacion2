import math
from abc import ABC, abstractmethod
class Figura(ABC):
    def __init__(self, c):
        self.color = c
    def getColor(self):
        return self.color
    # Método abstracto getArea
    @abstractmethod
    def getArea(self):
        pass
    def __str__(self):
        return f"Figura [color={self.color}]"

class Cuadrado(Figura):
    def __init__(self, c, lado):
        super().__init__(c)
        self.lado = lado
#b
    def getArea(self):
        return self.lado ** 2

    def __str__(self):
        return f"Cuadrado [color={self.color}, lado={self.lado}]"

class Triangulo(Figura):
    def __init__(self, c, lado1, lado2, lado3):
        super().__init__(c)
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    #b
    def getArea(self):
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
    def __str__(self):
        return f"Triangulo [color={self.color}, lado1={self.lado1}, lado2={self.lado2}, lado3={self.lado3}]"

class Redondo(Figura):
    def __init__(self, c, radio):
        super().__init__(c)
        self.radio = radio
    #b
    def getArea(self):
        return math.pi * self.radio ** 2
    def __str__(self):
        return f"Redondo [color={self.color}, radio={self.radio}]"
#C
c1 = Cuadrado("rojo", 5)
c2 = Cuadrado("azul", 3)
t1 = Triangulo("verde", 3, 4, 5)
t2 = Triangulo("amarillo", 6, 8, 10)
r1 = Redondo("morado", 4)
r2 = Redondo("naranja", 2)
print(c1, "Area:", c1.getArea())
print(c2, "Area:", c2.getArea())
print("------------------------------")
print(t1, "Area:", t1.getArea())
print(t2, "Area:", t2.getArea())
print("------------------------------")
print(r1, "Area:", r1.getArea())
print(r2, "Area:", r2.getArea())
#d
print("mayor area")
if c1.getArea() > t1.getArea():
    print(f" {c1} tiene el area más grande.")
elif t1.getArea() > c1.getArea():
    print(f" {t1} tiene el area más grande.")
else:
    print("Ambas figuras tienen la misma area.")