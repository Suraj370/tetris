
import numpy as np

class Ground:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = np.zeros((width, height), dtype=int)

    def can_place(self, tile):
        matrix = tile.get_coordinates()
        for pos in matrix:
            if pos[0] < 0 or pos[0] >= self.width or pos[1] >= self.height or (pos[1] >= 0 and self.matrix[pos[0], pos[1]] != 0):
                return False
        return True

    def place(self, tile):
        matrix = tile.get_coordinates()
        for pos in matrix:
            if 0 <= pos[0] < self.width and 0 <= pos[1] < self.height:
                self.matrix[pos[0], pos[1]] = tile.get_color()

    def clear_full_rows(self):
        full_rows = []
        for y in range(self.height):
            if np.all(self.matrix[:, y] != 0):
                full_rows.append(y)
        
        for row in reversed(full_rows):
            self.matrix[:, 1:row+1] = self.matrix[:, :row]
            self.matrix[:, 0] = 0
        
        return len(full_rows)