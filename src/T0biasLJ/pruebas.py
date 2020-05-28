from clasesmias import Multiplicacion
from clasesmias import Deportista
while True:
    numero1=int(input("Dame el primer numero: "))
    numero2= int(input("Dame el segundo numero: "))
    respuesta=Multiplicacion(numero1,numero2)
    imprimir=respuesta.multi()
    print(imprimir)
    break

deporte=input("En que deporte esta?:")
peso=int(input("Cuanto pesa?:"))
edad=int(input("Cuantos años tiene?"))
persona= Deportista(deporte,peso,edad)
info=persona.infodep()
print(info)