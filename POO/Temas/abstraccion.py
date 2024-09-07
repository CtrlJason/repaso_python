class Auto():
    def __init__(self):
        self._estado = "apagado"
    
    def encender(self):
        self._estado = "encendido"
        print("El auto esta encendido")
    
    def conducir(self): # abstraccion, el usuario no sabe que hay una verificacion de por si el auto esta apagado que este se encienda. Busca ocultar la complejidad de un sistema
        if self._estado == "apagado":
            self.encender()
            print("Conduciendo el auto")

carro = Auto()
carro.conducir()
    