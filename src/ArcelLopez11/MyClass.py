class xbox():
    def __init__(self, Precio, Color):
        self.Precio = Precio
        self.Color = Color

    
    def imprimirInfo(self):
        print(f"xbox\n Precio: {self.Precio} \n Color: {self.Color}")


class Abanico():
    def __init__(self, Tamaño, Velocidades):
        self.Tamaño = Tamaño
        self.Velocidades = Velocidades

    
    def imprimirInfo(self):
        print(f"Abanico\n Tamaño: {self.Tamaño} \n Velocidades: {self.Velocidades}")


class Casa():
    def __init__(self, Habitaciones, Baños):
        self.Habitaciones = Habitaciones
        self.Baños = Baños

    
    def imprimirInfo(self):
        print(f"Casa\n Habitaciones: {self.Habitaciones} \n Baños: {self.Baños}")

        