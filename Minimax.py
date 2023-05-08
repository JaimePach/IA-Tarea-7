import math
import timeit


def print_board(board):
    """
    Imprime el tablero en la consola.
    board: matriz 3x3 que representa el estado actual del tablero
    """
    print("-------------")
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("-------------")

def check_winner(board, player):
    """
    Verifica si el jugador ha ganado.
    board: matriz 3x3 que representa el estado actual del tablero
    player: jugador actual ('X' o 'O')
    return: True si el jugador ha ganado, False de lo contrario
    """
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def check_tie(board):
    """
    Verifica si hay empate.
    board: matriz 3x3 que representa el estado actual del tablero
    return: True si hay empate, False de lo contrario
    """
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                return False
    return True

def minimax(board, depth, player):
    """
    Implementación del algoritmo Minimax.
    board: matriz 3x3 que representa el estado actual del tablero
    depth: profundidad actual de la búsqueda
    player: jugador actual ('X' o 'O')
    return: la mejor puntuación para el jugador
    """
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if check_tie(board):
        return 0
    if player == 'O':
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    score = minimax(board, depth+1, 'X')
                    board[i][j] = '-'
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'X'
                    score = minimax(board, depth+1, 'O')
                    board[i][j] = '-'
                    best_score = min(score, best_score)
        return best_score

def get_move(board, player):
    """
    Obtiene la jugada del jugador.
    board: matriz 3x3 que representa el estado actual del tablero
    player: jugador actual ('X' o 'O')
    return: la posición elegida por el jugador
    """
    if player == 'X':
        move = input("Introduce la posición de tu jugada (1-9): ")
        while not move.isdigit() or int(move) < 1 or int(move) > 9 or board[(int(move)-1)//3][(int(move)-1)%3] != '-':
            move = input("Introduce una posición válida (1-9): ")
        return (int(move)-1)//3, (int(move)-1)%3
    else:
        best_score = -math.inf
        best_move = (-1, -1)
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    score = minimax(board, 0, 'X')
                    board[i][j] = '-'
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_move


def play_game():
    """
    Función principal del juego.
    """
    board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    print_board(board)
    player = 'X'
    while True:
        if player == 'X':
            row, col = get_move(board, player)
            board[row][col] = 'X'
        else:
            print("Turno de la computadora (O):")
            start = timeit.default_timer()
            row, col = get_move(board, player)
            final = timeit.default_timer()
            board[row][col] = 'O'
            print("Terminado en --- %s segundos ---" % (final - start))
        print_board(board)
        if check_winner(board, player):
            print(player, "ha ganado!")
            break
        if check_tie(board):
            print("Empate!")
            break
        player = 'O' if player == 'X' else 'X'
        
play_game()

