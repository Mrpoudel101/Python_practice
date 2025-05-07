

import random
import os.path
import json
random.seed()

#making a function for the tic-tac-toe board

def draw_board(board):
    # develop code to draw the board
    print("--" * 9)
    for row in board:
        print(f"| {' | '.join(row)} |")
        print("--" * 9)


def welcome(board):
    # printing the welcome message
    
    print("----Welcome to Noughts and Crosses!----")
    draw_board(board)


def initialise_board(board):
    
    # using for loop
    for row in range(len(board)):
        for col in range(len(board[row])):
            board[row][col] = ' '
    return board


def get_player_move(board):
    # develop code to ask the user for the cell to put the X in,
    # and return row and col
    while True:
        move = input("Choose a cell to make your move. (1-9): ")
        row, col = (int(move[0]) - 1)//3, (int(move[0]) - 1)%3

        if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
            board[row][col] = 'X'
            return row, col
        else:
            print(" Please try again! Invalid cell!")

#creating a function for moves of computer

def choose_computer_move(board):
    
    while True:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if board[row][col] == ' ':
            board[row][col] = 'O'
            return row, col

# creating a function for checking who won the game(computer or user
def check_for_win(board, mark):
    
    for row in board:
        if all(cell == mark for cell in row):
            return True
    # check columns
    for col in range(3):
        if all(board[row][col] == mark for row in range(3)):
            return True
    # check diagonals
    if all(board[i][i] == mark for i in range(3)):
        return True
    if all(board[i][2-i] == mark for i in range(3)):
        return True
    return False

# A function for checking if all the spaces are fulfilled
def check_for_draw(board):
    
    for row in board:
        if any(cell == ' ' for cell in row):
            return False
    return True


#creating a function for playing the game
def play_game(board):
    # develop code to play the game
    # star with a call to the initialise_board(board) function to set
    # the board cells to all single spaces ' '
    # then draw the board
    initialise_board(board)
    
    draw_board(board)
    #Creating conditions using if -elif statement
    while True:
        row, col = get_player_move(board)
        draw_board(board)
        if check_for_win(board, 'X'):
            print("You won the game!")
            return 1
        # if not check for a draw by calling check_for_draw(board)
        elif check_for_draw(board):
            print("The game is a draw.")
            return 0
        # if not, then call choose_computer_move(board)
        # to choose a move for the computer
        row, col = choose_computer_move(board)
        draw_board(board)
        # update and draw the board
        # check if the computer has won by calling check_for_win(board, mark),
        if check_for_win(board, 'O'):
            print("Computer won the game!")
            return -1
        # if not check for a draw by calling check_for_draw(board)
        elif check_for_draw(board):
            print("The game is a draw.")
            return 0
        # repeat the loop
    return 0


#creating a function for asking user choice
def menu():
   
    while True:
        choice = input("1.To Play the game\n2.To Save score in file\n3.TO Load and display scores from file\nq. TO Quit\nMake your choice: ")
        if choice in ['1', '2', '3', 'q']:
            return choice

# function for loading leaderboards score in a python dictionary
def load_scores():
    
    if os.path.isfile('leaderboard.txt'):
        with open('leaderboard.txt', 'r') as f:
            leaders = json.load(f)
        return leaders
    else:
        return {}


#Function to prompt player name and storing them in the file leaderboard.txt
def save_score(score):
    
    name = input("Enter your name: ")
    leaders = load_scores()
    leaders[name] = score
    with open('leaderboard.txt', 'w') as f:
        json.dump(leaders, f)

# Gives leaderboard's content
def display_leaderboard(leaders):
    
    sorted_leaders = sorted(leaders.items(), key=lambda x: x[1], reverse=True)
    print("High Scores:")
    for name, score in sorted_leaders:
        print(f"{name}: {score}")