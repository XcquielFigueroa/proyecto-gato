import random

#mostrar tablero
def crear_tablero():
    tablero = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    return tablero

#mostrar tablero
def imprimir_tablero(tablero):
    fila = 0
    while fila < 3:
        print(f"{tablero[fila][0]}|{tablero[fila][1]}|{tablero[fila][2]}")
        if fila < 2:
            print("-" * 5)
        fila += 1
    print()

#entrada del jugador
def movimiento_jugador(tablero, jugador):
        while True:
            try:
                fila = int(input("Elige fila (0, 1, 2): "))
                columna = int(input("Elige columna (0, 1, 2): "))
                if 0 <= fila <= 2 and 0 <= columna <= 2:
                    if tablero[fila][columna] == " ":
                        tablero[fila][columna] = jugador
                        break
                    else:
                        print("¡Casilla ocupada!")
                else:
                    print("ingrese un valores entre 0, 1 o 2")
            except ValueError:
                print("No ingrese valores vacíos o inválidos, sólo números enteros")

#jugada ia
def movimiento_ia(tablero):
    grifear_jugador = jugada_grifeadora(tablero)
    if not grifear_jugador:
        casillas_vacias = [(i, j) for i in range(3) for j in range(3) if tablero[i][j] == " "]
        if casillas_vacias:
            fila, columna = random.choice(casillas_vacias)
            tablero[fila][columna] = "O"

#hacer jugada grifeadora
def jugada_grifeadora(tablero):
    # revisar coincidencia en fila 0
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == "X" and tablero[i][2] == " ":
            tablero[i][2] = "O"
            return True
        if tablero[i][1] == tablero[i][2] == "X" and tablero[i][0] == " ":
            tablero[i][0] = "O"
            return True
        if tablero[i][0] == tablero[i][2] == "X" and tablero[i][1] == " ":
            tablero[i][1] = "O"
            return True
    # revisar coincidencia en columnas 0
    for j in range(3):
        if tablero[0][j] == tablero[1][j] == "X" and tablero[2][j] == " ":
            tablero[2][j] = "O"
            return True
        if tablero[1][j] == tablero[2][j] == "X" and tablero[0][j] == " ":
            tablero[0][j] = "O"
            return True
        if tablero[0][j] == tablero[2][j] == "X" and tablero[1][j] == " ":
            tablero[1][j] = "O"
            return True
    # revisar coincidencia en diagonal \
        if tablero[0][0] == tablero[1][1] == "X" and tablero[2][2] == " ":
            tablero[2][2] = "O"
            return True
        if tablero[1][1] == tablero[2][2] == "X" and tablero[0][0] == " ":
            tablero[0][0] = "O"
            return True
        if tablero[0][0] == tablero[2][2] == "X" and tablero[1][1] == " ":
            tablero[1][1] = "O"
            return True
    # revisar coincidencia en diagonal /
        if tablero[0][2] == tablero[1][1] == "X" and tablero[2][0] == " ":
            tablero[2][0] = "O"
            return True
        if tablero[1][1] == tablero[2][0] == "X" and tablero[0][2] == " ":
            tablero[0][2] = "O"
            return True
        if tablero[0][2] == tablero[2][0] == "X" and tablero[1][1] == " ":
            tablero[1][1] = "O"
            return True
    return False

#revisar ganador
def hay_ganador(tablero):
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return True
    return False


#verificar tablero lleno
def tablero_lleno(tablero):
    for fila in tablero:
        if " " in fila:
            return False
    return True

#finalizador de partida segun puntaje
def finalizar_partida(ganador_partida, x, o):
    diferencia = abs(x - o)
    if x == 10 or o == 10:
        print(f"Resultados:\nJugador X = {x}\nJugador 0 = {o}")
        print(f"\033[32mTEl jugador {ganador_partida} ha ganado la partida con {diferencia} puntos de ventaja\033[0m")
        return False
    else:
        return True

#funcion principal
def juego():
    tablero = crear_tablero()
    jugador_actual = "X"
    puntos_x = 0
    puntos_o = 0
    while finalizar_partida(jugador_actual, puntos_x, puntos_o):
        while True:
            print(f"jugador X = {puntos_x} puntos\njugador O = {puntos_o} puntos\n")
            imprimir_tablero(tablero)
            print(f"\033[33mTurno de {jugador_actual}\033[0m\n")

            if jugador_actual == "X":
                movimiento_jugador(tablero, jugador_actual)

            else:
                movimiento_ia(tablero)
            if hay_ganador(tablero):
                imprimir_tablero(tablero)
                print(f"¡{jugador_actual} ha ganado!")
                if jugador_actual == "X":
                    puntos_x += 1
                else:
                    puntos_o += 1
                tablero = crear_tablero()
                break

            if tablero_lleno(tablero):
                imprimir_tablero(tablero)
                print("¡Empate!\n")
                tablero = crear_tablero()

            if jugador_actual == "O":
                jugador_actual = "X"

            else:
                jugador_actual = "O"

#evitar error al cerrar
try:
    juego()
except KeyboardInterrupt:
    print("\nJuego cerrado por el usuario")