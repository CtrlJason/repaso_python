frutas = ["manzana", "mango", "banano"]
frutas.append("mora")
print(frutas)

frutas.pop(2)
print(f"{frutas} cantidad: {len(frutas)}")

frutas.remove("manzana")
print(frutas)

frutas.insert(2, "guanabana")
print(frutas)

frutas.insert(1, (["pera", "guayaba"]))
print(frutas)

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
fila_1 = matriz[0]
fila_2 = matriz[1]

elemento = matriz[0][1]

print(f"Fila 1: {fila_1} Fila 2: {
      fila_2} El numero de la fila 1 posicion 2 es: {elemento}")
