# constants.py

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)

# Game dimensions
BLOCK_SIZE = 30
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
GAME_WIDTH = BOARD_WIDTH * BLOCK_SIZE
GAME_HEIGHT = BOARD_HEIGHT * BLOCK_SIZE

# Score display dimensions
SCORE_WIDTH = 200
SCORE_HEIGHT = GAME_HEIGHT

# Screen dimensions
SCREEN_WIDTH = GAME_WIDTH + SCORE_WIDTH
SCREEN_HEIGHT = GAME_HEIGHT

# Game speed
FPS = 60
FALL_SPEED = 0.5  # Blocks per second
FALL_TIME = 1 / FALL_SPEED

# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]]   # Z
]

# Color mapping for shapes
SHAPE_COLORS = [CYAN, YELLOW, PURPLE, ORANGE, BLUE, GREEN, RED]