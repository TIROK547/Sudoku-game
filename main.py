from print import print_game
from check import check_game
from boards import random_board
import time

difficulty_levels = ["easy", "medium", "hard"]
print("\033[32mWelcome ;D\033[0m ")
while True:
    input_difficulty = input("Please enter the difficulty of the game (\033[92measy,\033[93m medium,\033[91m hard\033[0m) : ").strip()
    if input_difficulty in difficulty_levels:
        break
    print("Please input a valid choice!!")

sudoku = random_board(input_difficulty)
original_board = sudoku.copy()

def is_game_complete(board):
    return all(0 not in row for row in board)
print("\n \033[96m**Game started**\033[0m \n")
print_game(sudoku, True, "Whats your first move?", None, [[], []],original_board)


correct_moves = 0
wrong_moves = 0
start_time = time.time()
move_saving = []

while not is_game_complete(sudoku):
    try:
        row = int(input("Row \033[93m(1 to 9)\033[0m: ")) - 1
        col = int(input("Column \033[93m(1 to 9)\033[0m: ")) - 1
        num = int(input("Number \033[93m(1 to 9)\033[0m: "))

        if not (0 <= row < 9 and 0 <= col < 9 and 0 <= num <= 9):
            print("Please enter a valid number: ")
            continue

        if original_board[row][col] != 0:
            print("You cannot change this value; it's from the base board!!")
            continue

        if num == 0:
            if sudoku[row][col] == 0:
                print("This box is already empty!!")
            else:
                sudoku[row][col] = 0
                print("This box has been cleared")

        else:
            result = check_game(sudoku, [row, col, num])
            flag, message = result[1], result[2]
            if flag:
                sudoku[row][col] = num
                correct_moves += 1
            else:
                wrong_moves += 1

            move_saving.append([row, col])
            print_game(sudoku, flag, message, [row, col, num], result[4],original_board)

    except ValueError:
        print("Please just enter numbers")

end_time = time.time()
total_time = round(end_time - start_time, 2)

print(f"Correct moves: {correct_moves}")
print(f"Wrong moves: {wrong_moves}")
print(f"Gaming time: {total_time} sec")
