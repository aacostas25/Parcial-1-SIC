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
    """
    Retorna quien es el jugador que debe jugar.
    """
    raise NotImplementedError


def actions(board):
    """
    Retorna el conjunto de todas las acciones posibles (i,j) disponibles en el tablero.
    """
    raise NotImplementedError


def result(board, action):
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
    """
    Retorna True si el juego se acabó y False si continua.
    """
    raise NotImplementedError


def utility(board):
    """
    Retorna 1 si X ganó el juego, -1 si O ganó, y 0 si empatan.
    """
    raise NotImplementedError


def minimax(board):
    """
    Reotrna la acción que optimiza la elección del jugador.
    """
    raise NotImplementedError
