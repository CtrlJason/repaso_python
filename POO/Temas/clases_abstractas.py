from abc import ABC, abstractmethod
#     ↑ modulo   ↑ clase    ↑ decorador

class Persona(ABC): # Al poner el parametro ABC convertimos una clase en una platilla (clase abstracta)
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    
    @abstractmethod # Funcion con abstraccion se debe llamar desde una clase que hereda la superclase
    def estado(self):
        pass
    
    def presentarse(self): # funcion sin abstraccion, se puede llamar desde cualquier lugar
        print(f"Hola, me llamo: {self.nombre} mi edad es {self.edad}")
        
# yeison = Persona("Jason", 23, "Masculino", "Programador") # No se puede crear un objeto con una clase abstracta

class Estudiante(Persona): # tomamos la plantilla como parametro
    def __init__(self, nombre, edad, sexo, trabajo):
        super().__init__(nombre, edad, sexo, trabajo)
    
    def estado(self):
        print(f"El estudiante: {self.nombre} estudia: {self.actividad}")
# --------------------------------------------------------------------------------------- #
class Trabajador(Persona): # tomamos la plantilla como parametro
    def __init__(self, nombre, edad, sexo, trabajo):
        super().__init__(nombre, edad, sexo, trabajo)
    
    def estado(self):
        print(f"El trabajador: {self.nombre} trabaja en: {self.actividad}")
# Creamos los objetos
yeison = Estudiante("Jason",23,"masculino","programacion")
juan = Trabajador("Juan", 32, "masculino", "constructor")

# llamamos el estado de las personas (onjetos)
yeison.estado()
juan.estado()

# llamamos la funcion presentarse del sujeto(objeto)
yeison.presentarse()
juan.presentarse()