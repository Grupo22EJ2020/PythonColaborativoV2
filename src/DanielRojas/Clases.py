class Playera ():
    def __init__ (self,color,marca,talla):
        self.__color=color
        self.__marca=marca
        self.__talla=talla
    
    def imprimirInfo(self):
        print(f"COLOR: {self.__color}")
        print(f"Marca:{self__marca}")
        print(f"Talla:{self.__talla}")