from print import*
from check import*
from boards import random_board
import time
import random
import json
import os



difficulty_levels = ["easy", "medium", "hard"]
while True:
    input_difficulty = input("please enter dificulty of the game from (easy, medium, hard)").strip()
    if input_difficulty in difficulty_levels:
        break
    print("please input a valid choice!!")

sudoku = random_board(input_difficulty)

original_board = [row[:] for row in sudoku]

incorrect_moves = set()



def is_game_complete(board):
    return all(0 not in row for row in board)

print("**game started**")
print_game(sudoku, original_board, incorrect_moves)

correct_moves = 0 
wrong_moves = 0
start_time = time.time()

while not is_game_complete(sudoku):
   
   try:
        row = int(input("please enter the row number between ( 1 to 9 ): ")) -1
        col = int(input("please enter the column number between ( 1 to 9 ): ")) -1
        num = int(input("please enter the value number between ( 1 to 9 ): "))

        if not (0 <= row < 9 and 0 <= col < 9 and 0 <= num <= 9):
            print("please enter a valid number: ")
            continue
        
        if original_board[row][col] != 0:
            print("you can not change this value its from base board!!")
            continue

        if num == 0:
            if sudoku[row][col] == 0:
                print("this box is already empty!!")
            else:
                sudoku[row][col] = 0
                incorrect_moves.discard((row, col))
                print("this box has been cleared")

        elif check_game(sudoku, row, col, num):
            sudoku[row][col] = num
            correct_moves += 1
            incorrect_moves.discard((row, col))
            print("changes accepted")
        else:
            wrong_moves += 1
            sudoku[row][col] = num
            incorrect_moves.add((row, col))
            print("invalid change, this number is repetitive")
        
        print_game(sudoku, original_board, incorrect_moves)

      
   except ValueError:
       print("please just enter numbers")
       
end_time = time.time()
total_time = round(end_time - start_time, 2)

print("**congratulations, you won**")
print(f"correct moves: {correct_moves}")
print(f"wrong movese: {wrong_moves}")
print(f"gaming time: {total_time} sec")