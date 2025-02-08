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
