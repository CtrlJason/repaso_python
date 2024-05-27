cadena1 = "bienvenidos"
cadena2 = "Despedida"

resultado = cadena1.capitalize()
print(resultado)

resultado = cadena1.encode()
print(resultado)

# .center funciona para centrar el resultado de print
# ljust justificar a la izquierda
# rjust justificar a la derecha
resultado = cadena1.center(50)
print(resultado)

# swapcase convierte minusculas a mayusculas y viseversa
conversion = cadena2.swapcase()
print(conversion)

cadena3 = "  bienvenidos  a  python"
resultado_espacios = cadena3.strip()
print(resultado_espacios)

resultado_espacios = cadena3.lstrip()
print(resultado_espacios)

cadena3 = cadena3.replace("bienvenidos", "welcome")
print(cadena3)
