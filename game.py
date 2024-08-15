# game.py

import pygame
from constants import *
from board import Board
from tetromino import Tetromino

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.current_tetromino = Tetromino()
        self.next_tetromino = Tetromino()
        self.fall_time = 0
        self.score = 0
        self.font = pygame.font.Font(None, 36)

    def draw(self):
        self.screen.fill(BLACK)
        
        # Draw the game board
        for y, row in enumerate(self.board.grid):
            for x, color in enumerate(row):
                pygame.draw.rect(self.screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)

        # Draw the current tetromino
        for x, y in self.current_tetromino.get_positions():
            if y >= 0:
                pygame.draw.rect(self.screen, self.current_tetromino.color,
                                 (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)

        # Draw the score display area
        pygame.draw.rect(self.screen, WHITE, (GAME_WIDTH, 0, SCORE_WIDTH, SCORE_HEIGHT), 2)
        
        # Draw the score
        score_text = self.font.render(f"Score:", True, WHITE)
        score_value = self.font.render(f"{self.score}", True, WHITE)
        self.screen.blit(score_text, (GAME_WIDTH + 20, 20))
        self.screen.blit(score_value, (GAME_WIDTH + 20, 60))

        # Draw the next tetromino preview
        next_text = self.font.render("Next:", True, WHITE)
        self.screen.blit(next_text, (GAME_WIDTH + 20, 120))
        for y, row in enumerate(self.next_tetromino.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, self.next_tetromino.color,
                                     (GAME_WIDTH + 20 + x * BLOCK_SIZE, 160 + y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)

        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move_tetromino(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    self.move_tetromino(1, 0)
                elif event.key == pygame.K_DOWN:
                    self.move_tetromino(0, 1)
                elif event.key == pygame.K_UP:
                    self.rotate_tetromino()
                elif event.key == pygame.K_SPACE:
                    self.hard_drop()
        return True

    def move_tetromino(self, dx, dy):
        self.current_tetromino.move(dx, dy)
        if self.board.is_collision(self.current_tetromino):
            self.current_tetromino.move(-dx, -dy)

    def rotate_tetromino(self):
        original_shape = self.current_tetromino.shape
        self.current_tetromino.rotate()
        if self.board.is_collision(self.current_tetromino):
            self.current_tetromino.shape = original_shape

    def hard_drop(self):
        while not self.board.is_collision(self.current_tetromino):
            self.current_tetromino.move(0, 1)
        self.current_tetromino.move(0, -1)
        self.lock_tetromino()

    def lock_tetromino(self):
        self.board.add_tetromino(self.current_tetromino)
        lines_cleared = self.board.clear_lines()
        self.score += lines_cleared * 100
        self.current_tetromino = self.next_tetromino
        self.next_tetromino = Tetromino()
        if self.board.is_game_over():
            return False
        return True

    def update(self):
        self.fall_time += self.clock.get_rawtime()
        if self.fall_time >= FALL_TIME * 1000:
            self.move_tetromino(0, 1)
            if self.board.is_collision(self.current_tetromino):
                self.current_tetromino.move(0, -1)
                if not self.lock_tetromino():
                    return False
            self.fall_time = 0
        return True

    def run(self):
        running = True
        while running:
            self.clock.tick(FPS)
            running = self.handle_events() and self.update()
            self.draw()
        pygame.quit()