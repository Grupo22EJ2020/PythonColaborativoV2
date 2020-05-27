from codigoprincipal import PC
from codigoprincipal import Nieve
from codigoprincipal import Teclado

print("CLASE PC")
Ram = input("¿Cuanta ram tiene tu pc? ")
Procesador = input("¿Que procesador tiene tu pc? ")

mostrar = PC(Ram,Procesador)
mostrarPC= mostrar.imprimirpc()

print("CLASE NIEVE")
Sabor = input("¿De que sabor es? ")
Envase = input("¿Con o sin envase?")
Precio = input("¿Qué precio tiene?") 

mostrar2 = Nieve(Sabor,Envase,Precio)
mostrarNIEVE = mostrar2.imprimirNIEVE()

print("CLASE Teclado")
PrecioT = input("¿Que precio tiene? ")
Marca = input("¿Que marca es?")
Modelo = input("¿Que modelo es?") 

mostrar3 = Teclado(PrecioT,Marca,Modelo)
mostrarTECLAOD = mostrar3.imprimirTECLADO()
