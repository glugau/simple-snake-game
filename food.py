import random

class Food:
    def __init__(self, pos):
        self.pos = pos

    def is_eaten(self, snake):
        if snake.pos == self.pos:
            return True
        return False


def spawn_food(board_height, board_width, snake):
    while True:
        p = [random.randrange(board_width), random.randrange(board_height)]
        if snake.pos == p:
            continue
        isbroken = False
        for i in snake.bodypos:
            if i == p:
                isbroken = True
                break
        if isbroken:
            continue
        break
    fo = Food(p)
    return fo