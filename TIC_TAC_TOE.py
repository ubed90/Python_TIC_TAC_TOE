import os
import random

def clear():
    os.system( 'cls' )

def display_board(board):
    clear()    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def player_input():
    
    marker = ''
    
    while marker != "X" and marker != 'O':
        marker = input('Enter Your Choice X or O : ').upper()
        
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')


def place_marker(board, marker, position):
    
    board[position] = marker


def win_check(board, mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


def choose_first():
    
    decesion = random.randint(0,1)
    
    if decesion == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    
    return board[position] == ' '


def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
        
    return True


def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        if position < 10:
            try:
                position = int(input('Choose your next position: (1-9) ::  '))
            except:
                print("INAVLID INPUT!!!!")

        else:
            print('INAVLID INPUT!!!!')
            position = 0
        
    return position

def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')

while True:
    # print('Welcome to Tic Tac Toe!')
    # Set the game up here(Boards , Whos First ,  Choose Marker)
    the_board = [' '] * 10
    display_board(the_board)
    
    player1_marker , player2_marker = player_input()
    #Deciding Who will Go first
    turn = choose_first()
    
    print(turn + ' will play FIRST!!!')
    #Asking the players if they want to play
    play_game = ''
    
    while play_game != 'y' and play_game != 'n':
        play_game = input('Ready to Play? y/n : ').lower()
        continue
    #If yes tyen set Play_game variable as TRUE
    if play_game == 'y':
        game_on = True
    else:
        print('\nThanks For Playing')
        break

    while game_on:
        #Player_1 Turn
        if turn == 'Player 1':
            #show the Board
            display_board(the_board)
            
            #choose a position
            position  = player_choice(the_board)
            
            #place the marker on the position
            place_marker(the_board,player1_marker,position)
            
            #check if anyone Won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 Has Won !!!!')
                game_on = False
                
            else:
                #check if there's a tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print('THE GAME IS TIED!!!!')
                    game_on = False
                    
                else:
                    #No tie and No Win? Then Next Player's Turn
                    turn = 'Player 2'
        
        # Player2's turn.
        else:
            #show the Board
            display_board(the_board)
            
            #choose a position
            position  = player_choice(the_board)
            
            #place the marker on the position
            place_marker(the_board,player2_marker,position)
            
            #check if anyone Won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 Has Won !!!!')
                game_on = False
                
            else:
                #check if there's a tie
                if full_board_check(the_board):
                    print('THE GAME IS TIED!!!!')
                    game_on = False
                    
                else:
                    #No tie and No Win? Then Next Player's Turn
                    turn = 'Player 1'
            
            #pass

    if not replay():
        print('\nThanks For Playing')
        break