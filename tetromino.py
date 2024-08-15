# tetromino.py

import random
from constants import SHAPES, SHAPE_COLORS, BOARD_WIDTH

class Tetromino:
    def __init__(self):
        self.shape_index = random.randint(0, len(SHAPES) - 1)
        self.shape = SHAPES[self.shape_index]
        self.color = SHAPE_COLORS[self.shape_index]
        self.x = BOARD_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = list(zip(*self.shape[::-1]))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def get_positions(self):
        positions = []
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell:
                    positions.append((self.x + j, self.y + i))
        return positions