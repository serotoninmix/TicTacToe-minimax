"""
Tic Tac Toe Player
"""
import math
import copy
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
    countX = sum(row.count(X) for row in board)
    countO = sum(row.count(O) for row in board)
    if countX > countO:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid action")
    else:
        new_board = copy.deepcopy(board)
        new_board[action[0]][action[1]] = player(board)
        return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    lines = [
        # rows
        [board[i][0] for i in range(3)],
        [board[i][1] for i in range(3)],
        [board[i][2] for i in range(3)],
        # columns
        board[0],
        board[1],
        board[2],
        # diagonals
        [board[i][i] for i in range(3)],
        [board[i][2 - i] for i in range(3)]
    ]

    for line in lines:
        if line.count(X) == 3:
            return X
        if line.count(O) == 3:
            return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True


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


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    def max_value(state):
        if terminal(state):
            return utility(state)
        v = -math.inf
        for action in actions(state):
            v = max(v, min_value(result(state, action)))
        return v

    def min_value(state):
        if terminal(state):
            return utility(state)
        v = math.inf
        for action in actions(state):
            v = min(v, max_value(result(state, action)))
        return v

    current_player = player(board)
    best_score = -math.inf if current_player == X else math.inf
    best_action = None

    available_actions = list(actions(board))
    random.shuffle(available_actions)

    for action in available_actions:
        if current_player == X:
            score = min_value(result(board, action))
            if score > best_score:
                best_score = score
                best_action = action
        else:
            score = max_value(result(board, action))
            if score < best_score:
                best_score = score
                best_action = action

    return best_action