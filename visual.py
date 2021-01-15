import pygame as pg
import time
from screen_size import make_screen_size

def visual_game(board_height, board_width, max_screen_size):
    pg.init()
    screen = pg.display.set_mode(make_screen_size(board_width, board_height, max_screen_size))
    pg.display.set_caption("Snake (trash edition)")
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
