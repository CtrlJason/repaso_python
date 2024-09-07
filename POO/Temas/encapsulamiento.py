class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre # Se usa una barra baja para volver un dato privado y asi encapsularlo para que no se pueda acceder al mismo. Si se ponen 2 barras bajas seria privado - privado
        self._edad = edad

    def get_nombre(self): # get = obtener - Esta es una forma correcta de acceder a datos privados o muy privado (este ultimo solo se puede directamente de la clase)
        return self.__nombre
    
    def get_edad(self):
        return self._edad
    
    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre # set = definir - Se utiliza set_ para redefinir datos encapsulados . Privado o muy privado

yeison = Persona("yeison", 23)

nombre = yeison.get_nombre()
print(nombre)

yeison.set_nombre("Jason")

nombre = yeison.get_nombre()
edad = yeison.get_edad()
print(nombre, edad)

# yeison.__nombre # Esta es una forma incorrecta de llamar una variable muy privada (doble barra baja), unicamente se puede hacer desde la clase no fuera de ella.
# yeison = Persona(nombre="Yeison", edad= 23)
# print(yeison._edad, yeison._nombre) # para acceder a la informacion de una variable privada se debe colocar igual, con una barra baja pero no es lo correcto