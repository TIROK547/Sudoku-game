from pprint import pprint

mode_1= [ 
      [5, 3, 0, 0, 7, 0, 0, 0, 0],
      [6, 0, 0, 1, 9, 5, 0, 0, 0],
      [0, 9, 8, 0, 0, 0, 0, 6, 0],
      [8, 0, 0, 0, 6, 0, 0, 0, 3],
      [4, 0, 0, 8, 0, 3, 0, 0, 1],
      [7, 0, 0, 0, 2, 0, 0, 0, 6],
      [0, 6, 0, 0, 0, 0, 2, 8, 0],
      [0, 0, 0, 4, 1, 9, 0, 0, 5],
      [0, 0, 0, 0, 8, 0, 0, 7, 9] ]
#color_codes
#YELLOW = '\033[33m'
#RED = '\033[31m'
#WHITE = '\033[37m'
#RESET = '\033[0m'


user_choice = [0, 0, None]
#[],[1,3,6],None
#function:
def print_game(game_board,game_case,message,user_choice):
      for i in range(9) :
           if i % 3 == 0 and i != 0:
                  print("_" * 21) 
           for j in range(9):
               if j % 3 == 0 and j != 0 :
                  print("|", end = "")
               if game_board[i][j] != 0:
                        print(game_board[i][j], end =" ")
                
               else:
                        print(".", end = " ")     
           print() 

           if game_case == True:
                 user_choice[i][j] == num
                 print('\033[0m', '\033[33m', num, '\033[0m')
           elif game_case == False:
                user_choice[i][j] == num
                print('\033[0m', '\033[31m', num, '\033[0m')                  
print_game(mode_1,None,"congrats",[0,2,1])
