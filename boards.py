import random
import json
with open("./datas/data.json", 'r') as file:
    boards = json.load(file)
def random_board(difficulty):
    return random.choice(boards[difficulty])