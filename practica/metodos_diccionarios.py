diccionario = {
    "Nombre": "Yeison Mosquera",
    "Apellido": "Mosquera",
    "Estado": "Activo"
}

diccionario2 = {
    "Nombre": "Sebastian",
    "Cedela": 10000000
}

resultado = dir(diccionario)

print(resultado)
print(len(diccionario))
# Clear elimina el contenido de el diccionario
# diccionario.clear()

# Get se usa para obtener un valor espesifico del diccionario
print(diccionario.get("Nombre"))

# Items me devuelve el contenido del diccionario
print(diccionario.items())

# Keys me devuelve las llaves del diccionario
print(diccionario.keys())

# pop eliminar la clave y el valor del diccionario
diccionario.pop("Nombre")
print(diccionario)

diccionario.update(diccionario2)

print(diccionario)
