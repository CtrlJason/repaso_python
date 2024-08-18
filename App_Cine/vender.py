# App para cine con: 1 menu principal 2 compra de boletos - usuario escoje el aciento 3 ver cantidad de ventas 4 salir de la app
def vender_user():
    sala = [["☐","☐","☐"],["☐","☐","☐"],["☐","☐","☐"]]
    user = int(input("Cuantos boletos desea vender: "))
    count = 0 # Contador de boletos
    fin = False
    for sillas in sala:
        print(sillas)
    while fin != True:
        user_silla = int(input("Escoja la silla en la posicion del 1 al 9: "))
        if user_silla == 1 and sala[0][0] == "☐":
            sala[0][0] = "☒"
        elif user_silla == 2 and sala[0][1] == "☐":
            sala[0][1] = "☒"
        elif user_silla == 3 and sala[0][2] == "☐":
            sala[0][2] = "☒"
        elif user_silla == 4 and sala[1][0] == "☐":
            sala[1][0] = "☒"
        elif user_silla == 5 and sala[1][1] == "☐":
            sala[1][1] = "☒"
        elif user_silla == 6 and sala[1][2] == "☐":
            sala[1][2] = "☒"
        elif user_silla == 7 and sala[2][0] == "☐":
            sala[2][0] = "☒"
        elif user_silla == 8 and sala[2][1] == "☐":
            sala[2][1] = "☒"
        elif user_silla == 9 and sala[2][2] == "☐":
            sala[2][2] = "☒"
        else:
            print("Esta silla ya se encuentra marcada, seleccione una diferente/n/n")
            
        for silla in sala:
            print(silla)
        count += 1
        if count == user:
            fin = True