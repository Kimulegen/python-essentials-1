from random import randrange

board = [[x + y * 3 for x in range(1, 4)] for y in range(3)]


def display_board(board):
    print("+", "+", "+", "+", sep="-" * 7)
    for i, row in enumerate(board):
        print("|", "|", "|", "|", sep=" " * 7)
        for j, _ in enumerate(row):
            print("|", end="")
            print(str(board[i][j]).center(7, " "), end="")
        print("|")
        print("|", "|", "|", "|", sep=" " * 7)
        print("+", "+", "+", "+", sep="-" * 7)


def enter_move(board):
    found = False
    while not found:
        try:
            move = int(input("Enter your move: "))
            if not (1 <= move <= 9):
                raise ValueError
        except ValueError:
            print("invalid move")
            continue

        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == move:
                    board[i][j] = "O"
                    found = True

        if not found:
            print("illegal move")


def make_list_of_free_fields(board):
    free_fields = []
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if type(cell) != str:
                free_fields.append((i, j))

    return free_fields


def victory_for(board, sign):
    # horizontal
    for i, row in enumerate(board):
        if all(cell == sign for cell in row):
            return True

    # vertical
    for i, row in enumerate(board):
        vert = []
        for j, _ in enumerate(row):
            vert.append(board[j][i])
        if all(cell == sign for cell in vert):
            return True

    # diagonal
    diag = [board[i][i] for i in range(len(board))]
    if all(cell == sign for cell in diag):
        return True
    diag2 = [board[i][len(board[0]) - 1 - i] for i in range(len(board))]
    if all(cell == sign for cell in diag2):
        return True

    return False


def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    coord_y, coord_x = free_fields[randrange(len(free_fields))]
    board[coord_y][coord_x] = "X"


board[1][1] = "X"
sign = "X"

while not victory_for(board, sign) and len(make_list_of_free_fields(board)):
    if sign == "X":
        display_board(board)
        enter_move(board)
        sign = "O"
    else:
        draw_move(board)
        sign = "X"
display_board(board)

if len(make_list_of_free_fields(board)) == 0:
    print("tie")
elif sign == "X":
    print("you lost")
else:
    print("you won!")
