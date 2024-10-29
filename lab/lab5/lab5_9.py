def check_win(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != 0:
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return True

    return False


board_1 = [[1, 0, -1], [1, 1, -1], [0, 0, 1]]

board_2 = [[1, 0, -1], [1, 1, -1], [0, 0, 0]]

board_3 = [[1, 1, -1], [0, 0, -1], [0, 0, -1]]

print("X = 1 | O = -1")
print(f"Win is X (board_1): {check_win(board_1)}")
print(f"Win is X (board_2): {check_win(board_2)}")
print(f"Win is O (board_3): {check_win(board_3)}")
