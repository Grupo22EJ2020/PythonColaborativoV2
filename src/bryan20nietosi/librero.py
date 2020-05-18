class Alumno:
    def __init__(self,nombre,apellidos):
        self.__a=nombre
        self.__b=apellidos
    def Nombratura(self):
        return f"Nombre: {self.__a} Apellido: {self.__b}"
class Calificacion:
    def __init__(self,parcial,final):
        self.__c=parcial
        self.__d=final
    def Promedio(self):
        return f"Promedio Final: {(self.__c+self.__d)/2}"