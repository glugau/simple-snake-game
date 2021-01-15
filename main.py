from snake import Snake
from commandline import cmd_game
from visual.visual import visual_game

# SETTINGS
board_height = 19  # Minimum is 5
board_width = 19  # both sizes need to be odd, and if they aren't, they'll be set to be so
# (your board won't render properly otherwise, and I'm too lazy to fix it. It's better with an odd board anyways).

play_in_cmd = False  # use the command line game? If false, the normal visual game will play.

# max pixels in the inner window of the game.
# The full window will be 100 pixels wider and 100px higher
visual_max_size = 800
visual_framerate = 7  # frames per second, which then also is the speed of the snake

if board_width % 2 == 0:
    board_width += 1
if board_height % 2 == 0:
    board_height += 1
# assign settings to class
Snake.board_width = board_width
Snake.board_height = board_height
Snake.max_screen_size = visual_max_size

if play_in_cmd:
    cmd_game(board_height, board_width)
else:
    visual_game(board_height, board_width, visual_max_size, visual_framerate)
