import random

import numpy as np
import pygame

import shape
from tile import Tile

from ground import Ground


class Board:
    def __init__(self, screen, height=24, width=10):
        self._height = height
        self._width = width
        self._screen = screen
        self._ground = Ground(width, height)
        self._current_tile = None
        self.score = 0
        self._colours = shape.generate_colours()
        self._shapes = shape.generate_shapes()

    def draw(self):
        block_size = 35
        x_offset = 100
        y_offset = 50
        for x in range(self._width):
            for y in range(self._height):
                rect = pygame.Rect(x_offset + x * block_size, y_offset + y * block_size, block_size, block_size)
                color = self._colours[self._ground.matrix[x, y]]
                pygame.draw.rect(self._screen, color, rect, 1 if self._ground.matrix[x, y] == 0 else 0)
        
        if self._current_tile:
            self.draw_tile(self._current_tile)

    def update(self, on_timer=True):
        if self._current_tile is None:
            self.create_tile()
        elif on_timer:
            next_pos = self._current_tile._position + np.array([0, 1])
            next_tile = Tile(self._current_tile._shape, self._current_tile._color, next_pos[0], next_pos[1], self._current_tile._rotation)
            if self._ground.can_place(next_tile):
                self._current_tile.move(0, 1)
            else:
                self._ground.place(self._current_tile)
                cleared_rows = self._ground.clear_full_rows()
                self.score += cleared_rows * 100
                self._current_tile = None

    def create_tile(self):
        self._current_tile = Tile(self.get_shape(), self.get_colour(), random.randint(0, self._width - 1))
    
    def get_shape(self):
        return self._shapes[random.randint(0, len(self._shapes) - 1)]

    def get_colour(self):
        return random.randint(1, len(self._colours) - 1)

    def draw_tile(self, tile):
        matrix = tile.get_coordinates()
        block_size = 35
        x_offset = 100
        y_offset = 50
        for pos in matrix:
            if 0 <= pos[0] < self._width and 0 <= pos[1] < self._height:
                rect = pygame.Rect(x_offset + pos[0] * block_size, y_offset + pos[1] * block_size, block_size, block_size)
                pygame.draw.rect(self._screen, self._colours[tile.get_color()], rect, 0)

    def on_key_up(self):
        rotated_tile = Tile(self._current_tile._shape, self._current_tile._color, 
                            self._current_tile._position[0], self._current_tile._position[1], 
                            (self._current_tile._rotation + 1) % self._current_tile._shape.rotations_count)
        if self._ground.can_place(rotated_tile):
            self._current_tile.rotate(1)

    def on_key_down(self):
        next_tile = Tile(self._current_tile._shape, self._current_tile._color, 
                         self._current_tile._position[0], self._current_tile._position[1] + 1, 
                         self._current_tile._rotation)
        if self._ground.can_place(next_tile):
            self._current_tile.move(0, 1)

    def on_key_left(self):
        next_tile = Tile(self._current_tile._shape, self._current_tile._color, 
                         self._current_tile._position[0] - 1, self._current_tile._position[1], 
                         self._current_tile._rotation)
        if self._ground.can_place(next_tile):
            self._current_tile.move(-1, 0)

    def on_key_right(self):
        next_tile = Tile(self._current_tile._shape, self._current_tile._color, 
                         self._current_tile._position[0] + 1, self._current_tile._position[1], 
                         self._current_tile._rotation)
        if self._ground.can_place(next_tile):
            self._current_tile.move(1, 0)