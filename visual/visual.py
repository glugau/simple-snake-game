import pygame as pg
import time
from visual.screen_size import make_screen_size
from visual.board import Board
from food import Food, spawn_food
from snake import Snake

food_img = pg.image.load("./assets/heart.png")
snake_head = pg.image.load("./assets/head.png")
snake_body = pg.image.load("./assets/body.png")
snake_tail = pg.image.load("./assets/tail.png")
snake_angle_left = pg.image.load("./assets/angle_left.png")
snake_angle_right = pg.image.load("./assets/angle_right.png")

class TooSmallBoard(Exception):
    pass

def rotated_body_piece(bodypiece, direction):
    if direction == "up":
        out = pg.transform.rotate(bodypiece, 0)
    elif direction == "down":
        out = pg.transform.rotate(bodypiece, 180)
    elif direction == "left":
        out = pg.transform.rotate(bodypiece, 90)
    else:
        out = pg.transform.rotate(bodypiece, -90)
    return out

def find_turn(newdir, olddir):
    if (olddir == "up" and newdir == "left") or (olddir == "left" and newdir == "down") or (olddir == "down" and newdir == "right") or (olddir == "right" and newdir == "up"):
        return "left"
    elif (olddir == "up" and newdir == "right") or (olddir == "left" and newdir == "up") or (olddir == "down" and newdir == "left") or (olddir == "right" and newdir == "down"):
        return "right"
    return "straight"

def visual_game(board_height, board_width, max_screen_size, fps):
    clock = pg.time.Clock()
    if board_height < 5:
        raise TooSmallBoard("The height of the board should be at least 5")
    pg.init()
    screen_size = make_screen_size(board_width, board_height, max_screen_size)
    screen = pg.display.set_mode(screen_size)
    pg.display.set_caption("Snake (trash edition)")
    done = False
    board = Board(board_width, board_height, screen_size)
    snake = Snake()
    food = spawn_food(board_height, board_width, snake)
    queued_inputs = []
    while not done:
        if len(queued_inputs) != 0:
            snake.change_direction(queued_inputs[0])
            queued_inputs = queued_inputs[1:]
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN:
                # queue one additional input
                if event.key == pg.K_UP:
                    queued_inputs.append("up")
                if event.key == pg.K_DOWN:
                    queued_inputs.append("down")
                if event.key == pg.K_RIGHT:
                    queued_inputs.append("right")
                if event.key == pg.K_LEFT:
                    queued_inputs.append("left")
        rotated_snake_head = rotated_body_piece(snake_head, snake.direction)
        snake.move()

        if food.is_eaten(snake):
            food = spawn_food(board_height, board_width, snake)
            snake.eat()

        screen.fill((0, 255, 255))
        board.draw(screen)
        board.draw_element(food_img, food.pos, screen)
        board.draw_element(rotated_snake_head, snake.pos, screen)
        for i in range(len(snake.bodypos)):
            if i == len(snake.bodypos) - 1:
                board.draw_element(rotated_body_piece(snake_tail, snake.direction_history[i]), snake.bodypos[i], screen)
            elif snake.direction_history[i] == snake.direction_history[i + 1]:
                board.draw_element(rotated_body_piece(snake_body, snake.direction_history[i]), snake.bodypos[i], screen)
            else:
                if find_turn(snake.direction_history[i], snake.direction_history[i + 1]) == "left":
                    board.draw_element(rotated_body_piece(snake_angle_left, snake.direction_history[i]), snake.bodypos[i], screen)
                elif find_turn(snake.direction_history[i], snake.direction_history[i + 1]) == "right":
                    board.draw_element(rotated_body_piece(snake_angle_right, snake.direction_history[i]), snake.bodypos[i], screen)
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                # queue one additional input
                if event.key == pg.K_UP:
                    queued_inputs.append("up")
                if event.key == pg.K_DOWN:
                    queued_inputs.append("down")
                if event.key == pg.K_RIGHT:
                    queued_inputs.append("right")
                if event.key == pg.K_LEFT:
                    queued_inputs.append("left")
        clock.tick(fps)
