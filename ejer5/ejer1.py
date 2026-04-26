class Libro:
    def __init__(self, nombre, autor, año ):
        self.__nombre = nombre
        self.__autor = autor
        self.__año = año 
    
    def getNombre(self):
        return self.__nombre
    
    def getAutor(self):
        return self.__autor
    
    def getAño(self):
        return self.__año

    def __str__(self):
        return f"Libro: {self.__nombre}, Autor: {self.__autor}, Año: {self.__año}"

class Biblioteca :
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__libros = []
    def getNombre(self):
        return self.__nombre
    
    def agregar_libro(self, libro):
        if libro not in self.__libros:
            self.__libros.append(libro)
        
    def mostrarLibro(self):
        print("Biblioteca: ", self.__nombre)
        if len(self.__libros) == 0:
            print("no hay libros")
        else:
            for l in self.__libros:
                print(l)
    def buscarLibro(self, nombre):
        for l in self.__libros:
            if l.getNombre() == nombre:
                print("Libro encontrado:")
                print(l)
                return
        print("Libro no encontrado")

    def cantidadLibros(self):
        return len(self.__libros)
    
l1 = Libro("El Quijote", "Miguel de Cervantes", 1605)
l2 = Libro("El Arte de la Guerra", "SUN TZU", 500) 
l3 = Libro("Don Juan Tenorio", "José Zorrilla", 1844)
l4 = Libro("Ciudad Blanca", "Maria Soledad Quiroga", 1993)

b1 = Biblioteca("Biblioteca Central UMSA")
b2 = Biblioteca("Biblioteca Municipal")
#b
b1.agregar_libro(l1)
b1.agregar_libro(l2)

b2.agregar_libro(l3)
b2.agregar_libro(l4)

b1.mostrarLibro()
b2.mostrarLibro()
#c
b1.buscarLibro("El Arte de la Guerra")
#d
print("Biblioteca con mas libros: ")
if b1.cantidadLibros() > b2.cantidadLibros():
    print(b1.getNombre())
elif b1.cantidadLibros() < b2.cantidadLibros():
    print(b2.getNombre())

else:
    print("Ambas bibliotecas tienen la misma cantidad de libros")
    print(b1.getNombre())
    print(b2.getNombre())