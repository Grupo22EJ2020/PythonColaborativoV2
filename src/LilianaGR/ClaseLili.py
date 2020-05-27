class gato ():
    def __init__(self,color,sexo):
        self.__color=color
        self.__sexo=sexo

    def imprimirinfo(self):
        print(f"Este es el color {self.__color}")
        print(f"Este es el sexo del gato {self.__sexo}")

class perro ():
    def __init__(self,color,raza):
        self.__color=color
        self.__raza=raza

    def imprimirinfo(self):
        print(f"Este es el color {self.__color}")
        print(f"Este es el raza del perro {self.__raza}")

class conejo ():
    def __init__(self,color,tamaño,comida):
        self.__color=color
        self.__tamaño=tamaño
        self.__comida=comida

    def imprimirinfo(self):
        print(f"Este es el color {self.__color}")
        print(f"Este es el tamaño del conejo {self.__tamaño}")
        print(f"Este es la comida del conejo {self.__comida}")