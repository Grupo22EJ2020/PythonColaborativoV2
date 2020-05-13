class Cuadrado:
    def __init__(self,lado):
        self.lado=lado
    def area (self):
        return self.lado * self.lado
    def perimetro (self):
        return self.lado * 4
lado = int (input("Dame el lado: "))
cuadrito = Cuadrado(lado)
a=cuadrito.area()
p= cuadrito.perimetro()
print (f"el area es{a}")
print (f"el perimertro es{p}")