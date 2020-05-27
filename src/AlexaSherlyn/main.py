from clasesA import Celular, Mesa, Gato

while True:
    opcion = int(input("Elige una clase:\n1.- Celular\n2.- Mesa\n3.- Gato\n"))

    if opcion == 1:

        marca = ("SAMSUNG")
        modelo = ("A30S")

        cel = Celular(marca, modelo)
        
        print(cel.imprimirInfo())

    if opcion == 2:

        color = ("Chocolate")
        sillas = ("6")

        table = Mesa(color, sillas)

        print(table.imprimirInfo())

    if opcion == 3:

        sexo = ("Macho")
        nombre = ("Nino")

        michi = Gato(sexo, nombre)

        print(michi.imprimirInfo())