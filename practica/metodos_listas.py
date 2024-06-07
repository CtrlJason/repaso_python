juguetes = ["carro", "muñeca"]

print(juguetes)

# Se usa append para agregar un elemento al final de una lista
juguetes.append("piano")

print(juguetes)

# Se usa extend para poner varios o muchos elementos a una lista
# juguetes.extend((["helicoptero", "camion", "barco", "guitarra"]))

# Con insert podemos introducir unicamente un elemento en un lugar espesifico
juguetes.insert(2, "reloj")

print(juguetes)

juguetes.remove("muñeca")

print(juguetes)

# Con pop podemos eliminar un elemento por su indice
juguetes.pop(0)

print(juguetes)

juguetes.extend((["helicoptero", "camion", "barco", "guitarra"]))

print(juguetes)

juguetes.reverse()

print(juguetes)

# Se usa sort sirve para organizar de menor a mayor y si le ponemos (revers=True) cambia la orientacion de mayor a menor
juguetes.sort(reverse=True)

print(juguetes)

# Se usa para saber en que indice aparece el elemento dentro de la lista
print(juguetes.index("barco"))

# Se usa conunt para saber el numero de veces que sale el elemento en la lista
print(juguetes.count("barco"))

# para eliminar todos los elementos de una lista se utiliza clear
# juguetes.clear()
