import tkinter as tk
from tkinter import messagebox


def is_valid(board, row, col, num):
    """
    Check if a number is valid in a given position on a Sudoku board.
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


def pseudo_solver(board):
    """
    Solve a Sudoku puzzle using a backtracking algorithm.
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


def is_board_initially_valid(board):
    """
    Check if the initial Sudoku board is valid.
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                num = board[i][j]
                board[i][j] = 0  # Temporarily set the cell to 0
                if not is_valid(board, i, j, num):  # Check if the number is valid
                    board[i][j] = num
                    return False
                board[i][j] = num  # Restore the original value
    return True


def user_input_gui():
    """
    Retrieve the Sudoku board from the GUI, validate it, and solve it.
    """
    # Initialize an empty 9x9 board
    board = [[0 for _ in range(9)] for _ in range(9)]

    # Retrieve values from the entry widgets
    for i in range(9):
        for j in range(9):
            # Get the value from the entry widget
            value = entry_grid[i][j].get()
            if value == "":
                board[i][j] = 0  # Treat empty cells as 0
            else:
                try:
                    num = int(value)  # Convert the input to an integer
                    if num < 0 or num > 9:
                        raise ValueError  # Raise an error if the number is out of range
                    board[i][j] = num
                except ValueError:
                    # Show an error message if the input is invalid
                    messagebox.showerror("Invalid Input", f"Invalid input for cell ({
                                         i+1}, {j+1}). Please enter a number between 0 and 9.")
                    return None  # Exit the function if there's an error

    # Validate the initial board
    if not is_board_initially_valid(board):
        messagebox.showerror(
            "Invalid Board", "The given board is not initially valid (Duplicate numbers in the same row, column, or 3x3 box).")
        return None  # Exit the function if the board is invalid

    # Solve the board
    if pseudo_solver(board):
        # Update the GUI with the solved board
        for i in range(9):
            for j in range(9):
                entry_grid[i][j].delete(0, tk.END)  # Clear the entry widget
                # Insert the solved value
                entry_grid[i][j].insert(0, str(board[i][j]))
        messagebox.showinfo(
            "Solution Found", "The board has been solved successfully.")
    else:
        messagebox.showerror(
            "No Solution", "No solution exists for the given board.")


# Create the main window
root = tk.Tk()
root.title("Pseudoku Solver")


def clear_grid():
    for row in entry_grid:
        for entry in row:
            entry.delete(0, tk.END)
    messagebox.showinfo("Board Cleared", "The board has been cleared.")


# Configure the grid to make it resizable
for i in range(9):
    root.rowconfigure(i, weight=1)  # Make rows expand proportionally
    root.columnconfigure(i, weight=1)  # Make columns expand proportionally

# Create a 9x9 grid of entry widgets with alternating colors for 3x3 subgrids
entry_grid = []
for i in range(9):
    row = []
    for j in range(9):
        # Determine the background color based on the 3x3 subgrid
        if (i // 3 + j // 3) % 2 == 0:
            bg_color = "#A6A6A6"  # Gray for even subgrids
        else:
            bg_color = "#FFFFFF"  # White for odd subgrids

        entry = tk.Entry(root, width=3, font=("Arial", 16),
                         justify="center", bg=bg_color)
        entry.grid(row=i, column=j, padx=2, pady=2, sticky="nsew")
        row.append(entry)
    entry_grid.append(row)

# Create a "Solve" button
solve_button = tk.Button(
    root, text="Solve", command=user_input_gui, font=("Arial", 16))
solve_button.grid(row=9, column=2, columnspan=2, pady=10, sticky="ns")

# Create a "Clear" button
clear_button = tk.Button(
    root, text="Clear", command=clear_grid, font=("Arial", 16))
clear_button.grid(row=9, column=5, columnspan=2, pady=10, sticky="ns")

# Run the Tkinter event loop
root.mainloop()
