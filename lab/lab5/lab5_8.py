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


board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
board_ox = [[1, 1, 0], [-1, -1, 0], [-1, 1, -1]]

print("Display numeric board:")
display_board(board, False)
print()

print("Display numeric board_ox:")
display_board(board_ox, False)
print()

print("Display OX board:")
display_board(board_ox, True)
