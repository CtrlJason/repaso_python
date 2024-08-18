class Celular:
    # Metodo construcctor se utiliza para crear atributos, para crearlo se define agrega un metodo especial con el nombre __init__
    def __init__(self, marca, modelo, camara): #self hace referencia a un objeto instanciado de la clase - Seguido le ponemos los atributos que queremos para los objetos
        # La funcion se ejecuta automaticamente cuando creamos un objeto instanciado de la clase
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
    def llamar_on(self): # Methodo que realiza la funcion de ejecutar una llamada
        print(f"Ejecutando llamada desde un: {self.marca, self.modelo}") # Para realizar un llamado al construcror siempre se debe referenciar con self para que el methodo se llame asi mismo
    def llamar_off(self): # Methodo que realiza la funcion de desactivar una llamada
        print(f"Desactivando llamada del : {self.marca, self.modelo}")   
        
celular1 = Celular(modelo= "S23", marca="Samsung", camara= "48MP") #Forma 1 de asignar los atributos: nombre del atributo = nombre del atributo - El orden se puede cambiar
celular2 = Celular("Iphone", "15 Pro max", "46MP")#Forma 2 de asignar atributos: se pone directamente el nombre del atributo y python lo asigna al espacio automaticamente
celular3 = Celular("Huawei", "P20 Lite", "42MP")
celular4 = Celular("Iphone", "11", "22MP")
celulares_bodega = [celular1, celular2, celular3, celular4]

celular1.llamar_on()
celular2.llamar_off()




# marcas = []
# modelos = []
# camaras = []

# for i in celulares_bodega: # Desempaquetado de la marca y modelo de los celulares
#     marcas.append(i.marca)
#     modelos.append(i.modelo)
# print(f"Las marcas de los celulares disponibles son: {marcas} \nLos modelos son: {modelos}")


# for i in celulares_bodega: # Imprimir marca modelo y camara con un bucle for
#     print(f"disponible: {i.marca, i.modelo, i.camara,}")

# print(f"Celulares:\n {[i for i in celulares_bodega]}") # Sacar los objetos de la lista celulares_bodega

# print([i.marca, i.modelo, i.camara] for i in celulares_bodega) # Sacar marca, modelo y camara con un bucle en una sola linea
# bodega = [[i.marca, i.modelo, i.camara] for i in celulares_bodega] # Guardado del bucle anterior en una variable
