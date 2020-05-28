from Misclases import Blusa
from Misclases import Bolsa
from Misclases import Zapatos

menu=int(input("Con el numero 1 entras al programa y con el 2 te sales: "))
while menu==1:
    print ("**Menu Inicial**")
    print ("1.-Blusa\n")
    print ("2.-Bolsa\n")
    print ("3.-Zapatos\n")
    
    claseSeleccionada=int(input("\n¿Que clase desea seleccionar?: "))
    
    if claseSeleccionada == 1:
        talla=(input("Dime la talla de la blusa: "))
        color=(input("Dime el color de la blusa: "))
        b=Blusa(talla, color)
        b.Imprimirinfo()
        menu=int(input("Si desea seguir con el programa ponga 1 y ponga 2 para terminar: "))
    
    elif claseSeleccionada == 2:
        tamaño=(input("Dime el tamaño de la bolsa: "))
        color=(input("Dime el color de la bolsa: "))
        marca=(input("Dime la marca de la bolsa: "))
        bo=Bolsa(tamaño, color, marca)
        bo.Caracteristicas()
        menu=int(input("Si desea seguir con el programa ponga 1 y ponga 2 para terminar: "))
    
    elif claseSeleccionada == 3:
        talla=(input("Dime la talla de los zapatos: "))
        color=(input("Dime el color de los zapatos: "))
        z=Zapatos(talla, color)
        z.Informacion()
        menu=int(input("Si desea seguir con el programa ponga 1 y ponga 2 para terminar: "))


