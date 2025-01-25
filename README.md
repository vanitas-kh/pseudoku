# Pseudoku - Sudoku Solver

**Pseudoku** is a simple Sudoku solver application built using Python and Tkinter. It uses a backtracking algorithm to solve Sudoku puzzles and provides a user-friendly graphical interface for inputting and solving puzzles.

---

## Features

- **Sudoku Solver**: Solves any valid 9x9 Sudoku puzzle using a backtracking algorithm.
- **Graphical Interface**: Provides a 9x9 grid for inputting Sudoku puzzles.
- **Input Validation**: Ensures that the input puzzle is valid before attempting to solve it.
- **Clear Functionality**: Allows users to clear the grid and start over.
- **About Section**: Provides information about the application, including version, license, and contact details.

---

## Screenshots

![image](https://github.com/user-attachments/assets/a0e26d1a-e9a5-4e8a-9883-1cd3e4d990ab)
![image](https://github.com/user-attachments/assets/581096a6-63f0-4661-b287-4aafc6b2db7e)

---

## Installation

### Prerequisites
- **Python 3.x**: Ensure Python is installed. You can check by running `python3 --version` or `python --version` in your terminal.
- **Tkinter**: Tkinter is typically included with Python, but if not:
  - macOS: Install Python via [Python.org](https://www.python.org/downloads/) or Homebrew (`brew install python-tk`).
  - Linux: Install Tkinter using your package manager:
    
    ```
    sudo apt-get install python3-tk   # For Debian/Ubuntu
    sudo pacman -S tk                 # For Arch-based distributions
    sudo yum install python3-tkinter  # For RHEL/CentOS
    ```

### Steps

#### **For macOS/Linux**
1. **Clone the Repository**:
   Open your terminal and clone the repository:
    ```
    git clone https://github.com/vanitas-kh/pseudoku.git
   
    cd pseudoku
    ```
   
2. **Run the Application**:
    Execute the application using Python:
   
    ```python3 pseudoku.py```

   
#### **For Windows**
1. Follow the same steps above but replace `python3` with `python` (or `py`) depending on your configuration.

---

### Building the Executable for macOS/Linux
You can also create a standalone executable for macOS or Linux using PyInstaller:

#### **macOS**
1. Install PyInstaller:
   
   ```pip install pyinstaller```
   
2. Build the executable:
   
   ```pyinstaller --onefile --windowed --icon=pseudoku.ico --add-data "pseudoku.ico:." pseudoku.py```

    - **Note**: On macOS/Linux, use `:` as the separator in `--add-data` instead of `;`.

3. The executable will be created in the **dist/** directory.

#### **Linux**
1. Install PyInstaller:
   
   ```pip install pyinstaller```

2. Build the executable:

   ```pyinstaller --onefile --windowed --icon=pseudoku.ico --add-data "pseudoku.ico:." pseudoku.py```
  
3. Locate the executable in the **dist/** directory.

#### **Windows**
1. Install PyInstaller:
   
   ```pip install pyinstaller```
   
2. Build the executable:
   
   ```pyinstaller --onefile --windowed --icon=pseudoku.ico --add-data "pseudoku.ico;." pseudoku.py```

3. The executable will be located in the **dist/** directory.

---

### Running the Standalone Executable
- **macOS/Linux**: Ensure the file is executable:

  ```chmod +x ./dist/pseudoku ./dist/pseudoku```
  - **macOS Security**: On macOS, you may need to bypass security restrictions for unsigned apps:
  - Go to **System Preferences > Security & Privacy > General**.
  - Allow the app under "Allow apps downloaded from".

---

### Steps

1. **Clone the Repository**:
   
    ```
    git clone https://github.com/vanitas-kh/pseudoku.git
   
    cd pseudoku
    ```

3. **Run the Application**:
   
   ```python pseudoku.py```

---

### Usage
1. **Input the Puzzle**:
    - Enter the numbers of the Sudoku puzzle into the board. Use ```0``` or leave cells blank for empty cells.

2. **Solve the Puzzle**:
    - Click the **Solve** button to solve the puzzle. The solved puzzle will be displayed in the board.

3. **Clear the Board**:
    - Click the **Clear** button to reset the board and start over.

4. **About**:
    - Click the **About** button to view information about the application.

---

### License
This project is licensed under the **MIT License**.

---

### Acknowledgements
- Thanks to the open-source community for their contributions.
- Built with Python and Tkinter.

---

### Contact
For more information, visit the project repository: 
https://github.com/vanitas-kh/pseudoku
