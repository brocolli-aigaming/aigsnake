from random import choice, shuffle

botName = 'abkeble-1'

dirs = {"N": [0,-1], "E": [1,0], "S": [0,1], "W": [-1,0]}

def calculate_move(gamestate):
    all_moves = ["N", "E", "S", "W"]
    board = gamestate["Board"]
    my_snake = gamestate["MySnake"]
    opp_snake = gamestate["OppSnake"]
    food = gamestate["Food Coordinates"]
    
    moves = avoid_walls(all_moves, board, my_snake)
    moves = avoid_snakes(moves, board, my_snake, opp_snake, food)
    moves = avoid_potential_snakes(moves, my_snake, opp_snake)
    moves = rank_moves(moves, my_snake, food)
    if moves != []:
        move = moves[0]
    else:
        move = choice(all_moves)
    
    print(move)
    return {"Direction": move}


def avoid_walls(directions, board, snake):
    return directions
    
def avoid_snakes(directions, board, snake, opp_snake, food):
    return directions
    
def avoid_potential_snakes(directions, snake, opp_snake):
    return directions
    
def rank_moves(directions, snake, food):
    return directions
    
def distance_from_coordinate(snake, coord):
    def func(x=None):
        if x is None:
            return abs(snake[0][0] - coord[0]) + abs(snake[0][1] - coord[1])
        else:
            return abs(snake[0][0] + dirs[x][0] - coord[0]) + abs(snake[0][1] + dirs[x][1] - coord[1])
    return func



