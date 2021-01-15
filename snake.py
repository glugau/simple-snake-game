class Snake:
    board_width = 0
    board_height = 0
    directions = {
        "up": [0, -1],
        "down": [0, 1],
        "left": [-1, 0],
        "right": [1, 0]
    }

    def __init__(self):
        self.pos = [int(Snake.board_width / 2), int(Snake.board_height / 2)]
        self.direction = "up"
        self.length = 3
        self.bodypos = [
            [self.pos[0], self.pos[1] + 1],
            [self.pos[0], self.pos[1] + 2]
        ]

    def change_direction(self, axis):
        if self.direction == "up" and axis == "down":
            return
        if self.direction == "down" and axis == "up":
            return
        if self.direction == "left" and axis == "right":
            return
        if self.direction == "right" and axis == "left":
            return
        if axis != "up" and axis != "down" and axis != "left" and axis != "right":
            return
        self.direction = axis

    def move(self):
        pos_old = self.pos.copy()
        bodypos_old = self.bodypos.copy()
        self.pos[0] += Snake.directions[self.direction][0]
        self.pos[1] += Snake.directions[self.direction][1]
        for i in range(len(self.bodypos)):
            if i == 0:
                self.bodypos[i] = pos_old
                continue
            self.bodypos[i] = bodypos_old[i - 1]

    def is_colliding(self):
        for p in self.bodypos:
            if p == self.pos:
                return True
        if self.pos[0] < 0 or self.pos[0] >= Snake.board_width:
            return True
        if self.pos[1] < 0 or self.pos[1] >= Snake.board_height:
            return True
        return False

    def eat(self):
        self.bodypos.append(self.bodypos[-1])
