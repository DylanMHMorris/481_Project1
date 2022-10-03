"""
Tic Tac Toe Player
"""

import copy
import math
from copy import deepcopy


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
    if board == initial_state():
        # if the game has not started yet X always has first move and will exit function early
        return X
    # sets initial number for turns taken for each player
    Xturns = 0
    Oturns = 0

    # counts how many x's and o's are placed on board
    for row in board:
        Xturns += row.count(X)
        Oturns += row.count(O)

    # returns player who has taken less turns
    if Xturns <= Oturns:
        return X
    else:
        return O
    # raise NotImplementedError


# Dylan M
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # creates storage for possible actions player can take
    possible_actions = set()
    # shifts through board to see what spots are available
    for x in range(len(board)):
        for y in range(3):
            # if spot on board is empty add it to possible actions
            if board[x][y] == EMPTY:
                possible_actions.add((x, y))
    # return set of possible actions
    return possible_actions
    # raise NotImplementedError


# Kevin
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # raise exception errors for out of bounds or position taken
    if action not in actions(board):
        raise Exception("Placement is out of bound or has been taken")

    # create new copy of board
    # take in action from new board
    # set new board to intial player board
    newBoard = copy.deepcopy(board)
    newBoard[action[0]][action[1]] = player(board)

    return newBoard


# Kevin
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # increment row to determine winner at any row
    for row in range(3):
        # check for winner horizontally
        if board[row][0] == board[row][1] == board[row][2]:
            # check position at row nth and column 0-2
            # return symbol from winning position
            if board[row][0] == X:
                return X
            elif board[row][0] == O:
                return O

    for col in range(3):
        # check for winner vertically
        if board[0][col] == board[1][col] == board[2][col]:
            # check position at col nth and row 0-2
            # return symbol from winning position
            if board[0][col] == X:
                return X
            elif board[0][col] == O:
                return O

    # check for winner diagonally from top left to bottom right
    if board[0][0] == board[1][1] == board[2][2]:
        # return symbol from winning position
        if board[0][0] == X:
            return X
        elif board[0][0] == O:
            return O
    # check for winner diagonally from bottom left to top right
    if board[0][2] == board[1][1] == board[2][0]:
        # return symbol from winning position
        if board[0][2] == X:
            return X
        elif board[0][2] == O:
            return O


# Dylan T
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check to see if there is a winner
    if winner(board):
        return True
    # If there is not a winner, check to see if all possible moves have been made
    elif not actions(board):
        return True
    # At this point there are no winners and no possible moves to be made
    else:
        return False


#    raise NotImplementedError


# Dylan T
def score(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Check if the game has ended
    if terminal(board):
        # If the winner of the game is X return a 1
        if winner(board) == X:
            return 1
        # If the winner of the game is O return a -1
        elif winner(board) == O:
            return -1
        # If neither X or O won, return a 0 to indicate a tie
        else:
            return 0

    # raise NotImplementedError


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
