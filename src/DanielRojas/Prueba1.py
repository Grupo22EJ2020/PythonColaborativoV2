from Clases import Playera
from Clases import Pantalon
from Clases import Zapatos



seleccion=1

while seleccion==1:
    print("1=Quiero seleccionar la clase Playera ")
    print("2=Quiero seleccionar la clase Pantalon")
    print("3=Quiero seleccionar la clase Zapatos")
    opcion=int(input(":"))
    if opcion==1:
        color=(input("Dime el color de Playera : "))
        marca=(input("Dime la marca de la Playera :"))
        talla=(input("Dime la talla de la Playera : "))
        objeto=Playera(color,marca,talla)
        objeto.imprimirInfo()
        print("1= Si quiero seguir con el programa" )
        print("2=No quiero seguir con el programa" )
        seleccion=int(input("Deseas seguir con el programa :"))

    elif opcion==2:
        talla=(input("Dime la talla del Pantalon:"))
        marca=(input("Dime la marca del Pantalon : "))
        color=(input("Dime el color del Pantalon"))
        objeto1=Pantalon(talla,marca,color)
        objeto1.ImprimirInfo()
        print("1= Si quiero seguir con el programa" )
        print("2=No quiero seguir con el programa" )
        seleccion=int(input("Deseas seguir con el programa :"))
    
    elif opcion==3:
        modelo=(input("Dime el modelo de los Zapatos:"))
        marca=(input("Dime la marca de los Zapatos:"))
        costo=(int(input("Dime el costo de los Zapatos")))
        objeto2=Zapatos(modelo,marca,costo)
        objeto2.ImprimirInfo2()
        print("1= Si quiero seguir con el programa" )
        print("2=No quiero seguir con el programa" )
        seleccion=int(input("Deseas seguir con el programa :"))

