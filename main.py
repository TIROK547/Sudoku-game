from print import*
from check import*
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

def print_board(sudoku):
    print_game(sudoku)

    
    
    
    
    print()



def check_board(board, row, col, num):
    return check_game(sudoku, row, col, num)
    
    print ()


while True:
   try:
        row = int(input("please enter the row number between ( 1 to 9 ): "))
        col = int(input("please enter the column number between ( 1 to 9 ): "))
        num = int(input("please enter the value number between ( 1 to 9 ): "))

        if not (0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9):
            print("please enter a valid number: ")
            continue
        if sudoku[row][col] != 0:
            print("this box is already has compleated, please enter other boxes location: ")
            continue
        if check_board(sudoku, row, col, num):
            sudoku[row][col] = num 
            print("changes accepted")
            print_board(sudoku)
        else:
            print("invalid move please check the rows or columns ")
   except ValueError:
       print("please just enter numbers")
       