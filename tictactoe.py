"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

# Dylan M
def player(board):
    """
    Returns player who has the next turn on a board.
    """
    raise NotImplementedError

# Dylan M
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError

# Kevin
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError

# Kevin 
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError

# Dylan T
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError

# Dylan T
def score(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError

# Michael M
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
