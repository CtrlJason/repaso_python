tablero = [["#", "#", "#"], ["#", "#", "#"], ["#", "#", "#"]]

for mesa in tablero:
    print(mesa)

count = 0
fin = False

while True:
    fin = False
    fin2 = False
    ######  JUGADOR 1  ######
    while fin != True:
        Jugador_1 = int(input("Jugardor 1: Escribe la posicion del 1 al 9: "))
        if Jugador_1 == 1 and tablero[0][0] == "#":
            tablero[0][0] = "X"
            fin = True
        elif Jugador_1 == 2 and tablero[0][1] == "#":
            tablero[0][1] = "X"
            fin = True
        elif Jugador_1 == 3 and tablero[0][2] == "#":
            tablero[0][2] = "X"
            fin = True
        elif Jugador_1 == 4 and tablero[1][0] == "#":
            tablero[1][0] = "X"
            fin = True
        elif Jugador_1 == 5 and tablero[1][1] == "#":
            tablero[1][1] = "X"
            fin = True
        elif Jugador_1 == 6 and tablero[1][2] == "#":
            tablero[1][2] = "X"
            fin = True
        elif Jugador_1 == 7 and tablero[2][0] == "#":
            tablero[2][0] = "X"
            fin = True
        elif Jugador_1 == 8 and tablero[2][1] == "#":
            tablero[2][1] = "X"
            fin = True
        elif Jugador_1 == 9 and tablero[2][2] == "#":
            tablero[2][2] = "X"
            fin = True
        for mesa in tablero:
            print(mesa)

    ######  VERIFICADOR DE TRIQUI JUGADOR 1 ######

    if tablero[0][0] == "X" and tablero[1][0] == "X" and tablero[2][0] == "X":
        print("Jugador 1 ha ganado")
        break
    elif tablero[0][1] == "X" and tablero[1][1] == "X" and tablero[2][1] == "X":
        print("Jugador 1 ha ganado")
        break
    elif tablero[0][2] == "X" and tablero[1][2] == "X" and tablero[2][2] == "X":
        print("Jugador 1 ha ganado")
        break
    elif tablero[0][0] == "X" and tablero[0][1] == "X" and tablero[0][2] == "X":
        print("Jugador 1 ha ganado")
        break
    elif tablero[1][0] == "X" and tablero[1][1] == "X" and tablero[1][2] == "X":
        print("Jugador 1 ha ganado")
        break
    elif tablero[2][0] == "X" and tablero[2][1] == "X" and tablero[2][2] == "X":
        print("Jugador 1 ha ganado")
        break
    elif tablero[0][0] == "X" and tablero[1][1] == "X" and tablero[2][2] == "X":
        print("Jugador 1 ha ganado")
        break
    elif tablero[0][2] == "X" and tablero[1][1] == "X" and tablero[2][0] == "X":
        print("Jugador 1 ha ganado")
        break
    ######  VERIFICADOR DE TURNOS  ######
    count += 1
    if count == 5:
        print("El juego a terminado")
        break

    ######  JUGADOR 2  ######

    while fin2 != True:
        Jugador_2 = int(input("Jugardor 2: Escribe la posicion del 1 al 9: "))
        if Jugador_2 == 1 and tablero[0][0] == "#":
            tablero[0][0] = "O"
            fin2 = True
        elif Jugador_2 == 2 and tablero[0][1] == "#":
            tablero[0][1] = "O"
            fin2 = True
        elif Jugador_2 == 3 and tablero[0][2] == "#":
            tablero[0][2] = "O"
            fin2 = True
        elif Jugador_2 == 4 and tablero[1][0] == "#":
            tablero[1][0] = "O"
            fin2 = True
        elif Jugador_2 == 5 and tablero[1][1] == "#":
            tablero[1][1] = "O"
            fin2 = True
        elif Jugador_2 == 6 and tablero[1][2] == "#":
            tablero[1][2] = "O"
            fin2 = True
        elif Jugador_2 == 7 and tablero[2][0] == "#":
            tablero[2][0] = "O"
            fin2 = True
        elif Jugador_2 == 8 and tablero[2][1] == "#":
            tablero[2][1] = "O"
            fin2 = True
        elif Jugador_2 == 9 and tablero[2][2] == "#":
            tablero[2][2] = "O"
            fin2 = True
        for mesa in tablero:
            print(mesa)

    ######  VERIFICADOR DE TRIQUI JUGADOR 2 ######

    if tablero[0][0] == "O" and tablero[1][0] == "O" and tablero[2][0] == "O":
        print("Jugador 2 ha ganado")
        break
    elif tablero[0][1] == "O" and tablero[1][1] == "O" and tablero[2][1] == "O":
        print("Jugador 2 ha ganado")
        break
    elif tablero[0][2] == "O" and tablero[1][2] == "O" and tablero[2][2] == "O":
        print("Jugador 2 ha ganado")
        break
    elif tablero[0][0] == "O" and tablero[0][1] == "O" and tablero[0][2] == "O":
        print("Jugador 2 ha ganado")
        break
    elif tablero[1][0] == "O" and tablero[1][1] == "O" and tablero[1][2] == "O":
        print("Jugador 2 ha ganado")
        break
    elif tablero[2][0] == "O" and tablero[2][1] == "O" and tablero[2][2] == "O":
        print("Jugador 2 ha ganado")
        break
    elif tablero[0][0] == "O" and tablero[1][1] == "O" and tablero[2][2] == "O":
        print("Jugador 2 ha ganado")
        break
    elif tablero[0][2] == "X" and tablero[1][1] == "X" and tablero[2][0] == "X":
        print("Jugador 2 ha ganado")
        break
