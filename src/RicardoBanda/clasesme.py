class suma():
    def __init__(self, num1, num2):
        self.__num1=num1
        self.__num2=num2
    def suma(self):
        return f"El resultado de la suma es {self.__num1+self.__num2}"

class Carro():
    def __init__(self, color, marca, transmicion):
        self.__color=color
        self.__marca=marca
        self.__transmicion=transmicion
    def infocarro(self):
        return f"Es color{self.__color}, Es de la marca{self.__marca}, Su transmicion es{self.__transmicion}"

class video():
    def __init__(self, duracion, titulo, reproducciones):
        self.__duracion=duracion
        self.__titulo=titulo
        self.__reproducciones=reproducciones
    def infovideo(self):
        return f"Dura{self.__duracion}, Se llama{self.__titulo}, Se reprodujo{self.__reproducciones}"
        

        
        


