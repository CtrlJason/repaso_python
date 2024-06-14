tienda = {
    "Platano": 1.35,
    "Manzana": 0.80,
    "Pera": 0.85,
    "Naranja": 0.90
}

# fruta = int(input(
#     "Para consultar el precio por kilo elija una de las siguientes frutas (digite el numero): [1]platano, [2]manzana, [3]pera o [4]naranja: "))
# nkilos = float(
#     input("Ahora escriba la canidad de kilos para saber el costo: "))

# if fruta == 1:
#     total = nkilos * tienda.get("platano")
#     print(f"El total de kilos seleccionado es de: {
#           nkilos}k y el precio total del platano es de: ${total}")
# if fruta == 2:
#     total = nkilos * tienda.get("manzana")
#     print(f"El total de kilos seleccionado es de: {
#           nkilos}k y el precio total de la manzana es de: ${total}")
# if fruta == 3:
#     total = nkilos * tienda.get("pera")
#     print(f"El total de kilos seleccionado es de: {
#           nkilos}k y el precio total del pera es de: ${total}")
# if fruta == 4:
#     total = nkilos * tienda.get("naranja")
#     print(f"El total de kilos seleccionado es de: {
#           nkilos}k y el precio total del naranja es de: ${total}")
# else:
#     print("La fruta seleccionada no existe en la base de datos")

# title convierte la primera letra en mayuscula
# Se pueden usar varios metodos en una misma variable
fruta = input("¿Qué frutas quieres? ").lower().title()
kg = float(input("¿Cuantos kilos? "))

if fruta in tienda:
    print(f"{kg} kilos de {fruta} valen {tienda[fruta]*kg}$ ")
else:
    print("La fruta no se encuentra en la base de datos")
