from check import check_game
#check input data: check_game(game_arr, [row, col, num])
#check output data: return [new_game_arr, game_winner, game_message, user_choices]
difficulty = int(input("Choose difficulty: easy(1), medium(2), hard(3): "))
user_choices = list(map(int,input("Enter your choice: ").split()))
