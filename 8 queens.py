N = 8

def print_board(board):
    for r in board:
        print(" ".join("Q" if c else "." for c in r))
    print()

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i]: return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]: return False
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j]: return False
    return True

def solve(board, col=0):
    if col == N:
        print_board(board)
        return True
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve(board, col + 1): return True
            board[i][col] = 0
    return False

board = [[0]*N for _ in range(N)]
solve(board)