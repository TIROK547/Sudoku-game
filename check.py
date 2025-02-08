from pprint import pprint

game = [
    [0, 2, 0, 6, 0, 8, 0, 0, 0],
    [5, 8, 0, 0, 0, 9, 7, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 0],
    [3, 7, 0, 0, 0, 0, 5, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 8, 0, 0, 0, 0, 1, 3],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 9, 8, 0, 0, 0, 3, 6],
    [0, 0, 0, 3, 0, 6, 0, 9, 0]
]

def check_game(arr, user_choice):
    row, col, num = user_choice
    message = ""
    game_case = None
    if arr[row][col] != 0:
        message = "This cell is already filled"
        game_case = False
    if num in arr[row]:
        message = "Number already in this row"
        game_case = False
    if num in [arr[i][col] for i in range(9)]:
        message = "Number already in this column"
        game_case = False
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if arr[start_row + i][start_col + j] == num:
                message = "Number already in this box"
                game_case = False
                break
    
    if all(all(cell != 0 for cell in row) for row in arr):
                message = "Congratulations! You won!"
                game_case = True
                
    return [arr, game_case, message, user_choice]

pprint(check_game(game, [8, 0, 1])) 
