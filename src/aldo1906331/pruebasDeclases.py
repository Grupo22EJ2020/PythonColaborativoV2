from clases import Jugo
from clases import Videojuego
from clases import fruta


marcaJugo = input("Que marca es tu jugo favorito? ")
saborJugo = input("Que sabor tiene tu jugo favorito? ")
imprimes = Jugo (marcaJugo,saborJugo)
enseña= imprimes.imprimirJugo()

modovideojuego = input("Dime que metodo de juego es tu favorito? ")
Tipodejuego = input("Que tipo de juego te gusta jugar? ")
imprimes = Videojuego (modovideojuego,Tipodejuego)
enseña= imprimes.imprimirJuego()

tamañofruta = input("De que tamaño te gusta la fruta? ")
tipodefruta = input("Que tipo de fruta es la mejor? ")
imprimes = fruta (tamañofruta,tipodefruta)
enseña= imprimes.imprimirlafruta()



