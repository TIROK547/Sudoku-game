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
def check_game(arr,user_choice):
        my_game = arr
        row = user_choice[1]
        col = user_choice[0]
        if arr[row][col] == 0:
            if user_choice[2] in arr[row]:
                return [False,"This is not a valid choice"]
            elif user_choice[2] in [arr[i][col] for i in range(9)]:
                return [False,"This is not a valid choice"]
            else:
                my_game[row][col] = user_choice[2]
                return my_game
        elif arr[row][col] != 0:
            return [False,"This is not a valid choice"]
pprint(check_game(game,[1-1,9-1,1]))