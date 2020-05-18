from librero import Alumno
from librero import Calificacion
cantidad=int(input("Cantidad de alumnos: "))
lista=[]
for i in range(1,cantidad+1):
    nom=input(f"Nombre alumno {i}: ")
    ape=input("Apellidos: ")
    cal1=int(input(f"Cal1 de alumno {i}: "))
    cal2=int(input(f"Cal2 de alumno {i}: "))
    nombre=Alumno(nom,ape)
    prom=Calificacion(cal1,cal2)
    mostrar=nombre.Nombratura()
    promedio=prom.Promedio()
    lista.append(mostrar)
    lista.append(promedio)
print(lista)