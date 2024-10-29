def convert_to_xo(row):
    drow = []
    for i in range(len(row)):
        if row[i] == -1:
            drow.append("O")
        elif row[i] == 1:
            drow.append("X")
        else:
            drow.append(str(row[i]))
    return drow


def display_row_data(row, isConvert):
    if isConvert:
        row = convert_to_xo(row)
    print(f"  {row[0]} | {row[1]} | {row[2]}  ")


def display_row_border():
    print(" ---+---+--- ")


def display_board(board, isConvert):
    display_row_data(board[0], isConvert)
    display_row_border()
    display_row_data(board[1], isConvert)
    display_row_border()
    display_row_data(board[2], isConvert)


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


def main():
    board_ox = [[1, 1, 0], [-1, -1, 0], [-1, 1, -1]]

    print("Display numeric board_ox:")
    display_board(board_ox, False)
    print()

    print("Display OX board:")
    display_board(board_ox, True)
    print()

    board_1 = [[1, 0, -1], [1, 1, -1], [0, 0, 1]]
    board_2 = [[1, 0, -1], [1, 1, -1], [0, 0, 0]]
    board_3 = [[1, 1, -1], [0, 0, -1], [0, 0, -1]]

    print("X = 1 | O = -1")
    print(f"Win is X (board_1): {check_win(board_1)}")  # Expected output: True
    print(f"Win is X (board_2): {check_win(board_2)}")  # Expected output: False
    print(f"Win is O (board_3): {check_win(board_3)}")  # Expected output: True


if __name__ == "__main__":
    print("\n_______________ 5.10 _________________\n")
    main()
    print("\n____________________________________\n")
