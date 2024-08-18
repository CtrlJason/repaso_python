import csv

with open("archivos\\datos2.csv") as datos: #"with" es una forma optima de abrir archivos y usamos "as" para renombrar
    leer_datos = csv.reader(datos)
    for info in leer_datos:
        print(info)