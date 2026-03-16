class Anime():
    def __init__(self,nombre, genero, nroEpisodios):
        self.nombre=nombre
        self.genero=genero
        self.__nroEpisodios= nroEpisodios
        self.__episodios=[]

    def __str__(self):
        return f"anime: {self.nombre} , genero: {self.genero} , episodios: {self.__nroEpisodios}"

class Main():
    x= Anime("naruto","guerra",300)
    print(x)

    y=Anime("doraymo", "Comedia",564)
    print(y)