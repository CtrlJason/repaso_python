# Escribir un programa que pida al usuario un numero entero positivo y muestre por pantalla la cuenta atras desde ese numero hasta cero separados por comas
# Escribir un programa que pida al usuario un numero entero y muestre por pantalla un triangulo rectangulo como el de abajo. de altura el numero introducido

numero_entero = int(input("Escriba un numero entero positivo: "))
cuenta_atras = []
for n in range(numero_entero, 0, -1):
    cuenta_atras.append(n-1)
    cuenta_atras.append(",")

print(cuenta_atras)
