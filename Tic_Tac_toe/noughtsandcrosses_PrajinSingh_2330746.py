import random
import os.path
import json
random.seed()

mark = "X"

def draw_board(board):
    # develop code to draw the board
    print("  -----------")
    print(" | " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("  -----------")
    print(" |", board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print("  -----------")
    print(" |", board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
    print("  -----------")
    pass


def welcome(board):
    # prints the welcome message
    # display the board by calling draw_board(board)
    print('\nWelcome to the "Unbeatable Noughts and Crosses" game.')
    print("The board layout is shown below:")
    draw_board(board)
    print("When prompted, enter the number corresponding to the square you want.")
    pass


def initialise_board(board):
    # develop code to set all elements of the board to one space ' '
    board[0][0] = ' '
    board[0][1] = ' '
    board[0][2] = ' '
    board[1][0] = ' '
    board[1][1] = ' '
    board[1][2] = ' '
    board[2][0] = ' '
    board[2][1] = ' '
    board[2][2] = ' '
    return board


def get_player_move(board):
    # develop code to ask the user for the cell to put the X in,
    # and return row and col
    global col, row
    while True:
        try:
            if board[0][0] != " " and board[0][1] != " " and board[0][2] != " " \
                    and board[1][0] != " " and board[1][1] != " " and board[1][2] != " " \
                    and board[2][0] != " " and board[2][1] != " " and board[2][2] != " ":
                break
            else:
                inn = int(input('''\n                    1 2 3
                    4 5 6
Choose your square: 7 8 9 : '''))
                if inn > 1 or inn < 9:
                    if inn == 1:
                        row = inn - 1
                        col = inn - 1
                        if board[row][col] == ' ':
                            board[row][col] = "X"
                            print("")
                            print(f''' -----------
| {board[0][0]} | {board[0][1]} | {board[0][2]} |
 -----------
| {board[1][0]} | {board[1][1]} | {board[1][2]} |
 -----------
| {board[2][0]} | {board[2][1]} | {board[2][2]} |
 -----------''')
                            break
                        else:
                            print("\n Cell Occupied")
                    elif inn == 2:
                        row = inn - 2
                        col = inn - 1
                        if board[row][col] == ' ':
                            board[row][col] = "X"
                            print("")
                            print(f''' -----------
| {board[0][0]} | {board[0][1]} | {board[0][2]} |
 -----------
| {board[1][0]} | {board[1][1]} | {board[1][2]} |
 -----------
| {board[2][0]} | {board[2][1]} | {board[2][2]} |
 -----------''')
                            break
                        else:
                            print("\n Cell Occupied")
                    elif inn == 3:
                        row = inn - 3
                        col = inn - 1
                        if board[row][col] == ' ':
                            board[row][col] = "X"
                            print("")
                            print(f''' -----------
| {board[0][0]} | {board[0][1]} | {board[0][2]} |
 -----------
| {board[1][0]} | {board[1][1]} | {board[1][2]} |
 -----------
| {board[2][0]} | {board[2][1]} | {board[2][2]} |
 -----------''')
                            break
                        else:
                            print("\n Cell Occupied")
                    elif inn == 4:
                        row = inn - 3
                        col = inn - 4
                        if board[row][col] == ' ':
                            board[row][col] = "X"
                            print("")
                            print(f''' -----------
| {board[0][0]} | {board[0][1]} | {board[0][2]} |
 -----------
| {board[1][0]} | {board[1][1]} | {board[1][2]} |
 -----------
| {board[2][0]} | {board[2][1]} | {board[2][2]} |
 -----------''')
                            break
                        else:
                            print("\n Cell Occupied")
                    elif inn == 5:
                        row = inn - 4
                        col = inn - 4
                        if board[row][col] == ' ':
                            board[row][col] = "X"
                            print("")
                            print(f''' -----------
| {board[0][0]} | {board[0][1]} | {board[0][2]} |
 -----------
| {board[1][0]} | {board[1][1]} | {board[1][2]} |
 -----------
| {board[2][0]} | {board[2][1]} | {board[2][2]} |
 -----------''')
                            break
                        else:
                            print("\n Cell Occupied")
                    elif inn == 6:
                        row = inn - 5
                        col = inn - 4
                        if board[row][col] == ' ':
                            board[row][col] = "X"
                            print("")
                            print(f''' -----------
| {board[0][0]} | {board[0][1]} | {board[0][2]} |
 -----------
| {board[1][0]} | {board[1][1]} | {board[1][2]} |
 -----------
| {board[2][0]} | {board[2][1]} | {board[2][2]} |
 -----------''')
                            break
                        else:
                            print("\n Cell Occupied")
                    elif inn == 7:
                        row = inn - 5
                        col = inn - 7
                        if board[row][col] == ' ':
                            board[row][col] = "X"
                            print("")
                            print(f''' -----------
| {board[0][0]} | {board[0][1]} | {board[0][2]} |
 -----------
| {board[1][0]} | {board[1][1]} | {board[1][2]} |
 -----------
| {board[2][0]} | {board[2][1]} | {board[2][2]} |
 -----------''')
                            break
                        else:
                            print("\n Cell Occupied")
                    elif inn == 8:
                        row = inn - 6
                        col = inn - 7
                        if board[row][col] == ' ':
                            board[row][col] = "X"
                            print("")
                            print(f''' -----------
| {board[0][0]} | {board[0][1]} | {board[0][2]} |
 -----------
| {board[1][0]} | {board[1][1]} | {board[1][2]} |
 -----------
| {board[2][0]} | {board[2][1]} | {board[2][2]} |
 -----------''')
                            break
                        else:
                            print("\n Cell Occupied")
                    elif inn == 9:
                        row = inn - 7
                        col = inn - 7
                        if board[row][col] == ' ':
                            board[row][col] = "X"
                            print("")
                            print(f''' -----------
| {board[0][0]} | {board[0][1]} | {board[0][2]} |
 -----------
| {board[1][0]} | {board[1][1]} | {board[1][2]} |
 -----------
| {board[2][0]} | {board[2][1]} | {board[2][2]} |
 -----------''')
                            break
                        else:
                            print("\n Cell Occupied")
                    else:
                        print("\n  Invalid cell")
                    print(f'''  -----------
 | {board[0][0]} | {board[0][1]} | {board[0][2]} |
  -----------
 | {board[1][0]} | {board[1][1]} | {board[1][2]} |
  -----------
 | {board[2][0]} | {board[2][1]} | {board[2][2]} |
  -----------''')

        except ValueError:
            print("\n Invalid cell")
            print(f''' -----------
| {board[0][0]} | {board[0][1]} | {board[0][2]} |
 -----------
| {board[1][0]} | {board[1][1]} | {board[1][2]} |
 -----------
| {board[2][0]} | {board[2][1]} | {board[2][2]} |
 -----------''')
    return row, col


def choose_computer_move(board):
    # develop code to let the computer chose a cell to put a nought in
    # and return row and col
    global row, col
    while True:
        count = 0
        if board[0][0] != " " and board[0][1] != " " and board[0][2] != " " \
                and board[1][0] != " " and board[1][1] != " " and board[1][2] != " " \
                and board[2][0] != " " and board[2][1] != " " and board[2][2] != " ":
            break
        else:
            inn = random.randint(1, 9)
            if inn > 1 or inn < 9:
                if inn == 1:
                    row = inn - 1
                    col = inn - 1
                    if board[row][col] == ' ':
                        board[row][col] = "O"
                        print("The computer chosen square is: ", inn)
                        print(f''' -----------
| {board[0][0]} | {board[0][1]} | {board[0][2]} |
 -----------
| {board[1][0]} | {board[1][1]} | {board[1][2]} |
 -----------
| {board[2][0]} | {board[2][1]} | {board[2][2]} |
 -----------''')
                        break
                    else:
                        print("\n Cell Occupied")
                elif inn == 2:
                    row = inn - 2
                    col = inn - 1
                    if board[row][col] == ' ':
                        board[row][col] = "O"
                        print("The computer chosen square is: ", inn)
                        print(f''' -----------
| {board[0][0]} | {board[0][1]} | {board[0][2]} |
 -----------
| {board[1][0]} | {board[1][1]} | {board[1][2]} |
 -----------
| {board[2][0]} | {board[2][1]} | {board[2][2]} |
 -----------''')
                        break
                    else:
                        print("\n Cell Occupied")
                elif inn == 3:
                    row = inn - 3
                    col = inn - 1
                    if board[row][col] == ' ':
                        board[row][col] = "O"
                        print("The computer chosen square is: ", inn)
                        print(f''' -----------
| {board[0][0]} | {board[0][1]} | {board[0][2]} |
 -----------
| {board[1][0]} | {board[1][1]} | {board[1][2]} |
 -----------
| {board[2][0]} | {board[2][1]} | {board[2][2]} |
 -----------''')
                        break
                    else:
                        print("\n Cell Occupied")
                elif inn == 4:
                    row = inn - 3
                    col = inn - 4
                    if board[row][col] == ' ':
                        board[row][col] = "O"
                        print("The computer chosen square is: ", inn)
                        print(f''' -----------
| {board[0][0]} | {board[0][1]} | {board[0][2]} |
 -----------
| {board[1][0]} | {board[1][1]} | {board[1][2]} |
 -----------
| {board[2][0]} | {board[2][1]} | {board[2][2]} |
 -----------''')
                        break
                    else:
                        print("\n Cell Occupied")
                elif inn == 5:
                    row = inn - 4
                    col = inn - 4
                    if board[row][col] == ' ':
                        board[row][col] = "O"
                        print("The computer chosen square is: ", inn)
                        print(f''' -----------
| {board[0][0]} | {board[0][1]} | {board[0][2]} |
 -----------
| {board[1][0]} | {board[1][1]} | {board[1][2]} |
 -----------
| {board[2][0]} | {board[2][1]} | {board[2][2]} |
 -----------''')
                        break
                    else:
                        print("\n Cell Occupied")
                elif inn == 6:
                    row = inn - 5
                    col = inn - 4
                    if board[row][col] == ' ':
                        board[row][col] = "O"
                        print("The computer chosen square is: ", inn)
                        print(f''' -----------
| {board[0][0]} | {board[0][1]} | {board[0][2]} |
 -----------
| {board[1][0]} | {board[1][1]} | {board[1][2]} |
 -----------
| {board[2][0]} | {board[2][1]} | {board[2][2]} |
 -----------''')
                        break
                    else:
                        print("\n Cell Occupied")
                elif inn == 7:
                    row = inn - 5
                    col = inn - 7
                    if board[row][col] == ' ':
                        board[row][col] = "O"
                        print("The computer chosen square is: ", inn)
                        print(f''' -----------
| {board[0][0]} | {board[0][1]} | {board[0][2]} |
 -----------
| {board[1][0]} | {board[1][1]} | {board[1][2]} |
 -----------
| {board[2][0]} | {board[2][1]} | {board[2][2]} |
 -----------''')
                        break
                    else:
                        print("\n Cell Occupied")
                elif inn == 8:
                    row = inn - 6
                    col = inn - 7
                    if board[row][col] == ' ':
                        board[row][col] = "O"
                        print("The computer chosen square is: ", inn)
                        print(f''' -----------
| {board[0][0]} | {board[0][1]} | {board[0][2]} |
 -----------
| {board[1][0]} | {board[1][1]} | {board[1][2]} |
 -----------
| {board[2][0]} | {board[2][1]} | {board[2][2]} |
 -----------''')
                        break
                    else:
                        print("\n Cell Occupied")
                elif inn == 9:
                    row = inn - 7
                    col = inn - 7
                    if board[row][col] == ' ':
                        board[row][col] = "O"
                        print("The computer chosen square is: ", inn)
                        print(f''' -----------
| {board[0][0]} | {board[0][1]} | {board[0][2]} |
 -----------
| {board[1][0]} | {board[1][1]} | {board[1][2]} |
 -----------
| {board[2][0]} | {board[2][1]} | {board[2][2]} |
 -----------''')
                        break
                    else:
                        print("\n Cell Occupied")
                else:
                    print("\n  Invalid cell")
                print(f'''      -----------
     | {board[0][0]} | {board[0][1]} | {board[0][2]} |
      -----------
     | {board[1][0]} | {board[1][1]} | {board[1][2]} |
      -----------
     | {board[2][0]} | {board[2][1]} | {board[2][2]} |
      -----------''')
    return row, col


def check_for_win(board, mark):
    # develop code to check if either the player or the computer has won
    # return True if someone won, False otherwise
    # rows wise check
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] == mark:
        return True
    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] == mark:
        return True
    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] == mark:
        return True

    # column wise check
    elif board[0][0] == board[1][0] == board[2][0] and board[0][0] == mark:
        return True
    elif board[0][1] == board[1][1] == board[2][1] and board[2][1] == mark:
        return True
    elif board[0][2] == board[1][2] == board[2][2] and board[1][2] == mark:
        return True

    # diagonal check
    elif board[0][2] == board[1][1] == board[2][0] and board[2][0] == mark:
        return True
    elif board[0][0] == board[1][1] == board[2][2] and board[1][1] == mark:
        return True

def check_for_draw(board):
    # develop cope to check if all cells are occupied
    # return True if it is, False otherwise
    if board[0][0] != " " and board[0][1] != " " and board[0][2] != " " \
            and board[1][0] != " " and board[1][1] != " " and board[1][2] != " " \
            and board[2][0] != " " and board[2][1] != " " and board[2][2] != " ":
        return True
    else:
        return False


def play_game(board):
    # develop code to play the game
    # star with a call to the initialise_board(board) function to set
    # the board cells to all single spaces ' '
    initialise_board(board)
    # then draw the board
    draw_board(board)
    # then in a loop, get the player move, update and draw the board
    while True:
        global mark
        get_player_move(board)
        if mark == 'X':
            mark = "O"
        else:
            mark = 'X'

        # check if the player has won by calling check_for_win(board, mark),
        # if so, return 1 for the score
        if check_for_win(board, "X"):
            print("You won!!")
            return 1

        # if not check for a draw by calling check_for_draw(board)
        # if drawn, return 0 for the score
        draw = check_for_draw(board)
        if draw == True:
            print("It's a tie")
            return 0

        # if not, then call choose_computer_move(board)
        # to choose a move for the computer
        # update and draw the board
        choose_computer_move(board)
        if mark == 'X':
            mark = "O"
        else:
            mark = 'X'

        # check if the computer has won by calling check_for_win(board, mark),
        # if so, return -1 for the score
        if check_for_win(board, "O"):
            print("You lost!!")
            return -1
        # if not check for a draw by calling check_for_draw(board)
        # if drawn, return 0 for the score

        draw = check_for_draw(board)
        if draw == True:
            print("It's a tie")
            return 0
        if mark == 'X':
            mark = "O"
        else:
            mark = 'X'

    # repeat the loop



def menu():
    # get user input of either '1', '2', '3' or 'q'
    global score
    while True:
        choice = input('''\nMenu:
        (1) Start Game
        (2) Save Score
        (3) Load Score
        (q) End the program ''').lower()
        # 1 - Play the game
        if choice == '1':
            print("\nLoading Game...")
        # 2 - Save score in file 'leaderboard.txt'
        elif choice == '2':
            print("\n Saving score...")
        # 3 - Load and display the scores from the 'leaderboard.txt'
        elif choice == '3':
            print("\nDisplaying score... ")
        # q - End the program
        elif choice == 'q':
            print("Exiting...")
        else:
            print("Invalid Menu")
        return choice

def load_scores():
    # develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # return the scores in a Python dictionary
    # with the player names as key and the scores as values
    # return the dictionary in leaders
    try:
        f = open("leaderboard.txt", "r")
        leaders = f.read()
        return leaders
    except FileNotFoundError:
        print("No 'leaderboard.txt' file found.")

def save_score(score):
    # develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'
    check = os.path.isfile("leaderboard.txt")
    if check == True:
        name = input("Enter your name: ")
        data = {name: score}
        data_json = json.dumps(data)
        f = open("leaderboard.txt", "w")
        score = f.write(str(data))
        f.close()
    else:
        print("\n File 'Leaderboard.txt' not available to save.")
        print("Create a text file 'leaderboard.txt' in the current directory to save the score.")
    return

def display_leaderboard(leaders):
    # develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader
    print(f"Leaderboard Scores:\n{leaders}")
    pass