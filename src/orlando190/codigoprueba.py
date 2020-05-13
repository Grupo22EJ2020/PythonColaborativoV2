from codigoprincipal import PC
procesador = input("¿Que procesador tiene tu PC?: ")
ram = input("¿Cuanta ram tiene tu PC?: ")

mostrarcomponentes= PC(procesador,ram)
mostrar2= mostrarcomponentes.imprimirInfo()