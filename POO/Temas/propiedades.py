class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre # Se usa una barra baja para volver un dato privado y asi encapsularlo para que no se pueda acceder al mismo. Si se ponen 2 barras bajas seria privado - privado
        self._edad = edad

    @property # el @property se usa para que el objeto instanciado al invocarlo se llame como una propiedad osea no es necesario porner parentecis.
    def nombre(self): # lo toma automaticamente como un get = obtener - Esta es una forma correcta de acceder a datos privados o muy privado (este ultimo solo se puede directamente de la clase)
        return self._nombre
    
    @nombre.setter # Se usa para cambiar
    def nombre(self, new_nombre):
        self._nombre = new_nombre
        
    @nombre.deleter # Se usa para eliminar
    def nombre(self): # lo toma automaticamente como un del = eliminar - Esta es una forma correcta de acceder a datos privados o muy privado (este ultimo solo se puede directamente de la clase)
        del self._nombre
    
    def get_edad(self):
        return self._edad
    

yeison = Persona("yeison", 23)

nombre = yeison.nombre # Aqui lo utilizamos con @property, sin parentecis y se llama de igual forma la funcion
edad = yeison.get_edad() # Aqui lo utilizamos sin @property, tendriamos que poner la funcion completa para llamarla
print(nombre, edad)

yeison.nombre = "Jason" # Aqui utilizamos @nombre.setter para modificar (decorador modificador)
nombre = yeison.nombre # Re escribimos la variable nombre con el nuevo dato
print(nombre, edad)

del yeison.nombre # Ahora la propiedad no existe, si intento acceder a ella sale un error

