import math
import random
import timeit


def print_board(board):
    print("\n".join([ " | ".join(row) for row in board ]))

def get_winner(board):
    # Check rows
    for row in board:
        if len(set(row)) == 1 and row[0] != "-":
            return row[0]

    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "-":
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        return board[0][2]

    # Check for draw
    if all([ cell != "-" for row in board for cell in row ]):
        return "draw"

    return None

def get_best_move(board, depth, maximizing_player):
    if depth == 0 or get_winner(board):
        return None, evaluate(board)

    if maximizing_player:
        best_score = -math.inf
        best_move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == "-":
                    board[i][j] = "X"
                    _, score = get_best_move(board, depth - 1, False)
                    board[i][j] = "-"
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_move, best_score
    else:
        best_score = math.inf
        best_move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == "-":
                    board[i][j] = "O"
                    _, score = get_best_move(board, depth - 1, True)
                    board[i][j] = "-"
                    if score < best_score:
                        best_score = score
                        best_move = (i, j)
        return best_move, best_score

def evaluate(board):
    winner = get_winner(board)
    if winner == "X":
        return 1
    elif winner == "O":
        return -1
    else:
        return 0

def play_game():
    depth = int(input("Ingrese la profundidad de búsqueda del algoritmo Minimax: "))
    board = [ [ "-" for j in range(3) ] for i in range(3) ]
    turn = "X"

    while not get_winner(board):
        print_board(board)

        if turn == "X":
            print("Es el turno del jugador X.")
            i, j = map(int, input("Ingrese las coordenadas de su jugada (ejemplo: 1 2): ").split())
            while board[i][j] != "-":
                print("Esa celda ya está ocupada. Por favor, elija otra.")
                i, j = map(int, input("Ingrese las coordenadas de su jugada (ejemplo: 1 2): ").split())
            board[i][j] = "X"
            turn = "O"
        else:
            print("Es el turno de la computadora O.")
            start = timeit.default_timer()
            move, score = get_best_move(board, depth, False)
            final = timeit.default_timer()
            board[move[0]][move[1]] = "O"
            print("Terminado en --- %s segundos ---" % (final - start))
            turn = "X"

    print_board(board)
    winner = get_winner(board)
    if winner == "X":
        print("¡Felicitaciones! ¡Has ganado!")
    elif winner == "O":
        print("La computadora ha ganado. ¡Mejor suerte la próxima vez!")
    else:
        print("¡Es un empate!")
play_game()


