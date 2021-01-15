# play the game through the command line.
# call the function in the main file!
from snake import Snake
from food import Food, spawn_food
import random


def print_2d_list(inlist):
    for i in inlist:
        line = ""
        for li in i:
            line += li
        print(line)

def cmd_game(board_height, board_width):
    chars = {
        "empty": "◻️",
        "snake": "⬛",
        "snakehead": "🔲",
        "food": "#"
    }
    done = False
    snake = Snake()

    def spawn_f():
        return spawn_food(board_height, board_width, snake)

    food = spawn_f()
    while not done:
        snake.move()
        board = []
        if food.is_eaten(snake):
            food = spawn_f()
            snake.eat()
        for i in range(board_height):
            line = []
            for le in range(board_width):
                line.append(chars["empty"])
            board.append(line)
        if 0 <= snake.pos[1] < board_height and 0 <= snake.pos[0] < board_width:
            board[snake.pos[1]][snake.pos[0]] = chars["snakehead"]
        for i in snake.bodypos:
            board[i[1]][i[0]] = chars["snake"]
        board[food.pos[1]][food.pos[0]] = chars["food"]
        print_2d_list(board)
        print("\n")
        if snake.is_colliding():
            print("Snake died!")
            break
        if board_width * board_height == len(snake.bodypos) + 1:
            print("You won!")
            break
        in_move = input("Which direction should the snake go? (up, down, left, right, or nothing to continue): ")
        snake.change_direction(in_move)
