class Animal:
    def __init__(self, nombre, edad, nombreDuenio):
        self.__nombre = nombre 
        self.__edad = edad
        self.__nombreDuenio = nombreDuenio
    
    def getNombre(self):
        return self.__nombre

    def getEdad(self):
        return self.__edad

    def getNombreDuenio(self):
        return self.__nombreDuenio
    
    def __str__(self):
        return f"{self.__nombre}, Edad: {self.__edad}, Dueño: {self.__nombreDuenio}"


class Perro(Animal):
    def __init__(self, nombre, edad, nombreDuenio, requiereBosal, ladraFuerte):
        super().__init__(nombre, edad, nombreDuenio)
        self.__requiereBosal = requiereBosal
        self.__ladraFuerte = ladraFuerte
    
    def __str__(self):
        return f"Perro: {super().__str__()}, Bosal: {self.__requiereBosal}, Ladra fuerte: {self.__ladraFuerte}"


class Gato(Animal):
    def __init__(self, nombre, edad, nombreDuenio, cazaRatones, tomaLeche):
        super().__init__(nombre, edad, nombreDuenio)
        self.__cazaRatones = cazaRatones
        self.__tomaLeche = tomaLeche
    
    def getTomaLeche(self):
        return self.__tomaLeche

    def __str__(self):
        return f"Gato: {super().__str__()}, Toma leche: {self.__tomaLeche}"    


class CentroVeterinario:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__perros = []
        self.__gatos = []
    
    def agregarPerro(self, p):
        self.__perros.append(p)

    def agregarGato(self, g):
        self.__gatos.append(g)

    #B
    def ordenarPerros(self):
        self.__perros.sort(key=lambda p: (p.getEdad(), p.getNombreDuenio(), p.getNombre()))
    
    #  C
    def ordenarGatos(self):
        self.__gatos.sort(key=lambda g: (
            not g.getTomaLeche(),   
            -g.getEdad(),           
            g.getNombre()           
        ))


    def mostrar(self):
        print("\nCentro:", self.__nombre)

        print("----P-----")
        for p in self.__perros:
            print(p)

        print("----G-----")
        for g in self.__gatos:
            print(g)

    # Inciso D
    def verificarDuenios(self):
        conteo = {}

        for p in self.__perros:
            d = p.getNombreDuenio()
            conteo[d] = conteo.get(d, 0) + 1

        for g in self.__gatos:
            d = g.getNombreDuenio()
            conteo[d] = conteo.get(d, 0) + 1

        print("\nDueños con más de un animal:")
        for d in conteo:
            if conteo[d] > 1:
                print(d, "tiene", conteo[d], "animales")





c1 = CentroVeterinario("Centro 1")
c2 = CentroVeterinario("Centro 2")


p1 = Perro("Max", 5, "Juan", True, True)
p2 = Perro("Rocky", 3, "Juan", False, False)

g1 = Gato("Michi", 2, "Ana", True, True)
g2 = Gato("Luna", 4, "Ana", False, False)

c1.agregarPerro(p1)
c1.agregarPerro(p2)
c1.agregarGato(g1)
c1.agregarGato(g2)


p3 = Perro("Toby", 6, "Carlos", True, False)
p4 = Perro("Firulais", 2, "Luis", False, True)

g3 = Gato("Misu", 3, "Carlos", True, False)
g4 = Gato("Nina", 1, "Sofia", False, True)

c2.agregarPerro(p3)
c2.agregarPerro(p4)
c2.agregarGato(g3)
c2.agregarGato(g4)


c1.ordenarPerros()
c1.ordenarGatos()

c2.ordenarPerros()
c2.ordenarGatos()


c1.mostrar()
c1.verificarDuenios()

c2.mostrar()
c2.verificarDuenios()