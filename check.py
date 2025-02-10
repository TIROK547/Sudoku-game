from print import print_game


#easy_sudoku_boards = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
#                      [6, 0, 0, 1, 9, 5, 0, 0, 0],
#                      [0, 9, 8, 0, 0, 0, 0, 6, 0],
#                      [8, 0, 0, 0, 6, 0, 0, 0, 3],
#                      [4, 0, 0, 8, 0, 3, 0, 0, 1],
#                      [7, 0, 0, 0, 2, 0, 0, 0, 6],
#                      [0, 6, 0, 0, 0, 0, 2, 8, 0],
#                      [0, 0, 0, 4, 1, 9, 0, 0, 5],
#                      [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def check_game(arr, user_choice):
    inflicted_loc = [[],[]]
    row, col, num = user_choice
    message = ""
    game_case = None
    if num in arr[row]:
        message = "Number already in this row"
        game_case = False
        inflicted_loc[0].append(arr.index(arr[row]))
        inflicted_loc[0].append(arr[row].index(num))
    if num in [arr[i][col] for i in range(9)]:
        message = "Number already in this column"
        game_case = False
        for i in range(9):
            if arr[i][col] == num:
                inflicted_loc[1].append(i)
                inflicted_loc[1].append(col) 
                break
        print(inflicted_loc)
    message = "Number not in this column"
    game_case = True
    print("Number can be placed in the column")

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
                
    return (arr, game_case, message, user_choice,inflicted_loc)
#x = check_game(easy_sudoku_boards,[2,0,6])
#print(x[0],x[1],x[2],x[3],x[4])