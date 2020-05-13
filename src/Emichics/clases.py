class Celular:
    def __init__(self, marca, precio):
        self.marca = marca
        self.precio = precio
    def imprimirInfo(self):
        print(f"Su celular marca {self.marca} fue comprado a un precio de {self.precio}")