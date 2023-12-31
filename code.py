######################################################
## A traditional TIC TAC TOE game written in PYTHON ##
######################################################


# Display Board: to display the board
import random


def display_board(board):
    print(f'{board[1]}  |  {board[2]}  |  {board[3]}')
    print('______________\n')
    print(f'{board[4]}  |  {board[5]}  |  {board[6]}')
    print('______________\n')
    print(f'{board[7]}  |  {board[8]}  |  {board[9]}')
    print('______________\n')


# PLAYER INPUT: function to take in a player input and assign their marker as 'X' or 'O'
def player_input():

    choice = 'wrong'

    while choice not in ['X', 'O']:

        choice = input('Player 1: Choose X or O: ').upper()

    if choice == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# PLACE MARKER: takes in board list object, a marker('X' or 'O'),
# and position (numbers 1-9) and assigns it to the board
def place_marker(board, marker, position):

    board[position] = marker
    return board


# WIN_CHECK: takes in board and a mark (X or O) and then checks to see if that mark has won
def win_check(board, mark):

    # WIN TIC TAC TOE?
    # check if all rows, all columns, 2 diagonals are same

    # rows
    board1 = board[1:4]
    board2 = board[4:7]
    board3 = board[7:10]

    # columns
    board4 = [board[1], board[4], board[7]]
    board5 = [board[2], board[5], board[8]]
    board6 = [board[3], board[6], board[9]]

    # diagonals
    board7 = [board[1], board[5], board[9]]
    board8 = [board[3], board[5], board[7]]

    def check_equal(boardlist):
        # all([true,true,true]) returns true
        if all(x == boardlist[0] for x in boardlist):
            return boardlist[0]
        else:
            return False

    listofboards = [board1, board2, board3,
                    board4, board5, board6, board7, board8]

    for b in listofboards:
        if mark == check_equal(b):
            # mark has won
            return True
        else:
            pass

    return False


# RANDOM PLAYER: to randomly decide which player goes first. returns a string of which player went first
def choose_first():

    player = random.randint(1, 2)

    return player


# NOT TO OVERWRITE: a function that returns a boolean indicating whether a space on the board is freely available.
def space_check(board, position):
    return board[position] == ''


# BOARD FULL: a function that checks if the board is full and returns a boolean value.
# True if full, False if otherwise.
def full_board_check(board):
    return '' not in board


# PLAYER CHOICE: ask for player's next position(1 to 9) and use function (space_check) to check if free space is available, if it is then return the position for later use
def player_choice(board):

    acceptable_range = [str(x) for x in range(1, 10)]
    choice = 'wrong'
    hasValue = False

    while choice not in acceptable_range or hasValue == True:

        choice = input('Input the position you want to play from 1-9: ')

        if (choice in acceptable_range):
            isFree = space_check(board, int(choice))
            if (isFree):
                return int(choice)

            else:
                print('This position already has a value and cannot be replaced')
                hasValue = True

# PLAY AGAIN: function to ask the player if they want to play again and returns a boolean True
# if they want to play again


def replay():

    wannaplay = 'wrong'

    while wannaplay not in ['N', 'Y']:

        wannaplay = input(
            'Would you want to continue playing the game? Y/N: ').upper()

        if wannaplay not in ['Y', 'N']:
            print('Sorry, I dont understand, please choose Y or N')

    return wannaplay == 'Y'


####################
## START THE GAME ##
####################


while (True):
    # SETUP THE VARIABLES FOR THE GAME
    print("Welcome to Tic Tac Toe!!")

    board = ['wrong', '', '', '', '', '', '', '', '', '']

    display_board(board)

    # Do you want to be player 'X' or player 'O'
    player1, player2 = player_input()

    # randomly choose a player to go first
    number = choose_first()
    print(f'Player {number} will go first')

    if number == 1:
        player = player1
    else:
        player = player2

    play_game = input('Ready to play? Y or N? ').upper()

    if (play_game == 'Y'):
        game_on = True
    else:
        game_on = False

    # ACTUAL GAME BEGINS
    while game_on == True:
        # while game_on:

        # Input the position you want to play ~ from 1-9
        position = player_choice(board)

        # check if empty space is available on board
        while (space_check(board, position) == False):

            # Input the position you want to play ~ from 1-9
            print("This position is full, choose another position")
            position = player_choice(board)

        # if available, update the board with 'X' or 'O' in the inputted position
        board = place_marker(board, player, position)

        # check to see if someone has won after each play!
        if (win_check(board, player)):
            print(f'GAME OVER!! {player} has won!!')
            display_board(board)
            break

        # check if all positions are full
        if (full_board_check(board)):
            print('Board is full, no one wins!')
            display_board(board)
            break

        print('Your current board')
        display_board(board)

        if (player == player1):
            player = player2
        else:
            player = player1

    if not replay():
        break
