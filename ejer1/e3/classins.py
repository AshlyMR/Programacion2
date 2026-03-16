class Instrumento():
    def __init__(self,nombre,material,tipo):
        self.nombre= nombre
        self.__material= material
        self.__tipo= tipo

    def __str__(self):
        return f"nombre: {self.nombre} , material: {self.__material} , tipo:{self.__tipo}"

class Main():
    x=Instrumento ("bajo", "mastil", "cuerda")
    print(x)

    y=Instrumento ("guitarra","madera","cuerda")
    print(y)