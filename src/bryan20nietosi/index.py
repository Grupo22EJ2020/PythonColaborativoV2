from librero import Alumno, Escuela, Facultad
cantidad=int(input("Cantidad de alumnos: "))
lista=[]
for i in range(1,cantidad+1):
    input(f"Alumno numero: {i}\n Enter para continuar...")
    nom=input(f"Nombre alumno: ")
    ape=input("Apellidos: ")
    escuela=input(f"Nombre de Escuela: ")
    ciudad=input(f"Ciudad: ")
    facultad=input("Nombre de Facultad: ")
    carrera_facultad=input("Nombre de Carrera: ")
    ciudad_facultad=input("Ciudad de origen de Facultad: ")
    nombre=Alumno(nom,ape)
    provincia=Escuela(escuela,ciudad)
    profesion=Facultad(facultad,carrera_facultad,ciudad_facultad)
    print(nombre.Info())
    print(provincia.Info())
    print(profesion.Info())
    input("Enter para continuar...")