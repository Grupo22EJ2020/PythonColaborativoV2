from librero import bryan20nietosi
cantidad=int(input("Dame una cantidad de veces a sumar 2 numeros: "))
i=1
while i<= cantidad:    
    numero=int(input("Dame el numero 1: "))
    numero2=int(input("Dame el numero 2:"))
    suma=bryan20nietosi(numero,numero2)
    impresion=suma.sumatoria()
    i+=1
    print(impresion)
