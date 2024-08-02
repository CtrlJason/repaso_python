tupla = (["hola", "adios", 2, 99, 2.39], [45, "hola", "adios"])

for listas in tupla:
    print(tupla[0][1])

numeros = 1, 2, 3, 4, 5
sub_tupla = numeros[1:4]
print(sub_tupla)

frutas = ("naranja", "pera", "mango")
frutas_carrito = frutas[0:3]
print(frutas_carrito)


tupla[0].pop(0)

print(tupla)
