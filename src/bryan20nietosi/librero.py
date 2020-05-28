class Alumno:
    def __init__(self,nombre,apellido):
        self.__a=nombre
        self.__b=apellido
    @property 
    def nombre(self):
        return {self.__a}
    @nombre.setter
    def nombre(self,valor):
        self.__a=valor
    @property 
    def apellido(self):
        return {self.__b}
    @apellido.setter
    def apellido(self,valor):
        self.__b=valor
    def Info(self):
        return f"Nombre: {self.__a}, Apellidos: {self.__b}"
class Escuela:
    def __init__(self,nombre,ciudad):
        self.__n=nombre
        self.__c=ciudad
    @property
    def n(self):
        return "{self.__n}"
    @n.setter 
    def n(self, valor):
        self.__n=valor
    @property
    def c(self):
        return "{self.__c}"
    @c.setter 
    def c(self, valor):
        self.__c=valor
    def Info(self):
        return f"Escuela: {self.__n}, Ciudad: {self.__c}"
class Facultad:
    def __init__(self,nombre,carrera,ciudad):
        self.__n=nombre
        self.__c=carrera
        self.__ci=ciudad
    @property
    def n(self):
        return "{self.__n}"
    @n.setter
    def n(self,valor):
        self.__n=valor
    @property
    def c(self):
        return "{self.__c}"
    @c.setter
    def c(self,valor):
        self.__c=valor
    @property
    def ci(self):
        return "{self.__ci}"
    @ci.setter
    def ci(self,valor):
        self.__ci=valor
    def Info(self):
        return f"Facultad: {self.__n}, Carrera: {self.__c}, Ciudad: {self.__ci}"
