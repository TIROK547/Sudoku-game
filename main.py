from print import print_game
from check import check_game
from api import generate_sudoku
import copy
import time

GREEN, YELLOW, RED, BLUE, RESET = "\033[32m", "\033[93m", "\033[31m", "\033[96m", "\033[0m"
difficulty_levels = {0: 0.4, 1: 0.55, 2: 0.75}

def print_colored(text, color=RESET):
    print(f"{color}{text}{RESET}")

def get_valid_input(prompt, valid_range):
    while True:
        try:
            value = int(input(prompt))
            if value in valid_range:
                return value
            print_colored("⚠️ Invalid input! Please enter a valid number.", RED)
        except ValueError:
            print_colored("❌ Invalid input! Please enter numbers only.", RED)

def is_game_complete(board):
    return all(0 not in row for row in board)

print_colored("\n Welcome to Sudoku! 🎮\n", GREEN)

input_difficulty = get_valid_input(f"🎯 Choose difficulty {GREEN}Easy(1) {YELLOW}Medium(2) {RED}Hard(3){RESET}: ", range(1, 4)) - 1
sudoku = generate_sudoku(difficulty_levels[input_difficulty])
original_sudoku = copy.deepcopy(sudoku)

print_colored("\n🚀 **Game started**", BLUE)
print_game(sudoku, True, "🎲 What's your first move?", None, [[], []], original_sudoku)

correct_moves, wrong_moves = 0, 0
start_time = time.time()
move_saving = []

while not is_game_complete(sudoku):
    row = get_valid_input(f"📌 Row {YELLOW}(1-9){RESET}: ", range(1, 10)) - 1
    col = get_valid_input(f"📌 Column {YELLOW}(1-9){RESET}: ", range(1, 10)) - 1
    num = get_valid_input(f"🔢 Number {YELLOW}(1-9, 0 to reset){RESET}: ", range(0, 10))

    if num == 0:
        if original_sudoku[row][col] == 0:
            sudoku[row][col] = 0
            print_game(sudoku, True, "🔄 The value has been reset to default!", [row, col, num], [[], []], original_sudoku)
        else:
            print_game(sudoku, False, "⛔ You cannot change this value! It's from the base board!", [row, col, num], [[], []], original_sudoku)
        continue

    result = check_game(sudoku, [row, col, num])
    flag, message = result[1], result[2]

    if flag:
        sudoku[row][col] = num
        correct_moves += 1
    else:
        wrong_moves += 1

    move_saving.append([row, col])
    print_game(sudoku, flag, f"📍 {message}", [row, col, num], result[4], original_sudoku)

total_time = round(time.time() - start_time, 2)
print(f"\n🎯 Game Over! 🏆\n✅ Correct moves: {GREEN}{correct_moves}{RESET}\n❌ Wrong moves: {RED}{wrong_moves}{RESET}\n⏳ Gaming time: {BLUE}{total_time}{RESET} sec")
