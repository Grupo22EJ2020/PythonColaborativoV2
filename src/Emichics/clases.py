class Celular:
    def __init__(self, marca, precio):
        self.__marca = marca
        self.__precio = precio
    @property
    def marca (self):
        return self.__marca
    @property
    def precio (self):
        return self.__precio
    @marca.setter
    def marca (self, valor):
        self.__marca = valor
    @precio.setter
    def precio (self, valor):
        self.__precio = valor
    
    def imprimirInfo(self):
        print(f"Su celular marca {self.__marca} fue comprado a un precio de {self.__precio}.")
class Lentes:
    def __init__(self,aumento,costo):
        self.__aumento = aumento
        self.__costo = costo
    @property
    def aumento (self):
        return self.__aumento
    @property
    def costo (self):
        return self.__costo
    @aumento.setter
    def aumento (self, valor):
        self.__aumento = valor
    @costo.setter
    def costo (self, valor):
        self.__costo = valor
    
    def imprimirInfo(self):
        print(f"Los lentes tienen un aumento de {self.__aumento} y le costaron {self.__costo}.")
class Perro:
    def __init__(self, color, raza):
        self.__color = color
        self.__raza = raza
    @property
    def color (self):
        return self.__color
    @property
    def raza (self):
        return self.__raza
    @color.setter
    def color (self, valor):
        self.__color = valor
    @raza.setter
    def raza (self, valor):
        self.__raza = valor
    
    def imprimirInfo(self):
        print(f"Su perro es de color {self.__color} y es de raza {self.__raza}.")

    
    