#!/usr/bin/env python
# coding: utf-8

# Initilize variables
number_of_players = 2
m = 4
n = 4
input_history = []
winner_sum_array = []
game_matrix = []
game_board = []
winner_sum_array = [0]*(number_of_players + 1)

# Initialize game variables
player_number = 1
player_input = '-'
game_response = 'PLAY'

for index, player_sum in enumerate(winner_sum_array):
    winner_sum_array[index] = pow(index, n) 

# Initialize correct result product array
def multiplyList(myList) :       
    result = 1
    for x in myList: 
        result = result * x  
    return result 

game_matrix = [[0 for _ in range(m)] for _ in range(n)]
game_board = game_matrix.copy()
game_board.append([x for x in range(1, n + 1)])

# Display 4x4 Game Board in current state
def display_board():
    for index, row in enumerate(game_board):
        if index == n:
            print('|----|')
        print('|', end='', flush=True)
        for col in game_board[index]:
            print(col, end='', flush=True)
        print('|')
    print()

# Check if a sequence exists
def sequence(player_number):
    col_sum = [multiplyList(x) for x in zip(*game_matrix)]
#     print('col prod: ', col_sum)
    if winner_sum_array[player_number] in col_sum:
        return True
    else:
        row_sum = [multiplyList(x) for x in game_matrix]
#         print('row prod: ', row_sum)
        if winner_sum_array[player_number] in row_sum:
            return True
        else:  
            sum_first_diagonal = multiplyList(game_matrix[i][i] for i in range(m))
#             print('d1 prod: ', sum_first_diagonal)
            if winner_sum_array[player_number] is sum_first_diagonal:
                return True
            else:
                sum_second_diagnol = multiplyList(game_matrix[i][n-i-1] for i in range(m))
#                 print('d2 prod: ', sum_second_diagnol)
                if winner_sum_array[player_number] is sum_second_diagnol:
                    return True
                else:
                    return False

# Play a move on the game board
def make_move(player_input, player_number):
    if player_input > n:
        return 'ERROR'
    column_list = [row[player_input-1] for row in game_matrix]
    for index, col in enumerate(column_list):
        reverse_index = -(index + 1)
        if column_list[reverse_index] is 0:
            game_matrix[reverse_index][player_input-1] = player_number
            input_history.append(player_input)
            
            # Check for sequence
            if len(input_history) >= 7:
            
                if sequence(player_number):
                    return 'WIN'
                elif len(input_history) is 16:
                    return 'DRAW'
                else:
                    return 'OK'
            else:
                return 'OK'
            break
        elif index is len(column_list) - 1:
            return 'ERROR'


# get input history from player
def get_input_history():
    for inp in input_history:
        print(inp)

print('------------- 9DT --------------')
print('Type one of the following options:')
print('GET - Retrieve all past moves')
print('BOARD - See the current board')
print('PUT column_number - Place your coin on the board')
print('EXIT - Exit game')
while(not player_input == 'EXIT'):
    player_input = str(input())
    if player_input == 'GET':
        get_input_history()
    elif player_input == 'BOARD':
        display_board()
    elif player_input == 'RESTART':
        restart_game()
    elif 'PUT' in player_input:
        player_input_col = int(player_input.split(' ')[1])
        if not game_response == 'WIN' and not game_response == 'DRAW':
            game_response = make_move(player_input_col, player_number)
            print(game_response)
            print()
            if not game_response == 'ERROR':
                if player_number is 1:
                    player_number = 2
                else:
                    player_number = 1
        else:
            print('Game Over!')
    elif not player_input == 'EXIT':
        print('Unknown Input. Please try again')
