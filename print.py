from pprint import pprint

#color_codes
#YELLOW = '\033[33m'
#RED = '\033[31m'
#WHITE = '\033[37m'
#RESET = '\033[0m'


user_choice = [0, 0, None]

def print_game(game_board,game_case,message,user_choice):
      row , col, num = user_choice
      game_board[row][col] = num


      for i in range(9) :
           if i % 3 == 0 and i != 0:
              print("_" * 21) 

           for j in range(9):
               if j % 3 == 0 and j != 0 :
                  print("|", end = "")
      
               if (i, j) == (row, col):
                  if game_case is None:   
                        print('\033[0m'+ '\033[33m'+ str(num) +'\033[0m' + " ", end="")
                  elif game_case is False:  
                        print('\033[0m' + '\033[31m' + str(num) + '\033[0m'+" ", end="")
               else:  
                    print(game_board[i][j] if game_board[i][j] != 0 else ".", end=" ")    
           print()
           
