"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None

# Helper functions


def get_diags(board):
    return [[board[0][0], board[1][1], board[2][2]],
            [board[0][2], board[1][1], board[2][0]]]


def get_columns(board):
    columns = []

    for i in range(3):
        columns.append([row[i] for row in board])

    return columns


def three_in_a_row(row):
    return True if row.count(row[0]) == 3 else False


def all_cells_filled(board):
    for row in board:
        if EMPTY in row:
            return False

    return True

# Pre-defined Functions


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
    cntX=0
    cntO=0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                cntX += 1
            if board[i][j] == O:
                cntO += 1

    if cntO == cntX:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions=set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i,j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = deepcopy(board)
    cur_player = player(board)
    i,j=action

    if new_board[i][j] is not EMPTY:
        raise Exception("Invalid Move")
    else:
        new_board[i][j]=cur_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    rows = board + get_diags(board) + get_columns(board)

    for row in rows:
        current_player = row[0]

        if current_player is not None and three_in_a_row(row):
            return current_player

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    else:
        return all_cells_filled(board)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def max_value(board,alpha,beta):
    if terminal(board):
        return utility(board)

    temp = -math.inf
    for action in actions(board):
        temp = max(temp,min_value(result(board,action),alpha,beta))
        alpha = max(alpha, temp)

        if alpha >= beta:
            break

    return temp


def min_value(board,alpha,beta):
    if terminal(board):
        return utility(board)

    temp = math.inf
    for action in actions(board):
        temp = min(temp, max_value(result(board,action),alpha,beta))
        beta = min(beta, temp)

        if alpha >= beta:
            break

    return temp


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    cur_player = player(board)
    optimum_move = None

    alpha = -math.inf
    beta = math.inf

    if cur_player == X:
        v = -math.inf
        for action in actions(board):
            new_v = min_value(result(board,action),alpha,beta)
            alpha = max(v, new_v)

            if new_v >= v:
                v=new_v
                optimum_move = action
    else:
        v = math.inf
        for action in actions(board):
            new_v = max_value(result(board,action),alpha,beta)
            beta = min(new_v, v)

            if new_v <= v:
                v=new_v
                optimum_move = action

    return optimum_move



