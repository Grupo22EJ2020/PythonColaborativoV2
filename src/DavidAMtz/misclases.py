class Gorra ():
    def __int__(self, diseño, talla, color):
        self.__diseño=diseño
        self.__talla=talla
        self.__color=color

    def ImprimirInfo(self):
        print(f"diseño:{self.__diseño}  talla:{self.__talla}  color:{self.__color}")

class Television ():
    def __int__(self, marca, pulgadas, modelo):
        self.__marca=marca
        self.__pulgadas=pulgadas
        self.__modelo=modelo

    def ImprimirInfo(self):
        print(f"marca:{self.__marca}  pulgadas:{self.__pulgadas}  modelo:{self.__modelo}")

class Pulsera ():
    def __int__(self, marca, talla, color):
        self.__marca=marca
        self.__talla=talla
        self.__color=color

    def ImprimirInfo(self):
        print(f"marca:{self.__marca}  talla:{self.__talla}  color:{self.__color}")
        