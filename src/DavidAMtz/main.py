from misclases import Gorra
from misclases import Television
from misclases import Pulsera

while True 

    print("**Menu Inicial**")
    print("1.-Gorra\n")
    print("2.-Television\n")
    print("3.-Pulsera\n")

    claseSeleccionada=int(input("\n¿Cual es la clase a seleccionar?: "))

    if claseSeleccionada == 1:
        diseño=(input("Dime el diseño de la Gorra: "))
        talla=(input("Dime la talla de la Gorra: "))
        color=(input("Dime el color de la Gorra: "))
        g=Gorra(diseño, talla, color)
        g.ImprimirInfo()
        input("\nPresiona enter para continuar...\n")

    if claseSeleccionada == 2:
        marca=(input("Dime la marca de la T.V.: "))
        pulgadas=int(input("Dime las pulgadas de la T.V.: "))
        modelo=(input("Dime el modelo de la T.V.: "))
        tv=Television(marca, pulgadas, modelo)
        tv.ImprimirInfo()
        input("\nPresiona enter para continuar...\n")
        












        
     




      
