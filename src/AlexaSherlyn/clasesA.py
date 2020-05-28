class Celular():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, valor):
        self.__marca = valor

    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, valor):
        self.__modelo = valor
    
    def imprimirInfo(self):
        print(f"Celular\nMarca: {self.marca}\nModelo: {self.modelo}")
    
class Mesa():
    def __init__(self, color, sillas):
        self.color = color
        self.sillas = sillas
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, valor):
        self.__color = valor

    @property
    def sillas(self):
        return self.__sillas
    
    @sillas.setter
    def sillas(self, valor):
        self.__sillas = valor

    def imprimirInfo(self):
        print(f"Mesa\nColor: {self.color}\nSillas: {self.sillas}")

class Gato():
    def __init__(self, sexo, nombre):
        self.sexo = sexo
        self.nombre = nombre

    @property
    def sexo(self):
        return self.__sexo
    
    @sexo.setter
    def sexo(self, valor):
        self.__sexo = valor

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor
    
    def imprimirInfo(self):
        print(f"Gato\nSexo: {self.sexo}\nNombre: {self.nombre}")