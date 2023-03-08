"""
Jugador de tricy
"""

import math
import copy

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
    #Retorna quien es el jugador que debe jugar.
   
    #Siempre empieza la X
    if board==initial_state():
       return X
    else:
      contX = 0
      contO = 0
      for i in range(3):
          for j in range(3):
              if board[i][j] == X:
                contX+=1
              if board[i][j] == O:
                contO+=1
      #esto permite que empiece O
      if contO>=contX:
        return X
      else:
        return O



def actions(board):
    Acciones=[]
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                Acciones.append((i,j))
    return Acciones


def result(board, action):
    NewBoard = copy.deepcopy(board)
    if player(board) == X:
      NewBoard[action[0]][action[1]] = X
    elif player(board)==O:
      NewBoard[action[0]][action[1]] = O
    return NewBoard



def winner(board):
    """
    Retorna el ganador del juego
    """
    if terminal(board) and utility(board)==1:
      return X
    if terminal(board) and utility(board)==-1:
      return O
    else:
      return None


def terminal(board):
    s=0
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                s=1
    if s==0 :
        return True
    if (utility(board) ==1) or (utility(board)==-1):
       return True
    else:
       return False
    """
    Retorna True si el juego se acabó y False si continua.
    """
def utility(board):
    #t=0
    #Para X
    #Comprobar lineas horizontales
    for i in range(0,3):
      if (board[i][0] == X) and (board[i][1] == X) and (board[i][2] == X):
        return 1
    #Comprobar lineas verticales
    for j in range(0,3):
      if (board[0][j] == X) and (board[1][j] == X) and (board[2][j] == X):
        return 1
    #Comprobar diagonales
    if (board[0][0] == X and board[1][1] == X and board[2][2] == X) or (board[2][0] == X and board[1][1] == X and board[0][2] == X):
        return 1

    #Para O
    #Comprobar lineas horizontales
    for i in range(0,3):
      if board[i][0] == O and board[i][1] == O and board[i][2] == O:
        return -1
    #Comprobar lineas verticales
    for j in range(0,3):
      if board[0][j] == O and board[1][j] == O and board[2][j] == O:
        return -1
    #Comprobar diagonales
    if (board[0][0] == O and board[1][1] == O and board[2][2] == O) or (board[2][0] == O and board[1][1] == O and board[0][2] == O):
        return -1

   
   # Como el return automaticaente termina la lectura del código si se llega a esta linea es porque nadie ganó en el estado terminal
    #if t ==0:
       #return 0
    return 0

    #Retorna 1 si X ganó el juego, -1 si O ganó, y 0 si empatan.
    


def min_value(board):
   if terminal(board):
      return utility(board)
   else:
    v = math.inf
    for action in actions(board):
        v = min(v,max_value(result(board,action)))
    return v

def max_value(board):
   if terminal(board):
      return utility(board)
   else:
    v = -math.inf
    for action in actions(board):
        v = max(v,min_value(result(board,action)))
    return v

def minimax(board):
   if terminal(board):
      return None
   elif player(board)==X:
      if board ==initial_state():
         return (1,2)
      v = -math.inf
      mejorJugada = ()
      for action in actions(board):
         puntaje = max_value(result(board,action))
         print(puntaje)
         if puntaje > v:
            v = puntaje
            mejorJugada = action
      return mejorJugada
   elif player(board)==O:
      v = math.inf
      mejorJugada = ()
      print('otro')
      for action in actions(board):
         puntaje = min_value(result(board,action))
         print(action)
         if v > puntaje:
            v = puntaje
            mejorJugada = action
      return mejorJugada