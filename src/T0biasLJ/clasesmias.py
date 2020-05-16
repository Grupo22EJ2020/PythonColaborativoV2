class Multiplicacion():
    def __init__(self,numero1,numero2):
        self.__numero1=numero1
        self.__numero2=numero2
    def multi(self):
         return f"El resultado de tu multiplicacion es:{self.__numero1*self.__numero2}"

class Deportista():
    def __init__(self,deporte,peso,edad):
        self.__deporte=deporte
        self.__peso=peso
        self.__edad=edad
    def infodep(self):
        return f"Entrena {self.__deporte} , pesa: {self.__peso} kilos , tiene {self.__edad} años"

class Encuesta:
    def __init__(self,nombre,ciudad):
        self.__nombre=nombre
        self.__ciudad=ciudad
    def infopersona(self):
        return f"Eres {self.__nombre}, vives en {self.__ciudad}"
    

