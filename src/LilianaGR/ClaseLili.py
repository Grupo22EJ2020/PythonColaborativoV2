class gato ():
    def __init__(self,color,sexo):
        self.__color=color
        self.__sexo=sexo

    def imprimirinfo(self):
        print(f"Este es el color {self.__color}")
        print(f"Este es el sexo del gato {self.__sexo}")