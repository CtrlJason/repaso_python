class Animal():
    def comer(self):
        print("comiendo")
    
class Mamifero(Animal): # Hereda los metodos de Animal
    def amamantar(self):
        print("amamantando")
    
class Ave(Animal): # Hereda los metodos de Animal
    def volar(self):
        print("volando")
    
class Murcielago(Mamifero, Ave): # Hereda los metodos de Mamifero y Ave y a su vez los metodos de Animal en arbol
    pass
animal = Murcielago()

animal.comer()
animal.amamantar()
animal.volar()

print(Murcielago.mro()) # Para ver las clases que hereda y el orden