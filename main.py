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
        fila = int(input("Elige fila (0, 1, 2): "))
        columna = int(input("Elige columna (0, 1, 2): "))
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador
            break
        else:
            print("¡Casilla ocupada!")

#jugada ia
def movimiento_ia(tablero):
    casillas_vacias = [(i, j) for i in range(3) for j in range(3) if tablero[i][j] == " "]
    if casillas_vacias:
        fila, columna = random.choice(casillas_vacias)
        tablero[fila][columna] = "O"

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
                print("¡Empate!")
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