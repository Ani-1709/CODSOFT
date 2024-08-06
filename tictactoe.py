import math

# Constants
PLAYER_X = "X"  # Human player
PLAYER_O = "O"  # AI player
EMPTY = " "

# Initialize the board
def init_board():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

# Print the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Check for a winner
def check_winner(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None

# Check if the board is full
def is_full(board):
    for row in board:
        if EMPTY in row:
            return False
    return True

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == PLAYER_O:
        return 1
    if winner == PLAYER_X:
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Find the best move for the AI
def best_move(board):
    best_val = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_O
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = EMPTY
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    return move

# Main game loop
def play_game():
    board = init_board()
    human_turn = True
    
    while True:
        print_board(board)
        
        if check_winner(board):
            print(f"{check_winner(board)} wins!")
            break
        
        if is_full(board):
            print("It's a tie!")
            break
        
        if human_turn:
            row, col = map(int, input("Enter your move (row and column): ").split())
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_X
                human_turn = False
            else:
                print("Invalid move. Try again.")
        else:
            move = best_move(board)
            if move:
                board[move[0]][move[1]] = PLAYER_O
            human_turn = True

# Start the game
play_game()
