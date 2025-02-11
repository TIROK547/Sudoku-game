CONVERT_NUM = lambda num: "." if num == 0 else str(num)

BLUE, RED, YELLOW, RESET, UNDERLINE = "\033[94m", "\033[31m", "\033[33m", "\033[0m", "\033[4m"

def print_game(game_board, game_case, message, user_choice, inflicted_loc, original_board):
    print("")
    row, col, num = user_choice if user_choice else (-1, -1, -1)

    print(f"{BLUE}------{RED}#{BLUE}SUD-OKU{RED}#{BLUE}------{RESET}")

    for i in range(9):
        if i % 3 == 0 and i != 0:
            print(f"{BLUE}------#-------#------{RESET}")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(f"{BLUE}|{RESET}", end=" ")

            if [i, j] in inflicted_loc and game_board[i][j] != 0:
                print(f"{RED}{game_board[i][j]}{RESET}", end=" ")
            elif i == row and j == col and not game_case:
                print(f"{RED}{UNDERLINE}{num}{RESET}", end=" ")
            else:
                color = YELLOW if original_board[i][j] == 0 else RESET
                print(f"{color}{CONVERT_NUM(game_board[i][j])}{RESET}", end=" ")

        print()

    print(f"{BLUE}------{RED}*{BLUE}-------{RED}*{BLUE}------{RESET}")

    msg_color = BLUE if game_case or game_case is None else RED
    print(f"\n{msg_color}{message}{RESET}\n")
