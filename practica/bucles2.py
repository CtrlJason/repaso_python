
bitcoins = [2, 9, 4, 0, 3, 8]

# Multiplicacion x2 cada uno de los indices de la lista con for
# bitcoins_duplicados = []
# for num in bitcoins:
#     bitcoins_duplicados.append(num*2)
# print(bitcoins_duplicados)

# Multiplicamos x2 cada indice de la lista bitcoins con un for en una sola linea. Se bede poner la operacion antes de iterarla
bitcoins_duplicados = [n*2 for n in bitcoins]
print(bitcoins_duplicados)
