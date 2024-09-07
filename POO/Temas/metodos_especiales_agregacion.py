class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __add__(self, otro):
        valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre, valor)

yeison = Persona("Jason", 23)
daniel = Persona("daniel", 20)

resultado = yeison + daniel
print(resultado.edad)