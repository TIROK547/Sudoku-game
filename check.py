def check_game(arr, user_choice):
    inflicted_loc = [[], [], []]
    row, col, num = user_choice
    game_case = True
    #check if the number is inside the row
    if num in arr[row]:
        game_case = False
        inflicted_loc[0] = [row, arr[row].index(num)]
        message = f"⚠️ Oops! {num} is already in row {inflicted_loc[0][0]+1}, column {inflicted_loc[0][1]+1}.🔄 Try again! "
    #check if the number is inside the column
    if num in [arr[i][col] for i in range(9)]:
        game_case = False
        inflicted_loc[1] = [[i, col] for i in range(9) if arr[i][col] == num]
        message = f"🚫 Not allowed! {num} is already in column {inflicted_loc[1][0][0] + 1}, row {inflicted_loc[1][0][1] + 1}.🔢 Pick another number! "
    #check if the number is inside the box
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            r, c = start_row + i, start_col + j
            if arr[r][c] == num:
                game_case = False
                inflicted_loc[2] = [r, c]
                message = f"❌ Too bad! {num} is already in this 3×3 box (row {inflicted_loc[2][0]+1}, column {inflicted_loc[2][1]+1}).🎯 Try a different spot! "
    #if the move is correct were making a new message for the print
    if game_case:
        message = " Great choice! Keep going! 🚀 What's your next move?"

    return arr, game_case, f"{message}\n", user_choice, inflicted_loc
