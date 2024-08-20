class Persona(): # Super clase
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def datos(self):
        print(f"Tu nombre es {self.nombre} y tu edad es {self.edad} años")
        
class Estudiante(Persona): # Sub clase
    def __init__(self, nombre, edad, grado): # Se ponen todos los atributos que se quieren (Obligatoriamente se deben de poner todos los atributos de la super clase)
        super().__init__(nombre, edad) # Se ponen todos los atributos que heredan de la super clase
        self.grado = grado
    
    def curso(self):
        print(f"Su curso actual es {self.grado}")

carlos = Estudiante("Carlos", 22, "4 Grado") # Se crea el objeto y se asignan sus atributos

carlos.datos()
carlos.curso()