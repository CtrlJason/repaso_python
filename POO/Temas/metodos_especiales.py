class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    # __str__ está diseñado para producir una representación amigable y legible para el usuario.
    def __str__(self): # Se usa para definir como mostrar el objeto como cadena de texto para mostralo posterior mente en consola
        return 'Persona(nombre={self.nombre},edad={self.edad})'
    
    def __repr__(self): # repr es para producir una representacion para los desarrolladores
        return f'Persona("{self.nombre}",{self.edad})' # le ponemos comillas al dato que sea un string
    
    
nombre = Persona("Yeison", 23)

representacion = repr(nombre) # Se tranforma representacion a un objeto repr y le asignamos el objeto nombre
resultado = eval(representacion) # toma una cadena que contiene una expresión Python y la evalúa como si fuera una expresión escrita directamente en el código.

print(representacion)
print(resultado)
print(resultado.nombre) # se pone .atributo del objeto para obtener el atributo