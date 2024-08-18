from vender import vender_user #El from nos sirve para traer unicamente un parte del codigo de lo que se quiere de otro modulo

def menu():
    actividad = False
    while actividad == False:
        user = int(input("Seleccione en el menu que desea realizar \n\n 1. Vender boletos\n 2. Ver informe\n 3. Salir del programa\n #: "))
        if user == 1:
            vender_user
        elif user == 2:
            vender_user
        elif user == 3:
            print("Ha salido del programa")
            actividad = True

menu()