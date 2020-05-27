from codigoprincipal import PC
from codigoprincipal import Helado
from codigoprincipal import Teclado


Ram = input("¿Cuanta ram tiene tu pc? ")
Procesador = input("Procesador: ")

mostrar = PC(Ram,Procesador)
mostrarPC= mostrar.imprimirpc()

print("Helado")
Sabor = input("¿Sabor ")
Envase = input("Tipo de envase")
Precio = input("precio") 

mostrar2 = Helado(Sabor,Envase,Precio)
mostrarNIEVE = mostrar2.imprimirHelado()

print("Teclado")
PrecioT = input("¿Que precio tiene? ")
Marca = input("¿Que marca es?")
Modelo = input("¿Que modelo es?") 

mostrar3 = Teclado(PrecioT,Marca,Modelo)
mostrarTECLADO = mostrar3.imprimirTECLADO()
