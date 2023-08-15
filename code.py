# Display Board: to display the board

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

        choice = input("Do you want to be player X or player O?: ").upper()

    if choice == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
