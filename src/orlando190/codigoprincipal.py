class PC:
    def __init__(self, procesador, ram):
        self.procesador = procesador
        self.ram = ram
    def imprimirpc(self):
        print(f"PC \n procesador: {self.procesador} \n ram: {self.ram}")


class Nieve:
    def __init__(self, sabor, envase, precio):
        self.sabor = sabor
        self.envase = envase
        self.precio = precio
    def imprimirNIEVE(self):
        print(f"Nieve \n sabor: {self.sabor} \n envase: {self.envase} \n precio: {self.precio}")


class Teclado:
    def __init__(self, precio, marca, modelo):
        self.precio = precio
        self.marca = marca
        self.modelo = modelo
    def imprimirTECLADO(self):
        print(f"Teclado \n precio: {self.precio} \n marca: {self.marca} \n modelo: {self.modelo}")
    
    

