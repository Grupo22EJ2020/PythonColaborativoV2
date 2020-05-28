from MyClass import xbox
from MyClass import Abanico
from MyClass import Casa



Seleccion=1

while seleccion==1:
    print("1=Quiero elegir la clase xbox ")
    print("2=Quiero elegir la clase Abanico")
    print("3=Quiero elegir la clase Casa")
    opcion=int(input(":"))
    if opcion==1:
        Precio=(input("Que precio buscas tu xbox : "))
        Color=(input("Que color quieres tu xbox :"))
        objeto=xbox(Precio,Color)
        objeto.imprimirInfo()
        print("1= Seguir en el programa" )
        print("2=No seguir en el programa" )
        seleccion=int(input("Deseas seguir con el programa :"))

    elif opcion==2:
        Tamaño=(input("Que tamaño quieres tu Abanico:"))
        Velocidades=(input("De cuantas Velocidades quieres tu Abanico : "))
        objeto1=Abanico(Tamaño,Velocidades)
        objeto1.ImprimirInfo()
        print("1= Seguir en el programa" )
        print("2=No seguir en el programa" )
        seleccion=int(input("Deseas seguir con el programa :"))
    
    elif opcion==3:
        Habitaciones=(int(input("Numero de habitaciones en la Casa:")))
        Baños=(int(input("Cuantos Baños tiene la casa:")))
        objeto2=Casa(Habitaciones,Baños)
        objeto2.ImprimirInfo2()
        print("1= Seguir en el programa" )
        print("2=No seguir en el programa" )
        seleccion=int(input("Deseas seguir con el programa :"))