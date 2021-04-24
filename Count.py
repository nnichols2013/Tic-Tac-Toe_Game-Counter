# count the number of valid tic tac toe games

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
total = 0


def print_board():
    for x in range(3):
        print(board[x])
    print()


# check if either player wins
def complete():
    # rows
    if board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0] != ' ':
        return True
    if board[1][0] == board[1][1] and board[1][0] == board[1][2] and board[1][0] != ' ':
        return True
    if board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[2][0] != ' ':
        return True

    # columns
    if board[0][0] == board[1][0] and board[0][0] == board[2][0] and board[0][0] != ' ':
        return True
    if board[0][1] == board[1][1] and board[0][1] == board[2][1] and board[0][1] != ' ':
        return True
    if board[0][2] == board[1][2] and board[0][2] == board[2][2] and board[0][2] != ' ':
        return True

    # diagonal
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != ' ':
        return True
    if board[2][0] == board[1][1] and board[2][0] == board[0][2] and board[2][0] != ' ':
        return True

    return False


def count(row, col, team):
    temp = board[row][col]      # save value and restore upon return
    board[row][col] = team
    if complete():              # restore and increment

        # Uncomment to print all of the games
        # print_board()

        board[row][col] = temp
        global total; total += 1; return

    new_team = 'X' if team != 'X' else 'O'
    for x in range(3):
        for y in range(3):
            if board[x][y] == ' ':
                count(x, y, new_team)
    board[row][col] = temp


def count_all():
    for x in range(3):
        for y in range(3):
            count(x, y, 'X')


count_all()
print(total)