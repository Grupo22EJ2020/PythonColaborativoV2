class celular ():
    def __init__(self,marca,color):
        self.marca = marca
        self.color = color
    
    def ImprimirInfo (self):
        print (f"la marca del celular es:{self.marca}")
        print (f"el color del celular es:{self.color}")



class vestido ():
    def __init__(self, precio, talla, color):
        self.precio = precio
        self.talla = talla
        self.color = color

    def ImprimirInfo (self):
        print (f"el precio del vestido es:{self.precio}")
        print (f"la talla del vestido es:{self.talla}")
        print (f"el color del vestido es:{self.color}")
        