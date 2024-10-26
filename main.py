import random as rn

board = [i for i in range(1,10)]
print("\n The rules are pretty simple, or is it?")
print(f"""
     {board[0]} | {board[1]} | {board[2]} 
    ---+---+---
     {board[3]} | {board[4]} | {board[5]} 
    ---+---+---
     {board[6]} | {board[7]} | {board[8]} 
    """)
# print("\n 1 | 2 | 3 \n 4 | 5 | 6 \n 7 | 8 | 9")


valid = [[1,2,3], [4,5,6], [7,8,9], [1,5,9], [3,5,7], [1,4,7], [2,5,8], [3,6,9]]

player_one = []
player_two = []

available_moves = [1,2,3,4,5,6,7,8,9]

# Function to display the board
def display_board():
    board = [' ' for i in range(1,10)]
    for move in player_one:
        board[move - 1] = 'X'
    for move in player_two:
        board[move - 1] = 'X'
    
    print(f"""
     {board[0]} | {board[1]} | {board[2]} 
    ---+---+---
     {board[3]} | {board[4]} | {board[5]} 
    ---+---+---
     {board[6]} | {board[7]} | {board[8]} 
    """)

while True:
    display_board()

    # Player 1's turn
    player1_input = int(input("player 1: "))
    if player1_input in available_moves:
        player_one.append(player1_input)
        available_moves.remove(player1_input)
        player_one.sort()
    elif player1_input not in available_moves:
        print("try again")
        continue

    # Check if player 1 has won
    for combo in valid:
        if set(combo).issubset(player_one):
            display_board()
            print("i think someone won")
            exit()

    # Check for draw
    if not available_moves:
        display_board()
        print("uhhhh ig thats it")
        break

    display_board()

    # Player 2's turn
    player2_input = int(input("player 2: "))
    
    if player2_input in available_moves:
        player_two.append(player2_input)
        available_moves.remove(player2_input)
        player_two.sort()
    elif  player2_input not in available_moves:
        print("try again")
        continue

    # Check if player 2 has won
    for combo in valid:
        if set(combo).issubset(player_two):
            display_board()
            print("i think someone won")
            exit()

    if not available_moves:
        display_board()
        print("uhhhh ig thats it")
        break
