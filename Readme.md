# Python Tetris Game

This is a simple implementation of the classic Tetris game using Python and Pygame. The game features a clean, object-oriented design with the game board on the left side and the score display on the right side.

## Screenshots

[Add a screenshot of the game in action here]

[Add a screenshot of the game over screen here]

## Features

- Classic Tetris gameplay
- Score tracking
- Next piece preview
- Increasing difficulty as the game progresses

## Requirements

- Python 3.x
- Pygame

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/python-tetris.git
   ```

2. Navigate to the project directory:
   ```
   cd python-tetris
   ```

3. Install the required dependencies:
   ```
   pip install pygame
   ```

## How to Play

Run the game by executing the `main.py` file:

```
python main.py
```

### Controls

- Left Arrow: Move the tetromino left
- Right Arrow: Move the tetromino right
- Down Arrow: Soft drop (move the tetromino down faster)
- Up Arrow: Rotate the tetromino clockwise
- Spacebar: Hard drop (instantly drop the tetromino to the bottom)

## Game Rules

1. Tetrominos (shapes composed of four blocks) fall from the top of the screen.
2. Use the controls to move and rotate the tetrominos.
3. Fill horizontal lines with blocks to clear them and score points.
4. The game ends when the blocks stack up to the top of the screen.

## Scoring

- 1 line cleared: 100 points
- 2 lines cleared: 200 points
- 3 lines cleared: 300 points
- 4 lines cleared: 400 points

## Project Structure

- `main.py`: The entry point of the game
- `game.py`: Contains the main game logic
- `board.py`: Represents the Tetris board
- `tetromino.py`: Defines the Tetromino shapes and their behavior
- `constants.py`: Stores game constants

## Contributing

Feel free to fork this project and submit pull requests with improvements or bug fixes. You can also open issues for any bugs you find or features you'd like to suggest.

## License

This project is open source and available under the [MIT License](LICENSE).

