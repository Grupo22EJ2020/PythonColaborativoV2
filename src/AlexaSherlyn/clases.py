class Celular():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def imprimirInfo(self):
        print(f"Cargador \n Marca: {self.marca} \n Modelo: {self.modelo}")
    
class Mesa():
    def __init__(self, color, sillas):
        self.color = color
        self.sillas = sillas
    
    def imprimirInfo(self):
        print(f"Mesa \n Color: {self.color} \n Sillas: {self.sillas}")

class Gato():
    def __init__(self, sexo, nombre):
        self.sexo = sexo
        self.nombre = nombre
    
    def imprimirInfo(self):
        print(f"Gato \n Sexo: {self.sexo} \n Nombre: {self.nombre}")