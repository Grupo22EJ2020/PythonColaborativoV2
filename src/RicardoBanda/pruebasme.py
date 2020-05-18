from clasesme import suma
from clasesme import Carro
from clasesme import Videos
While True:
num1=int(input("Dame el numero1"))
num2=int(input("Dame el numero2"))
respuesta=suma(num1,num2)
imprimir=respuesta.suma()
print(imprimir)
break

color=input("¿De que color es?")
marca=input("¿De que marca es?")
transmicion=input("¿Cual es su transmicion?")
respueta=Carro(color,marca,transmicion)
info=carro.infocarro()
print(info)

duracion=input("¿Cuanto dura el video?")
titulo=input("¿Cuanto tiempo dura?")
reproducciones=input("¿Cuantas reproduccuiones tiene?")
respuesta=Video(duracion,titulo,reproducciones)
info=video.infovideo()
print(info)