def check_game(arr, user_choice):
    inflicted_loc = [[], []]
    row, col, num = user_choice
    message = ""
    game_case = True

    if num in arr[row]:
        message = "The number is already in this row!"
        game_case = False
        inflicted_loc[0].append(arr.index(arr[row]))
        inflicted_loc[0].append(arr[row].index(num))
    if num in [arr[i][col] for i in range(9)]:
        message = "The number is already in this column!"
        game_case = False
        for i in range(9):
            if arr[i][col] == num:
                inflicted_loc[1].append(i)
                inflicted_loc[1].append(col) 
                break
        print(inflicted_loc) 

    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if arr[start_row + i][start_col + j] == num:
                message = "The same number is already in this box!"
                game_case = False

    if game_case:
        message = "Nice! whats your next move?:)"
    message += '\n'
    print(inflicted_loc)
    return arr, game_case, message, user_choice, inflicted_loc
