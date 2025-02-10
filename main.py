from print import*
from check import*
import time
import random
import json
import os


file_path = os.path.join("datas", "data.json")
with open(file_path, "r", encoding="utf-8") as file:
    data= json.load(file)

easy_sudoku_boards = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                      [6, 0, 0, 1, 9, 5, 0, 0, 0],
                      [0, 9, 8, 0, 0, 0, 0, 6, 0],
                      [8, 0, 0, 0, 6, 0, 0, 0, 3],
                      [4, 0, 0, 8, 0, 3, 0, 0, 1],
                      [7, 0, 0, 0, 2, 0, 0, 0, 6],
                      [0, 6, 0, 0, 0, 0, 2, 8, 0],
                      [0, 0, 0, 4, 1, 9, 0, 0, 5],
                      [0, 0, 0, 0, 8, 0, 0, 7, 9]]
medium_sudoku_boards = []


hard_sudoku_boards = []

input_1 = int (input("please choose dificulties of the game from 1 to 3 (easy, medium, hard)"))

if input_1 == 1:
    sudoku = random.choice(easy_sudoku_boards)
elif input_1 == 2:
    sudoku = random.choice(medium_sudoku_boards)
elif input_1 == 3:
    sudoku = random.choice(hard_sudoku_boards)
else:
    print("invalid number please enter another numer: ")

original_board = [row[:] for row in sudoku]

incorrect_moves = set()

# def print_game(sudoku, original_board, incorrect_moves):
   



#     print()



# def check_game(board, row, col, num):
   
   
   
#    print()

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