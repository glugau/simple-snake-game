import pygame as pg


class Board:
    tiles = [
        pg.image.load("./assets/boardtiles/boardtile2.png"),
        pg.image.load("./assets/boardtiles/boardtile1.png")
    ]
    board_height = 0
    board_width = 0

    def __init__(self, board_width, board_height, screen_size):
        self.board_size = (screen_size[0] - 100, screen_size[1] - 100)
        self.cell_size = int(self.board_size[0] / board_width)
        Board.tiles = [
            pg.transform.scale(Board.tiles[0], (int(self.cell_size), int(self.cell_size))),
            pg.transform.scale(Board.tiles[1], (int(self.cell_size), int(self.cell_size)))
        ]
        self.tiles_position = []
        Board.board_height = board_height
        Board.board_width = board_width
        currenty = 0
        for i in range(board_height):
            currentx = 0
            hor = []
            for le in range(board_width):
                hor.append((currentx, currenty))
                currentx += self.cell_size
            self.tiles_position.append(hor)
            currenty += self.cell_size

    def draw(self, screen):
        firstim = True
        for i in self.tiles_position:
            for el in i:
                if firstim:
                    screen.blit(Board.tiles[0], (int(el[0] + 50), int(el[1] + 50)))
                else:
                    screen.blit(Board.tiles[1], (int(el[0] + 50), int(el[1] + 50)))
                firstim = not firstim

    def draw_element(self, image, pos, screen):
        if 0 <= pos[0] < Board.board_width and 0 <= pos[1] < Board.board_height:
            im = pg.transform.scale(image, (self.cell_size, self.cell_size))
            screen.blit(im, (pos[0] * self.cell_size + 50, pos[1] * self.cell_size + 50))
