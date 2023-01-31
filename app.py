import random

def draw_board(board):
    print("\n" * 100) # Clears the screen
    print("| {} | {} | {} | {} | {} |".format(*board[0:5]))
    print("| {} | {} | {} | {} | {} |".format(*board[5:10]))
    print("| {} | {} | {} | {} | {} |".format(*board[10:15]))
    print("| {} | {} | {} | {} | {} |".format(*board[15:20]))
    print("| {} | {} | {} | {} | {} |".format(*board[20:25]))

def update_board(board, move, symbol):
    board[move - 1] = symbol

def check_winner(board, symbol):
    # Check rows
    for i in range(0, 25, 5):
        if all(x == symbol for x in board[i:i+5]):
            return True
    
    # Check columns
    for i in range(0, 5):
        if all(x == symbol for x in board[i::5]):
            return True

    # Check diagonals
    if all(x == symbol for x in board[0::6]):
        return True
    if all(x == symbol for x in board[4::4]):
        return True

    return False

def get_ai_move(board, ai_symbol):
    for i, x in enumerate(board):
        if x == " ":
            board[i] = ai_symbol
            if check_winner(board, ai_symbol):
                return i + 1
            board[i] = " "
    for i, x in enumerate(board):
        if x == " ":
            board[i] = "X"
            if check_winner(board, "X"):
                return i + 1
            board[i] = " "
    return random.choice([i + 1 for i, x in enumerate(board) if x == " "])

board = [" " for x in range(25)]
symbol = "X"
ai_symbol = "O"

draw_board(board)
while " " in board:
    if symbol == "X":
        move = int(input("Your turn player 1\nEnter your move (1-25): "))
        while board[move - 1] != " ":
            move = int(input("Invalid move. Try again (1-25): "))
        update_board(board, move, symbol)
        if check_winner(board, symbol):
            print("Player 1 wins!")
            break
        symbol = ai_symbol
    else:
        move = get_ai_move(board, ai_symbol)
        update_board(board, move, symbol)
        if check_winner(board, symbol):
            print("AI wins!")
            break
        symbol = "X"
    draw_board(board)

if " " not in board:
    print("It's a draw!")
