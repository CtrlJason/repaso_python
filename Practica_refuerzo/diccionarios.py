compras = {"pera": 2500, "arroz": 3200, "papa": 1500, "agua": 30000}

compras["azucar"] = 7200


compras2 = {"zanahora": 6300, "guayaba": 4900}
# print(compras)

compras2["factura"] = {"nombre": "Yeison", "apellido": "Mosquera", "edad": 23}
# print(f"La lista es:{compras2} y el dueño es: {compras2["factura"]["nombre"]}")

# for clave in compras2["factura"]:
#     print(clave)

# for valor in compras2.values():  # .vaules() muestra los valores de calla llave dentro del diccionario
#     print(valor)

# .items sirve para mostrar tanto la llave como el valor en un diccionario
for clave, valor in compras2["factura"].items():
    print(clave, valor)
