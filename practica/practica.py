# edad = int(input("Que edad tiene?: "))

# if edad >= 18:
#     print("Usted es mayor de edad")
# else:
#     print("Usted es menor de edad")


numero1 = int(input("Escriba el primer numero para relizar una division: "))
numero2 = int(input("Escriba el segundo numero para relizar una division: "))
resultado = numero1 / numero2

if numero2 == 0:
    print("No se puede divir entre 0")
else:
    print(f"el resultado es: {round(resultado)}")
