board = [[x + y * 3 for x in range(1, 4)] for y in range(3)]
print(board)


def display_board(board):
    print("+", "+", "+", "+", sep="-" * 7)
    for i in range(3):
        print("|", "|", "|", "|", sep=" " * 7)
        for j in range(3):
            print("|", end="")
            print(str(board[i][j]).center(7, " "), end="")
        print("|")
        print("|", "|", "|", "|", sep=" " * 7)
        print("+", "+", "+", "+", sep="-" * 7)


def enter_move(board):
    while True:
        try:
            move = int(input("Enter your move: "))
            if not (1 <= move <= 9):
                raise ValueError
            break
        except ValueError:
            print("invalid move")
            continue

    found = False
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == move:
                board[i][j] = "O"
                found = True
    if not found:
        print("illegal move")


display_board(board)
enter_move(board)
display_board(board)
