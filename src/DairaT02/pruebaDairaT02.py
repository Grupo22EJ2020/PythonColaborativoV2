from clasesDairaT02 import bolso
from clasesDairaT02 import blusa
from clasesDairaT02 import Auto

print("1.-Bolso")
print("2.-Blusa")
print("3.-Auto")

opcion = input("Elija la opcion a registrar")

opcion == 1:
    colorbolso = input("color del bolso")
    marcabolso = input("marca del bolso")
    tambolso = input("tamaño del bolso")
    bolso=bolso(color,marca,tamaño)
        bolso.imprimirBolso()

opcion == 2:
    colorblusa = input("color de blusa")
    marcablusa = input("marca de blusa")
    tamblusa = input("talla de blusa")
    blusa=blusa(color,marca,talla)
        blusa.imprimirBlusa()

opcion == 3:
    modeloauto = input("modelo del auto")
    color = input("color del auto")
    año = input("año del auto")
    auto=auto(modelo,color,año)
        Auto.imprimirAuto()