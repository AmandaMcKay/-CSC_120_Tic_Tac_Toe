board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]

firstturn = True
gameover = False


def print_board():
    print("Printing Board...")
    print(board[0])
    print(board[1])
    print(board[2])
    if not gameover:
        switch_player()
        player_input()


def print_board_error():
    print("Printing Board...")
    print(board[0])
    print(board[1])
    print(board[2])
    player_input()


def input_to_board(row, column):
    if playerid == 1:
        if row == 0 or row == 1 or row == 2:
            if column == 0 or column == 1 or column == 2:
                if board[row][column] == "-":
                    board[row][column] = "X"
                    print("Player 1 added mark at the location", row, ',', column)
                    print_board()
                else:
                    print("****Board", row, ',', column, "has already been selected. Please try another spot!****")
                    print("**** Invalid choice. Please mark again! ****")
                    print_board_error()
            else:
                print("**** Invalid row or column. Please select row / col between values 0 to 2.")
                print("**** Invalid choice. Please mark again! ****")
                print_board_error()
        else:
            print("**** Invalid row or column. Please select row / col between values 0 to 2.")
            print("**** Invalid choice. Please mark again! ****")
            print_board_error()

    if playerid == 2:
        if row == 0 or row == 1 or row == 2:
            if column == 0 or column == 1 or column == 2:
                if board[row][column] == "-":
                    board[row][column] = "O"
                    print("Player 2 added mark at the location", row, ',', column)
                    print_board()
                else:
                    print("****Board", row, ',', column, "has already been selected. Please try another spot!****")
                    print("**** Invalid choice. Please mark again! ****")
                    print_board_error()
            else:
                print("**** Invalid row or column. Please select row / col between values 0 to 2.")
                print("**** Invalid choice. Please mark again! ****")
                print_board_error()
        else:
            print("**** Invalid row or column. Please select row / col between values 0 to 2.")
            print("**** Invalid choice. Please mark again! ****")
            print_board_error()


def player_input():
    print("Make your move Player", playerid)
    rowinput = input("Enter row number (0-2):")
    columninput = input("Enter column number (0-2):")

    input_to_board(int(rowinput), int(columninput))


def switch_player():
    global firstturn
    global playerid
    if firstturn:
        playerid = 1

        firstturn = False
    else:
        if playerid == 1:
            playerid = 2
        elif playerid == 2:
            playerid = 1


print_board()
player_input()
