primer_nombre = input("Escriba su primer nombre: ")
segundo_nombre = input("Escriba su segundo nombre: ")
primer_apellido = input("Escriba su primer apellido: ")
segundo_apellido = input("Escriba su segundo apellido: ")

primer_nombre = primer_nombre.lower()
segundo_nombre = segundo_nombre.lower()
primer_apellido = primer_apellido.lower()
segundo_apellido = segundo_apellido.lower()

print(primer_nombre + " " + segundo_nombre + " " +
      primer_apellido + " " + segundo_apellido)
print(primer_nombre.upper() + " " + segundo_nombre.upper() + " " +
      primer_apellido.upper() + " " + segundo_apellido.upper())
print(primer_nombre.capitalize() + " " + segundo_nombre.capitalize() + " " +
      primer_apellido.capitalize() + " " + segundo_apellido.capitalize())
