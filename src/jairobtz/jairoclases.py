class Consola():
    def __init__(self,color,procesador,marca):
        self.procesador = procesador
        self.marca = marca
     def imprimirConsola(self):
         print(f"Consola \n procesador: {self.procesador} \n marca: {self.marca}")
