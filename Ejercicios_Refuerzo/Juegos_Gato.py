tablero = [["#", "#", "#"], ["#", "#", "#"], ["#", "#", "#"]]

for fila1 in tablero:
    print(fila1)
fin = False
while fin != True:
    ######  JUGADOR 1  ######
    fila_user = int(input("Jugardor 1: Escribe la posicion del 1 al 9: "))
    if fila_user == 1:
        tablero[0][0] = "X"
    elif fila_user == 2:
        tablero[0][1] = "X"
    elif fila_user == 3:
        tablero[0][2] = "X"
    elif fila_user == 4:
        tablero[1][0] = "X"
    elif fila_user == 5:
        tablero[1][1] = "X"
    elif fila_user == 6:
        tablero[1][2] = "X"
    elif fila_user == 7:
        tablero[2][0] = "X"
    elif fila_user == 8:
        tablero[2][1] = "X"
    elif fila_user == 9:
        tablero[2][2] = "X"
    for i in tablero:
        print(fila1)
    ######  JUGADOR 2  ######
    fila_posicion = int(input("Jugador 2: Escribe la posicion del 1 al 9: "))
    if fila_user == 1:
        tablero[0][0] = "O"
    elif fila_user == 2:
        tablero[0][1] = "O"
    elif fila_user == 3:
        tablero[0][2] = "O"
    elif fila_user == 4:
        tablero[1][0] = "O"
    elif fila_user == 5:
        tablero[1][1] = "O"
    elif fila_user == 6:
        tablero[1][2] = "O"
    elif fila_user == 7:
        tablero[2][0] = "O"
    elif fila_user == 8:
        tablero[2][1] = "O"
    elif fila_user == 9:
        tablero[2][2] = "O"
    for j in tablero[0]:
        print(fila1)
    ######  FINALIZACION  ######
    user_fin = int(
        input("si desea terminar el juego escriba 0 de lo contrario escriba 1"))
    if user_fin == 0:
        fin = True
    elif user_fin == 1:
        fin = False
