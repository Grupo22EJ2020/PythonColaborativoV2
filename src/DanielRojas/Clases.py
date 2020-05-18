class Playera ():
    def __init__ (self,color,marca,talla):
        self.__color=color
        self.__marca=marca
        self.__talla=talla
    
    def imprimirInfo(self):
        print(f"COLOR: {self.__color}")
        print(f"Marca:{self.__marca}")
        print(f"Talla:{self.__talla}")

class Pantalon ():
    def __init__ (self,talla,marca,color):
        self.__talla=talla
        self.__marca=marca
        self.__color=color 
    
    def ImprimirInfo(self):
        print(f"Talla : {self.__talla}")
        print(f"Marca : {self.__marca}")
        print(f"Color : {self.__color}")

class Zapatos ():
    def __init__ (self,modelo,marca,costo):
        self.__modelo=modelo
        self.__marca=marca
        self.__costo=costo

    def ImprimirInfo2(self):
        print(f"Modelo : {self.__modelo}")
        print(f"Marca : {self.__marca}")
        print(f"Costo : {self.__costo}")