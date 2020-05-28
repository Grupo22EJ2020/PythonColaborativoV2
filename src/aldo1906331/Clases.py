class Jugo ():
    def __init__ (self,marca,sabor):
        self.marca = marca
        self.sabor = sabor

    def imprimirJugo (self):
        print (f"Tu jugo favorito es {self.marca} tiene un sabor a {self.sabor}")



class Videojuego ():
    def __init__ (self,modo,tipoDejuego):
        self.modo = modo
        self.tipoDejuego = tipoDejuego

    def imprimirJuego (self):
        print (f"Cual es tu modo favorito de jugar {self.modo} que tipo de juego tiene {self.tipoDejuego}")



class fruta ():
    def __init__ (self,tamaño,tipoDefruta):
        self.tamaño = tamaño
        self.tipoDefruta = tipoDefruta

    def imprimirlafruta (self):
        print (f"El tamaño de tu fruta preferida es {self.tamaño} que tipo de fruta es {self.tipoDefruta}")
        