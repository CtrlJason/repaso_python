# Datos simples

nombre = "yeison"
apellido = "mosquera"
edad = 23

bienvenido = f"Hola {nombre} {apellido} como estas?"

print(bienvenido)
print(len(nombre))
print(apellido[0:5:2])
print(nombre in bienvenido)
print("Daniel" in bienvenido)
print("Daniel" not in bienvenido)

# Datos compuestos

lista = ["yeison", "mosquera", True, 23]  # Se puede ver y modificar
tupla = ("yeison", "mosquera", True, 23)  # Solo se puede ver
conjunto = {"yeison", "mosquera", True, 23}  # No se puede ni ver ni modificar
print(lista[1])

# Crear diccionario
diccionario = {
    "Nombre": "Yeison",
    "Apellido": "Mosquera",
    "Actividad": "True",
    "Edad": 23
}
print(diccionario["Nombre"])
