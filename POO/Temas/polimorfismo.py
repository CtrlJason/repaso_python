class Animal(): # -> Tipo real, es el origen del objeto
    pass

class Gato(Animal): # -> Tipo declarado es la herencia del objeto padre
    def sonido(self): # -> Metodo sonido - polimorfismo
        return "Miau"
    
class Perro(Animal):
    def sonido(self): # -> Metodo sonido - polimorfismo
        return "Guau"
    
#--------------------------------------------------#
gato = Gato() # Instanciamos el objeto de la clase
perro = Perro()
#--------------------------------------------------#

def hacer_sonido(animal):
    print(animal.sonido()) # Llamamos la funcion almacenada con su sonido caracteristico
    
#--------------------------------------------------#
hacer_sonido(gato) # almacenamos el objeto en la funcion hacer sonido
hacer_sonido(perro)
#--------------------------------------------------#
# print(gato.sonido())
# print(perro.sonido())