"""
Jugador de tricy
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Retorna el estado inicial del tablero
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    if board== initial_state():
        return X
    elif 
    """
    Retorna quien es el jugador que debe jugar.
    """
    raise NotImplementedError


def actions(board):
    lista=[]
    for i in range(1,4):
        for j in range(1,4):
            if board[i][j] == EMPTY:
                lista.append([i,j])
    return lista
    """
    Retorna el conjunto de todas las acciones posibles (i,j) disponibles en el tablero.
    """
    raise NotImplementedError


def result(board, action):
    if player == X:
        board[action[0]][action[1]] = X
    else:
        board[action[0]][action[1]] = O
    """
    Retorna el tablero que resulta de hacer la acción (i,j) en el tablero.
    """
    raise NotImplementedError


def winner(board):
    """
    Retorna el ganador del juego
    """
    raise NotImplementedError


def terminal(board):
    s=0
    for i in range(1,4):
        for j in range(1,4):
            if board[i][j] == EMPTY:
                s=1
    if s==0 :
        return True
    else:
        for i in range(1,4):
            for j in range(1,4):
                if board[i][j] == X and board[i][j+1]==X and board[i][j]==X:
                    return True
                    



    """
    Retorna True si el juego se acabó y False si continua.
    """
    raise NotImplementedError


def utility(board):

    for i in range(1,4):
        for j in range(1,4):
            if board[i][j] == X and board[i][j+1]==X and board[i][j]==X:
                return True
                    

    """
    Retorna 1 si X ganó el juego, -1 si O ganó, y 0 si empatan.
    """
    raise NotImplementedError


def minimax(board):
    """
    Reotrna la acción que optimiza la elección del jugador.
    """
    raise NotImplementedError
