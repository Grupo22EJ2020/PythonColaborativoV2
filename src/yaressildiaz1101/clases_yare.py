class Maquillaje ():
    def __init__(self,marca,colores):
        self.marca = marca
        self.colores = colores

    def imprimirInfo(self):
        print(f"La marca es de prestigio \n Marca: {self.marca} Los colores estan bonitos \n Colores: {self.colores}")


class Bolsas ():
    def __init__ (self,tamaño,precio):
        self.tamaño = tamaño
        self.precio = precio 

    def imprimirInfo(self):
        print(f"El tamaño de la bolsa esta bien \n Tamaño: {self.tamaño} En un buen precio \n Precio: {self.precio}")


class Ropa():
    def __init__(self,estilo,talla):
        self.estilo = estilo
        self.talla = talla 

    def imprimirInfo(self):
        print(f"El estilo esta muy bonito \n Estilo: {self.estilo} En todas las tallas \n Talla: {self.talla}")
        
