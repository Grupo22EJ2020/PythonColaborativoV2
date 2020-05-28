from clases import Celular
from clases import Lentes
from clases import Perro

print("Menu\n1.-Celular\n2.-Lentes\n3.-Perro\n4.-Salir")
menu = int(input("Que desea hacer?:\n"))

while True:
    if menu == 1:
        marca = input("De qué marca es su celular?:\n")
        precio = input("Que precio le costó?:\n")
        cel = Celular(marca, precio)
        cel.imprimirInfo()
        print("Menu\n1.-Celular\n2.-Lentes\n3.-Perro\n4.-Salir")
        menu = int(input("Que desea hacer?:\n"))
    if menu == 2:
        aumento = input("Cuanto aumento tienen sus lentes?:\n")
        costo = input("Cuanto le costó?:\n")
        lente = Lentes(aumento, costo)
        lente.imprimirInfo()
        print("Menu\n1.-Celular\n2.-Lentes\n3.-Perro\n4.-Salir")
        menu = int(input("Que desea hacer?:\n"))
    if menu == 3:
        color = input("De qué color es su perro?:\n")
        raza = input("De qué raza es su perro?:\n")
        dog = Perro(color, raza)
        dog.imprimirInfo()
        print("Menu\n1.-Celular\n2.-Lentes\n3.-Perro\n4.-Salir")
        menu = int(input("Que desea hacer?:\n"))
    if menu == 4:
        break

    