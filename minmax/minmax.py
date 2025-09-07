# tic tac toe với minimax và alpha-beta
# người chơi: X, máy: O

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], board[i+1], board[i+2])
    print()

def is_winner(board, player):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # hàng ngang
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cột dọc
        (0, 4, 8), (2, 4, 6)              # đường chéo
    ]
    return any(all(board[i] == player for i in combo) for combo in wins)

def is_full(board):
    return ' ' not in board

# minimax cơ bản
def minimax(board, depth, is_maximizing):
    if is_winner(board, 'O'):
        return 1
    if is_winner(board, 'X'):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:  # máy (O)
        best_score = -999
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(best_score, score)
        return best_score
    else:  # người (X)
        best_score = 999
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(best_score, score)
        return best_score

# alpha-beta pruning
def alphabeta(board, depth, alpha, beta, is_maximizing):
    if is_winner(board, 'O'):
        return 1
    if is_winner(board, 'X'):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -999
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = alphabeta(board, depth + 1, alpha, beta, False)
                board[i] = ' '
                best_score = max(best_score, score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = 999
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = alphabeta(board, depth + 1, alpha, beta, True)
                board[i] = ' '
                best_score = min(best_score, score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        return best_score

# tìm nước đi tốt nhất với minimax
def best_move_minimax(board):
    best_score = -999
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# tìm nước đi tốt nhất với alpha-beta
def best_move_alphabeta(board):
    best_score = -999
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = alphabeta(board, 0, -999, 999, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# chơi game
def play():
    board = [' '] * 9
    print("bạn đi trước (X), máy đi sau (O)")
    print_board(board)

    while True:
        # người đi
        move = int(input("chọn vị trí (0-8): "))
        if board[move] != ' ':
            print("ô đã đánh rồi!")
            continue
        board[move] = 'X'
        print_board(board)

        if is_winner(board, 'X'):
            print("bạn thắng!")
            break
        if is_full(board):
            print("hòa!")
            break

        # máy đi (dùng alpha-beta)
        move = best_move_alphabeta(board)
        board[move] = 'O'
        print("máy đánh:")
        print_board(board)

        if is_winner(board, 'O'):
            print("máy thắng!")
            break
        if is_full(board):
            print("hòa!")
            break

# chạy thử game
play()
