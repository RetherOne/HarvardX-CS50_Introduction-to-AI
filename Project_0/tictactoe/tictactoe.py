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
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    X_count = sum(row.count(X) for row in board)
    O_count = sum(row.count(O) for row in board)

    if X_count > O_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    result = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                result.add((i, j))

    return result


def result(board, action):
    i, j = action

    if i < 0 or i > 2 or j < 0 or j > 2:
        raise Exception("Invalid move: out of bounds")

    if board[i][j] != EMPTY:
        raise Exception("Invalid move: cell already taken")

    board[i][j] = player(board)

    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]

    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != EMPTY:
            return board[0][j]

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) != None or len(actions(board)) == 0


def utility(board, maximize=True):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    win = winner(board)
    act_len = len(actions(board))

    if win == X:
        return 1
    if win == O:
        return -1
    if act_len == 0:
        return 0

    if maximize:
        best_score = float("-inf")
        for act in actions(board):
            board[act[0]][act[1]] = X
            score = utility(board, False)
            board[act[0]][act[1]] = EMPTY
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for act in actions(board):
            board[act[0]][act[1]] = O
            score = utility(board, True)
            board[act[0]][act[1]] = EMPTY
            best_score = min(score, best_score)
        return best_score


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current = player(board)

    if current == X:
        best_score = float("-inf")
        best_move = None
        for act in actions(board):
            board[act[0]][act[1]] = X
            score = utility(board, False)
            board[act[0]][act[1]] = EMPTY
            if score > best_score:
                best_score = score
                best_move = act
        return best_move

    else:
        best_score = float("inf")
        best_move = None
        for act in actions(board):
            board[act[0]][act[1]] = O
            score = utility(board, True)
            board[act[0]][act[1]] = EMPTY
            if score < best_score:
                best_score = score
                best_move = act
        return best_move
