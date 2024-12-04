import random
move_counter = 0


# Step [1]: defining a function that prints out the display board

def display_board(board):
    print()
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print()

# Step [2]: defining a function that makes player 1 choose between X or O

def player_input():
    marker = '' #<--- universal marker

    while marker != 'X' and marker != 'O':
        marker = input('Hello there Player 1! Please choose between X or O: ').upper()

    if marker == 'X':
        return('X', 'O')
    else:
        return('O', 'X')

# Step [3]: defining a function that adds X or O at the chosen position on the board

def place_marker(board, marker, position):
    board[position] = marker

# Step [4]: defining a function that checks whether X or O has won the game

def win_check(board, mark):
    return((board[1] == mark and board[2] == mark and board[3] == mark) or
           (board[4] == board[5] == board[6] == mark) or
           (board[7] == board[8] == board[9] == mark) or
           (board[1] == board[4] == board[7] == mark) or
           (board[2] == board[5] == board[8] == mark) or
           (board[3] == board[6] == board[9] == mark) or
           (board[1] == board[5] == board[9] == mark) or
           (board[3] == board[5] == board[7] == mark))
            # checking for wins in horizontal, vertical and diagonal lines


# Step [5]: defining a function that gives information that the board is
#           clear to start the game

def space_check(board, position):
    return board[position] == ' '


# Step [6]: defining a function that checks for empty cells in the board,
#           if full it returns true, if not full it returns false 

def full_board_check(board):
    for x in range(1, 10):
        if space_check(board, x):
            return False
    return True

# Step[7]: defining function that asks the player to choose the next move

def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        
        try:
            position = int(input('\nEnter a number from 1-9 : '))
        except ValueError:
            print('\nThat is not a number! Try again!')
            continue

        if position < 1 or position > 9:
            print('\nThat number is out of range! Try again!')
            position = 0

        if board[position] != ' ':
            print('\nThat spot is already taken! Please choose an empty spot!')
            position = 0

    return position

# Step [8]: a function for a rematch

def replay():
    choice = input('Play again? Please enter Y or N : ').upper()
    print()
    return choice == 'y'.upper()

# Step [9]: a function that controls the computer's moves

def computer(board, position, marker):

    while not space_check(board, position):
        position = random.randint(1, 9)

    print('Player 2 makes a move at position {}!'.format(position))
    print()
    place_marker(board, marker, position)
    display_board(board)
    board[position] = marker

def log_file_move(move_counter, P1orP2, position, XorO):

    if position == 1:
        row = "1"
        column = "1"
    elif position == 2:
        row = "1"
        column = "2"
    elif position == 3:
        row = "1"
        column = "3"
    elif position == 4:
        row = "2"
        column = "1"
    elif position == 5:
        row = "2"
        column = "2"
    elif position == 6:
        row = "2"
        column = "3"
    elif position == 7:
        row = "3"
        column = "1"
    elif position == 8:
        row = "3"
        column = "2"
    elif position == 9:
        row = "3"
        column = "3"

    with open('C:/Users/Asus/Desktop/logfile_22079719.txt', 'a') as file:
        L1 = "\n"
        L2 = str(move_counter) + ", "
        L3 = str(P1orP2) + ", "
        L4 = row + ", " + column + ", "
        L5 = str(XorO)
        file.writelines([L1, L2, L3, L4, L5])

        
###########################################################################

# Last step: Looping all of it together

with open('logfile_22079719.txt', 'a') as file:
    L1 = '\n------Start Game------'
    L2 = str(move_counter) + ", "
    file.writelines([L1, L2])

print('Welcome to my game of Tic-Tac-Toe!')
print()

while True:

    the_board = [' ']*10
    p1_marker, p2_marker = player_input()

    turn = 'Player 1'
    print()
    print(turn + ' will go first!')
    print()
    game_on = True
    display_board(the_board)


    while game_on:

        if turn == 'Player 1':

            position = player_choice(the_board)
            place_marker(the_board, p1_marker, position)
            print('\nPlayer 1 marks position {} as their next turn!'.format(position))
            move_counter += 1
            print()

            if win_check(the_board, p1_marker):
                display_board(the_board)
                print('Congratulations! Player 1 has won a game of Tic-Tac-Toe!')
                print()
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The final result is a tie game!')
                    print()
                    game_on = False
                else:
                    the_board[position] = p1_marker
                    turn = 'Player 2'

        # computer's move
        else:
            computer(the_board, position, p2_marker)

            if win_check(the_board, p2_marker):
                print('Good job Player 2 for winning the game!\n')
                game_on = False
            else:
                if full_board_check(the_board):
                    print('The game has resulted in a tie!')
                    display_board(the_board)
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        print('Thank you for playing my game! See you later!')
        break

