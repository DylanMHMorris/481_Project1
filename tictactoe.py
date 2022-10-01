"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy


class InvalidMove(Exception):
    "Custom exception to be raised in the results() when an invalid move is passed."
    pass


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


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


def minvalue(board):
    if terminal(board):
        return score(board)
    v = math.inf
    for action in actions(board):
        v = min(v, maxvalue(result(board, action)))
    return v


def maxvalue(board):
    if terminal(board):
        return score(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, minvalue(result(board, action)))
    return v


# Michael M
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    optimal_action = None
    if player(board) == X:
        best_val = -math.inf
        for action in actions(board):
            value = minvalue(result(board, action))
            if value > best_val:
                best_val = value
                optimal_action = action
    elif player(board) == O:
        best_val = math.inf
        for action in actions(board):
            value = maxvalue(result(board, action))
            if value < best_val:
                best_val = value
                optimal_action = action
    return optimal_action
