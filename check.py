def check_game(arr, user_choice):
    inflicted_loc = [[], [], []]
    row, col, num = user_choice
    game_case = True

    if num in arr[row]:
        game_case = False
        inflicted_loc[0] = [row, arr[row].index(num)]
        message = f"The number is already in this row!{str(inflicted_loc[0][0]+1 )},{str(inflicted_loc[0][1]+1)}"
    
    if num in [arr[i][col] for i in range(9)]:
        game_case = False
        inflicted_loc[1] = [[i, col] for i in range(9) if arr[i][col] == num]
        message = f"The number is already in this column!{str(inflicted_loc[1][0]+1 )},{str(inflicted_loc[1][1]+1)}"
    
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            r, c = start_row + i, start_col + j
            if arr[r][c] == num:
                game_case = False
                inflicted_loc[2] = [r, c]
                message = f"The number is already in this 3x3 box! {str(inflicted_loc[2][0]+1 )},{str(inflicted_loc[2][1]+1)}"

    if game_case:
        message = "Nice! What's your next move?:)"

    return arr, game_case, f"{message}\n", user_choice, inflicted_loc
