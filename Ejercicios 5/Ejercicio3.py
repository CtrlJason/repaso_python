numero_user = int(input("Escriba un numero entero: "))
num_inicial = 1
num_triangulo = []
resultado = 0
for n in range(0, numero_user):
    num_triangulo.insert(0, num_inicial)
    num_inicial = num_inicial + 2
    print(num_triangulo)

# n = int(input("Introduce la altura del triangulo: "))

# for i in range(1, n+1, 2):
#     for j in range(i, 0, -2):
#         print(j, end=" ")

#     print("")
