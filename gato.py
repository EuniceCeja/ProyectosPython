# Function definition to print board "Función para imprimir el tablero"
def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila)) # Print a row of the board (imprimir una fila del tablero)
        print("-" * 9) # Print divider line (imprimir linea divisoria)

# Function to check the winner
def verificador_ganador(tablero, jugador):
    #Check rows and columns
    for i in range(3):
        if all(tablero[i][j] == jugador for j in range(3)) or all(tablero[j][i] == jugador for j in range(3)):
            return True
    # Check diagonals
    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2-i] == jugador for i in range(3)):
        return True
        
    return False

# Main function (Función principal)
def jugar():
    tablero = [[" " for _ in range(3)] for _ in range(3)] # initialize empty board "inicializa un tablero vacio"
    # En este fragmento, range(3) se utiliza para generar los valores 0, 1 y 2,  que se utiliza como índices para acceder
    # a las filas y columnas del tablero. 

    jugador_actual = "X"
    jugadas = 0 # Contador de jugadas

    while jugadas < 9: # Maximun nnumber of plays in the game "Máximo numero de jugadas en el juego"
        imprimir_tablero(tablero) # No la hemos implementado
        print(f"Turno del jugador {jugador_actual}")

        fila = int(input("Ingrese el número de la fila (0, 1, 2): "))
        columna = int(input("Ingrese el número de columna (0, 1, 2): "))

        if 0 <= fila < 3 and 0 <= columna < 3 and tablero[fila][columna] == " ":
            # if the coordinate is valid and the cell is empty "Si la coordenada es válida y la celda está vacía"
            tablero[fila][columna] = jugador_actual #Update the board "actualizar el tablero"
            jugadas += 1 #Incrase the number of plays "Incrementar el contador de jugadas"

            if verificador_ganador(tablero, jugador_actual): # Check if the current player has won. "Checar si el jugador ha ganado"
                imprimir_tablero(tablero)
                print(f"¡El jugador {jugador_actual} gana!")
                break

            if jugador_actual == "X":
                jugador_actual = "O"
            else:
                jugador_actual = "X"
            # Jugador_actual = "0" if jugador_actual == "X" else "X" # Change the player "Cambiar el jugador"
        else:
            print("Movimiento inválido. Inténtalo de nuevo.")

    if jugadas == 9: # If all moves are completed and there is no winner. "Si se completan las 9 jugadas y no hay ganador"
        imprimir_tablero(tablero)
        print("¡Es un empate!")

if __name__ == "__main__":
    while True:
        print("Bienvenido al juego del Tic Tac Toe")
        jugar_nuevo = input("¿Quieres jugar una partida? (s/n): ")
        if jugar_nuevo.lower() != "s":
            break
        jugar()

