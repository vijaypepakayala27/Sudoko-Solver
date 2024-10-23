# Define the Sudoku board (0 represents an empty cell)
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

# Function to print the Sudoku board
def print_board(b):
    for row in b:
        print(" ".join(str(cell) for cell in row))

# Function to check if a number can be placed in a position
def is_valid(b, num, pos):
    # Check row
    for i in range(9):
        if b[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(9):
        if b[i][pos[1]] == num and pos[0] != i:
            return False

    # Check 3x3 sub-grid
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if b[i][j] == num and (i, j) != pos:
                return False

    return True

# Function to find empty space (0)
def find_empty(b):
    for i in range(9):
        for j in range(9):
            if b[i][j] == 0:
                return (i, j)  # row, col
    return None

# Backtracking function to solve the board
def solve(b):
    find = find_empty(b)
    if not find:
        return True  # Solved
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(b, i, (row, col)):
            b[row][col] = i

            if solve(b):
                return True

            b[row][col] = 0  # Backtrack

    return False

# Print initial board
print("Initial Sudoku Board:")
print_board(board)
solve(board)
print("\nSolved Sudoku Board:")
print_board(board)
