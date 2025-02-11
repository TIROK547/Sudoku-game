convert_num = lambda num: "\033[33m.\033[0m" if num == 0 else f"\033[33m{str(num)}\033[0m"
def print_game(game_board, game_case, message, user_choice, inflicted_loc,original_board):
    
    row, col, num = user_choice if user_choice else (-1, -1, -1)

    print("\033[94m------\033[31m#\033[94m\033[0mSUD-OKU\033[94m\033[31m#\033[94m------\033[0m")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("\033[94m------#-------#------\033[0m")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("\033[94m|\033[0m", end=" ")

            if [i, j] in inflicted_loc and game_board[i][j] != 0:
                print('\033[31m' + str(game_board[i][j]) + '\033[0m', end=" ")
            #elif (i, j) == (row, col):
            #    if game_case is True or game_case == None:
            #        print('\033[33m' + str(num) + '\033[0m', end=" ")
            #    elif game_case is False:
            #        print('\033[31m' + str(num) + '\033[0m', end=" ")
            else:
                print(str(original_board[i][j]) if original_board[i][j] != 0 else convert_num(game_board[i][j]), end=" ")

        print()
    
    print("\033[94m------\033[31m*\033[94m-------\033[31m*\033[94m------\033[0m")
    if game_case is True or game_case is None:
        print("\n\033[94m" + message +"\033[0m")
    else:
        print("\n\033[31m" + message + '\033[0m')
