class persona():
    def __init__(self, nombre, carnet, edad):
        self.nombre = nombre
        self.carnet = carnet
        self.edad = edad
    def __str__(self):
        return f"Nombre: {self.nombre}, Carnet: {self.carnet}, Edad: {self.edad}"
    
class estudiante(persona):
    def __init__(self, nombre, carnet, edad, matricula , carrera):
        super().__init__(nombre, carnet, edad)
        self.matricula = matricula
        self.carrera = carrera
    def __str__(self):
        return f"{super().__str__()}, Matrícula: {self.matricula}, Carrera: {self.carrera}"
    #d
    def misma_carrera(self, otro_estudiante):
        return self.carrera == otro_estudiante.carrera
class Docente(persona):
    def __init__(self, nombre, carnet, edad, antiguedad, sueldo):
        super().__init__(nombre, carnet, edad)
        self.an = antiguedad
        self.sueldo = sueldo
    def __str__(self):
        return f"{super().__str__()}, Antigüedad: {self.an}, Sueldo: {self.sueldo}"

#b
e1 = estudiante("Juan", "C001", 20, "M001", "Ingeniería")
e2 = estudiante("María", "C002", 22, "M002", "Medicina")
d1 = Docente("Dr. Smith", "D001", 22, 20, 5000)

print(e1)
print(e2)

print(d1)

#c
print("misma edad")
if e1.edad == d1.edad:
    print(f"{e1.nombre} tiene la misma edad que el docente.")
elif e2.edad == d1.edad:
    print(f"{e2.nombre} tiene la misma edad que el docente.")
else:
    print("Ningún estudiante tiene la misma edad que el docente.")

#d 
print("misma carrera")
if e1.misma_carrera(e2):
    print(f"{e1.nombre} y {e2.nombre} estudian la misma carrera.")
else:
    print(f"{e1.nombre} y {e2.nombre} no estudian la misma carrera.")