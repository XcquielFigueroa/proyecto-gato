# esta versión es la base para trabajar en la evaluación III
def crear_tablero():
    tablero = []
    fila = 0
    while fila < 3:
        tablero.append([" ", " ", " "])
        fila += 1
    return tablero


def crear_tablero():
    tablero = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    return tablero


def imprimir_tablero(tablero):
    fila = 0
    while fila < 3:
        print(f"{tablero[fila][0]}|{tablero[fila][1]}|{tablero[fila][2]}")
        if fila < 2:
            print("-" * 5)
        fila += 1


def imprimir_tablero(tablero):
    print(f"{tablero[0][0]}|{tablero[0][1]}|{tablero[0][2]}")
    print("-----")
    print(f"{tablero[1][0]}|{tablero[1][1]}|{tablero[1][2]}")
    print("-----")
    print(f"{tablero[2][0]}|{tablero[2][1]}|{tablero[2][2]}")


def movimiento_jugador(tablero, jugador):
    while True:
        fila = int(input("Elige fila (0, 1, 2): "))
        columna = int(input("Elige columna (0, 1, 2): "))
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador
            break
        else:
            print("¡Casilla ocupada!")


def hay_ganador(tablero):
    # Verificar filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            return True

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return True

    return False


def tablero_lleno(tablero):
    for fila in tablero:
        if " " in fila:
            return False
    return True


# Agregar en juego_completo():
if tablero_lleno(tablero):
    print("¡Empate!")
    break

import random


def movimiento_ia(tablero):
    casillas_vacias = [(i, j) for i in range(3) for j in range(3) if tablero[i][j] == " "]
    if casillas_vacias:
        fila, columna = random.choice(casillas_vacias)
        tablero[fila][columna] = "O"


# Modificar el turno en juego_completo():
if jugador_actual == "X":
    movimiento_jugador(tablero)
else:
    movimiento_ia(tablero)


def juego_completo():
    tablero = crear_tablero()
    jugador_actual = "X"

    while True:
        imprimir_tablero(tablero)
        print(f"Turno de {jugador_actual}")
        movimiento_jugador(tablero, jugador_actual)

        if hay_ganador(tablero):
            print(f"¡{jugador_actual} ha ganado!")
            break

        if (jugador_actual == "O"):
            jugador_actual = "X"
        else:
            jugador_actual = "O"


juego_completo()

# tablero = crear_tablero()
# imprimir_tablero(tablero)
# movimiento_jugador(tablero)
# imprimir_tablero(tablero)