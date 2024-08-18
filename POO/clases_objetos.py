class Celular:
    def __init__(self, marca, modelo, camara): #self hace referencia a un objeto instanciado de la clase - Seguido le ponemos los atributos que queremos para los objetos
        # La funcion se ejecuta automaticamente cuando creamos un objeto instanciado de la clase
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
celular1 = Celular(modelo= "S23", marca="Samsung", camara= "48MP") #Forma 1 de asignar los atributos: nombre del atributo = nombre del atributo - El orden se puede cambiar
celular2 = Celular("Iphone", "15 Pro max", "46MP")#Forma 2 de asignar atributos: se pone directamente el nombre del atributo y python lo asigna al espacio automaticamente
celular3 = Celular("Huawei", "P20 Lite", "42MP")
celular4 = Celular("Iphone", "11", "22MP")
celulares_bodega = [celular1, celular2, celular3, celular4]

print(len(celulares_bodega))




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
