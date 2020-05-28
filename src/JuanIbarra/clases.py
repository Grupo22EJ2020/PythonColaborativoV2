class Serie ():
    def __init__ (self,temporadas,capitulos,duracion):
        self.__temporadas=temporadas
        self.__capitulos=capitulos
        self.__duracion=duracion

    def MostrarInformacion(self):
        print(f"temporadas: {self.__temporadas}")
        print(f"capitulos: {self.__capitulos}")
        print(f"duracion: {self.__duracion}")

class ClubDeFutbol ():
    def __init__ (self,fundacion,estadio,titulos):
        self.__fundacion=fundacion
        self.__estadio=estadio
        self.__titulos=titulos

    def MostrarInformacion(self):
        print(f"fundacion: {self.__fundacion}")
        print(f"estadio: {self.__estadio}")
        print(f"titulos: {self.__titulos}")
    
class Contigencia ():
    def __init__ (self,duracion,contagiados,sospechosos,recuperados):
        self.__duracion=duracion
        self.__contagiados=contagiados
        self.__sospechosos=sospechosos
        self.__recuperados=recuperados
    
    def MostrarInformacion(self):
        print(f"duracion: {self.__duracion}")
        print(f"contagiados: {self.__contagiados}")
        print(f"sospechosos: {self.__sospechosos}")
        print(f"recuperados: {self.__recuperados}")









