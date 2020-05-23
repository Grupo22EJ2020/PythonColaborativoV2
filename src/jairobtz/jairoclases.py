class Consola():
    def __init__(self,color,procesador,marca):
        self.procesador = procesador
        self.marca = marca
     def imprimirConsola(self):
         print(f"Consola \n procesador: {self.procesador} \n marca: {self.marca}")



class Guitarra():
    def __init__(self,tipo,cuerdas,precio):
        self.tipo = tipo
        self.cuerdas = cuerdas
        self.precio = precio
     def imprimirGuitarra(self):
         print(f"Guitarra \n tipo: {self.tipo} \n cuerdas: {self.cuerdas} \n precio: {self.precio}")

