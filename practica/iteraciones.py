# x = 2
# x = x + 2

# Range es para poner numeros donde el primer indice muestra el comienzo el segundo hasta donde termina y el tercero el numero de saltos
# print(list(range(0, -51, -10)))

nombres = [["Yeison", "Carlos", "Juan", "Laura"]]
# Recorre todos los indices y los imprime
for nombre in nombres:
    print(nombre)

numeros = [[10, 15, 990, 12358, 32125603, 1]]

for numero in numeros:
    print(numero)

productos = ["papa", "yuka", "platano", "leche"]
cantidad = [12, 4, 8, 9]

# Zip se utiliza para recorrer 2 elementos en paralelo
for almuerzo, cantidad_almuerzo in zip(productos, cantidad):
    print(f"Comprar {almuerzo}: {cantidad_almuerzo}")


numeros_2 = [12, 10, 8, 10]

# enumerate muestra el indice con el 0 y muestra la posicion con el 1 (valor)
for num in enumerate(numeros_2):
    indice = num[0]
    valor = num[1]
    print(f"El idndice es: {indice} y el valor es: {valor}")

numeros_3 = [1, 2, 3, 4, 5, 6]

for n in numeros_3:
    if n == 7:
        print("El numero 7 se encuentra edentro de la lista")
        break
# else de for sirve para realizar acciones en caso de que el if dentro del for no cumpla su funcion
else:
    print("No se encontró el numero 7")

objetos = {
    "Nombre": "Yeison",
    "Apellido": "Mosquera",
    "Edad": 23,
    "Genero": "Masculino"
}

# Para recorrer un diccionario y obtener la clave y el valor utilizamos el metodo items donde si le ponemos en el rango 0 toma las llaves y si ponemos el 1 toma los valores
for datos in objetos.items():
    key = datos[0]
    valor = datos[1]
    print(f"La clave es: {key} y el valor es: {valor}")

# Para recorrer diccionario y obtener solo las claves
for datos in objetos:
    print(f"La clave es {datos}")

frutas = ["banano", "manzana", "ciruela", "pera",
          "naranja", "granadilla", "durazno", "patilla"]

# Evitando que Andres se coma una manzana con la sentencia continue
print(f"Dice Andres me voy a comer")
for fruta in frutas:
    if frutas == "manzana":
        continue
    print(f"un(a) {fruta}")

frutas = ["banano", "manzana", "ciruela", "pera",
          "naranja", "granadilla", "durazno", "patilla"]

# Evitando que Andres como mas frutas (por break tampoco se ejecuta else:)
print(f"Dice andres me voy a comer ")
for fruta in frutas:
    if fruta == "ciruela":
        break
    print(f"un(a) {fruta}")
