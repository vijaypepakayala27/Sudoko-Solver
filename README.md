# Sudoku Solver using Python

This is a simple Python program to solve any 9x9 Sudoku puzzle using the backtracking algorithm. The goal is to fill the puzzle with numbers from 1 to 9, ensuring that each number appears only once in each row, column, and 3x3 sub-grid.

## Features
- **Backtracking Algorithm**: Uses recursion and backtracking to fill the puzzle efficiently.
- **Customizable Input**: Modify the Sudoku board to solve any valid Sudoku puzzle.
- **Step-by-Step Solution**: Automatically finds empty spaces and attempts to solve the puzzle through valid placements.

## How It Works
The algorithm fills each empty cell in the Sudoku board by checking if a number (from 1 to 9) can be placed without violating Sudoku rules. If the current number placement leads to a solution, the program moves on. If not, it backtracks to try other possibilities until the puzzle is solved.

## Example Usage
Here’s an example of an unsolved Sudoku puzzle:

```python
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
