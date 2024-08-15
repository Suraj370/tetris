# board.py

from constants import BOARD_WIDTH, BOARD_HEIGHT, BLACK

class Board:
    def __init__(self):
        self.grid = [[BLACK for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

    def is_collision(self, tetromino):
        for x, y in tetromino.get_positions():
            if x < 0 or x >= BOARD_WIDTH or y >= BOARD_HEIGHT or (y >= 0 and self.grid[y][x] != BLACK):
                return True
        return False

    def add_tetromino(self, tetromino):
        for x, y in tetromino.get_positions():
            if y >= 0:
                self.grid[y][x] = tetromino.color

    def clear_lines(self):
        full_lines = [i for i, row in enumerate(self.grid) if all(cell != BLACK for cell in row)]
        for line in full_lines:
            del self.grid[line]
            self.grid.insert(0, [BLACK for _ in range(BOARD_WIDTH)])
        return len(full_lines)

    def is_game_over(self):
        return any(cell != BLACK for cell in self.grid[0])