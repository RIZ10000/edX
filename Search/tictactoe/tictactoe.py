"""
Tic Tac Toe Player
"""

import math
import copy
import numpy as np
import random

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


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # raise NotImplementedError

    nX, nO = 0, 0
    for i in board:
        for j in i:
            if j == X:
                nX += 1
            elif j == O:
                nO += 1

    return X if nX <= nO else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # raise NotImplementedError

    action = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                action.add((i, j))
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # raise NotImplementedError
    if action not in actions(board):
        raise ValueError
    board_copy = copy.deepcopy(board)
    board_copy[action[0]][action[1]] = player(board)
    return board_copy


def check(list):
    return all(i == list[0] for i in list)


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # raise NotImplementedError
    board = np.array(board)
    for i in range(3):
        if check(board[i, :]):
            return (board[i][0])
    for i in range(3):
        if check(board[:, i]):
            return (board[0][i])
    if check(np.diag(board)):
        return (board[0][0])
    elif check(np.fliplr(board).diagonal()):
        return (board[0][2])
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # raise NotImplementedError
    if winner(board) is not None or not actions(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # raise NotImplementedError
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # raise NotImplementedError

    if terminal(board):
        return None

    if board == initial_state():
        return (random.choice((0, 2)), random.choice((0, 2)))  # any corner is best

    p = player(board)

    if p == X:
        v = -math.inf
        for action in actions(board):
            minv = min_value(result(board, action))
            if minv > v:
                v = minv
                opti_action = action
    elif p == O:
        v = math.inf
        for action in actions(board):
            maxv = max_value(result(board, action))
            if maxv < v:
                v = maxv
                opti_action = action

    return opti_action


def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v
