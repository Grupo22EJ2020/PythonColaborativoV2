from clasesmias import Multiplicacion
while True:
    numero1=int(input("Dame el primer numero: "))
    numero2= int(input("Dame el segundo numero: "))
    respuesta=Multiplicacion(numero1,numero2)
    imprimir=respuesta.multi()
    print(imprimir)
    break