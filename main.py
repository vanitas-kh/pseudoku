# User input for a 9x9 Sudoku board with 0s representing empty cells
print("Enter the Sudoku board (0 for empty cells)\n\n")


def user_input():
    """
    Collect a 9x9 Sudoku board from user input, where 0s represent empty cells.

    This function prompts the user to input each row of a Sudoku board one at a time.
    Each row must consist of 9 numbers, separated by spaces. The input is validated
    to ensure that each row contains exactly 9 numbers and that all inputs are integers.
    If the input is invalid, the user is prompted to re-enter the row.

    Returns
    -------
    list of list of int
        A 9x9 2D list representing the Sudoku board, with 0s indicating empty cells.
    """

    # Initialize an empty 9x9 board
    board = [[0 for _ in range(9)] for _ in range(9)]

    for i in range(9):
        while True:
            try:
                # Prompt the user to enter a row
                row_input = input(
                    f"Enter row {i + 1} (9 numbers, separated by spaces): ")
                # Split the input into a list of strings
                row_values = row_input.split()
                # Check if exactly 9 numbers were entered
                if len(row_values) != 9:
                    print("Please enter exactly 9 numbers.")
                    continue
                valid = True
                # Convert the strings to integers and store them in the board
                for j in range(9):
                    num = int(row_values[j])
                    if num < 0 or num > 9:
                        print("Please enter numbers between 0 and 9.")
                        valid = False
                        break
                    board[i][j] = num
                if not valid:
                    continue
                # Exit the loop if the row is successfully entered
                break
            except ValueError:
                print("Invalid input. Please enter numbers only.")
    return board


# Check if the number is valid
def is_valid(board, row, col, num):
    """Check if a number is valid in a given position on a Sudoku board.

    A number is valid if it does not already exist in the same row, column, or 3x3 box.

    Parameters
    ----------
    board : 2D array
        The Sudoku board, represented as a 2D array.
    row : int
        The row of the position to check.
    col : int
        The column of the position to check.
    num : int
        The number to check.

    Returns
    -------
    bool
        True if the number is valid, False otherwise.
    """

    # Check row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True


def is_board_initially_valid(board):
    """
    Check if a Sudoku board is initially valid.

    A board is initially valid if all numbers initially present on the board are
    valid according to Sudoku rules. 

    Parameters
    ----------
    board : 2D array
        The Sudoku board, represented as a 2D array.

    Returns
    -------
    bool
        True if the board is initially valid, False otherwise.
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                num = board[i][j]
                board[i][j] = 0
                if not is_valid(board, i, j, num):
                    board[i][j] = num
                    return False
                board[i][j] = num
    return True

# Backtracking algorithm to solve Sudoku


def pseudo_solver(board):
    """
    Solve a Sudoku puzzle using a backtracking algorithm.

    The function attempts to fill the empty cells (represented by 0s) in the given
    Sudoku board with numbers from 1 to 9, ensuring that each number is valid
    according to Sudoku rules. It uses a recursive approach to try all possible
    numbers for each empty cell, backtracking if no valid number can be placed.

    Parameters
    ----------
    board : 2D array
        The Sudoku board, represented as a 2D array, where empty cells are marked with 0.

    Returns
    -------
    bool
        True if the Sudoku puzzle is solved successfully, False otherwise.
    """

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:  # Find an empty cell
                for num in range(1, 10):  # Try numbers 1-9
                    if is_valid(board, i, j, num):  # Check if the number is valid
                        board[i][j] = num  # Place the number
                        if pseudo_solver(board):  # Recurse to solve the rest
                            return True  # If solved, return True
                        board[i][j] = 0  # Backtrack if no solution is found
                return False  # Trigger backtracking if no number works
    return True  # Return True if the board is fully solved


# Main program
board = user_input()

# Validate the initial board
if not is_board_initially_valid(board):
    print("The given board is not initially valid.")
else:
    # Solve the board
    if pseudo_solver(board):
        print("Solution found:")
        for row in board:
            print(row)
    else:
        print("No solution exists for the given board.")
