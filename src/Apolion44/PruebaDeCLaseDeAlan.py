from ClasesDeAlan import Galleta 
from ClasesDeAlan import soda
from ClasesDeAlan import papas

nombreDeGalleta = input("dime como se llama tu galleta favorita? ")
saborGalleta = input("de que sabor es? ")

muestraGalleta = Galleta(nombreDeGalleta,saborGalleta)
mostrar= muestraGalleta.ImpresionDeGalleta()

nombreDePapas = input("dime como se llaman tus papas favorita? ")
saborPapas = input("de que sabor es? ")

muestraPapas = papas(nombreDePapas,saborPapas)
mostrar= muestraPapas.ImpresionDePapas()

nombreDeSoda = input("dime como se llama tu soda favorita? ")
saborSoda = input("de que sabor es? ")

muestraSoda = soda(nombreDeSoda,saborSoda)
mostrar= muestraSoda.ImpresionDeSoda()
