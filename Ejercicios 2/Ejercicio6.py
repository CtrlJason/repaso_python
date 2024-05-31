nombre = input("Como te llamas: ")
sexo = int(input("Cual es tu sexo 1 Femenino 2 Masculino: "))
grupoA = "abcdefghijkmnñopqrstuvwxyz"

nombre = nombre.lower()

if nombre[0] != "m" and nombre[0] != "n" and nombre[0] < grupoA[11]:
    if sexo == 1:
        print("Perteneces al grupo A Femenino")
    if sexo == 2:
        print("Perteneces al grupo A Masculino")
if nombre[0] != "m" and nombre[0] != "n" and nombre[0] > grupoA[12]:
    if sexo == 1:
        print("Perteneces al grupo A Femenino")
    if sexo == 2:
        print("Perteneces al grupo A Masculino")
else:
    if sexo == 1:
        print("Perteneces al grupo B Femenino")
    if sexo == 2:
        print("Perteneces al grupo B Masculino")
