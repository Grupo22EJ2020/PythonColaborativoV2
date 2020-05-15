class Blusa ():
    def __init__ (self,talla,color,):
        self.__talla=talla
        self.__color=color

    def Imprimirinfo (self):
        print (f"talla:{self.__talla}")
        print (f"color:{self.__color}")

class Bolsa ():
    def __init__ (self,tamaño,color,marca):
        self.__tamaño=tamaño
        self.__color=color
        self.__marca=marca

    def Caracteristicas (self):
        print (f"tamaño:{self.__tamaño}")
        print (f"color:{self.__color}")
        print (f"marca:{self.__marca}")
        
class Zapatos ():
    def __init__ (self,talla,color):
        self.__talla=talla
        self.__color=color

    def Informacion (self):
        print (f"talla:{self.__talla}")
        print (f"color:{self.__color}")
        

