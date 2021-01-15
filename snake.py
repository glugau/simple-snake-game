def opposite_dir(direction):
    if direction == "up":
        return "down"
    elif direction == "down":
        return "up"
    elif direction == "left":
        return "right"
    elif direction == "right":
        return "left"
    return "not valid"


class Snake:
    board_width = 0
    board_height = 0
    max_screen_size = 0
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
        self.direction_history = [
            "up",
            "up"
        ]
        self.fed_body_state = [
            False,
            False
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

        direction_old = self.direction
        directions_copy = self.direction_history.copy()
        for i in range(len(self.direction_history)):
            if i == 0:
                self.direction_history[i] = direction_old
                continue
            self.direction_history[i] = directions_copy[i - 1]

        fed_body_old = self.fed_body_state.copy()
        for i in range(len(self.fed_body_state)):
            if i == 0:
                self.fed_body_state[i] = False
            elif 1 < i:
                self.fed_body_state[i] = fed_body_old[i - 2]

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
        self.direction_history.append(self.direction_history[-1])

        self.bodypos[-1] = [self.bodypos[-1][0] + Snake.directions[opposite_dir(self.direction_history[-1])][0],
                            self.bodypos[-1][1] + Snake.directions[opposite_dir(self.direction_history[-1])][1]]
        self.fed_body_state.append(False)
        self.fed_body_state[0] = True
