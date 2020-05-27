class Bolso():
    def __init__ (self, color, marca,tamaño):
        self.color = color
        self.marca = marca
        self.tamaño = tamaño
    def imprimirBolso(self):
         print(f"Bolso \n color: {self.color} \n marca: {self.marca} \n tamaño: {self.tamaño}")

class Blusa():
    def __init__ (self, color, marca, talla):
        self.color = color
        self.marca = marca
        self.talla = talla
    def imprimirBlusa(self):
         print(f"Blusa \n color: {self.color} \n marca: {self.marca} \n talla: {self.talla}")


class Auto():
    def __init__(self,modelo,color,año):
        self.modelo = modelo
        self.color = color
        self.año = año
     def imprimirAuto(self):
         print(f"Auto \n modelo: {self.modelo} \n color: {self.color} \n año: {self.año}")
