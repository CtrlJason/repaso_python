contraseña = input("Cree una contraseña: ")
verificador = input("Escriba su contraseña para iniciar sesion: ")

contraseña = contraseña.lower()
verificador = verificador.lower()

if verificador == contraseña:
    print("Ha iniciado sesion con exito")
else:
    print("Su contraseña es incorrecta")
