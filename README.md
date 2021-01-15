# Basic Snake Game
This is a simple python remake of the game snake that I'm sure you know.
It queues input, and accepts variable board sizes.
It is also fully textured.
This repo has 2 versions of the game:

 - A command line game. It can be played through the command line, but pauses every frame to wait for an input.
 - A pygame version which is the "real version" of the game. It is the windowed game that you would expect.

You can choose which version you want to play in the main.py file with this line:

    play_in_cmd = False  # use the command line game? If false, the normal visual game will play.
You also have a few settings that are pretty explicit in the same file:
```
board_height = 9
board_width = 19
    
# max pixels in the inner window of the game. 
# The full window will be 100 pixels wider and 100px higher   
visual_max_size = 800
visual_framerate = 3  # frames per second, which then also is the speed of the snake
```

Have fun playing :)