from snake import Snake
from commandline import cmd_game
from visual.visual import visual_game

# SETTINGS
board_height = 13  # Minimum is 5
board_width = 19
play_in_cmd = False  # use the command line game? If false, the normal visual game will play.

# max pixels in the inner window of the game.
# The full window will be 100 pixels wider and 100px higher
visual_max_size = 800
visual_framerate = 5  # frames per second, which then also is the speed of the snake

# assign settings to class
Snake.board_width = board_width
Snake.board_height = board_height

if play_in_cmd:
    cmd_game(board_height, board_width)
else:
    visual_game(board_height, board_width, visual_max_size, visual_framerate)
