class Televisor:
    def __init__(self, marca=None, resolucion=None, tipo=None):
        self.__marca = marca
        self.__resolucion = resolucion
        self.__tipo = tipo

    def __str__(self):
        return f"marca: {self.__marca}, resolucion: {self.__resolucion}, tipo: {self.__tipo}"


    def getmarca(self):
        return self.__marca

    def getresolucion(self):
        return self.__resolucion

    def gettipo(self):
        return self.__tipo

    
    def setmarca(self, nuevo):
        self.__marca = nuevo

    def setresolucion(self, nuevo):
        self.__resolucion = nuevo

    def settipo(self, nuevo):
        self.__tipo = nuevo