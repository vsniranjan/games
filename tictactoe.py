# Tic Tac Toe
import random

theBoard = [" "," "," "," "," "," "," "," "," ", " " ]

def display_board(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def win_check(board,marker):  # Returns True or False
    
    return ((board[7] == marker and board[8] == marker and board[9] == marker) or # across the bottom
    (board[4] == marker and board[5] == marker and board[6] == marker) or # across the middle
    (board[1] == marker and board[2] == marker and board[3] == marker) or # across the top
    (board[7] == marker and board[4] == marker and board[1] == marker) or # down the left
    (board[8] == marker and board[5] == marker and board[2] == marker) or # down the middle
    (board[9] == marker and board[6] == marker and board[3] == marker) or # down the right 
    (board[7] == marker and board[5] == marker and board[3] == marker) or # diagonal
    (board[9] == marker and board[5] == marker and board[1] == marker)) # diagonal

def wining_positions(board, marker):
    winning_combinations = [
    [7, 8, 9], [4, 5, 6], [1, 2, 3],  # Rows
    [7, 4, 1], [8, 5, 2], [9, 6, 3],  # Columns
    [7, 5, 3], [9, 5, 1]  # Diagonals
    ]


def place_marker(board, position, marker):
    board[position] = marker
    display_board(theBoard)


def full_board(board):
    resp = True
    i = 1

    while (i <= 9):
        if board[i] != ' ':
            i = i + 1
        else:
            resp = False
            break
    
    return resp
    

def player_marker():
    marker = ''

    marker = input("Player1, Enter the marker (X or O): ")

    if marker == 'X':
        return ('X','O')
    else:
        return('O','X')


while True:

    turn = choose_first()
    print(turn, "will go first")
    player1_marker, player2_marker = player_marker()



    play_game = input("Are you ready to start (y/n)? ")

    print()
    print("=======The Board=======")
    print()
    display_board(theBoard)

    
    if play_game.lower()[0] == 'y':
        gameOn = True
    else:
        gameOn = False

    while gameOn:

        if turn == 'Player 1':


            pos = int(input("Player 1: Enter the position you want to play in: "))
            
            if (theBoard[pos] != " "):
                print()
                print("You cant place a marker there! Try again ")
                print()
                continue
                

            place_marker(theBoard, pos, player1_marker)

            if win_check(theBoard, player1_marker) == True:
                print("Congratulations Player 1 has won!")
                break
            else:
                if full_board(theBoard) == True:
                    print("The game has resulted in a draw!")
                    break
                else:
                    turn = "Player 2"


        else:
            pos = int(input("Player 2: Enter the position you want to play in: "))
            
            if (theBoard[pos] != " "):
                print()
                print("You cant place a marker there! Try again")
                print()
                continue

            place_marker(theBoard, pos, player2_marker)

            if win_check(theBoard, player1_marker) == True:
                print("Congratulations Player 2 has won!")
                break
            else:
                if full_board(theBoard) == True:
                    print("The game has resulted in a draw!")
                    break
                else:
                    turn = "Player 1"

    break
