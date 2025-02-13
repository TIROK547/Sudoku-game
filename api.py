from sudoku import Sudoku
#imports the game array from the api
def generate_sudoku(difficulty):
    sudoku = Sudoku(3).difficulty(difficulty).board
    new_sudoku = []
    for row in sudoku:
        row = [0 if x is None else x for x in row]
        new_sudoku.append(row)
    return new_sudoku