import tkinter as tk
from tkinter import messagebox

# Sudoku solving logic using backtracking
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve_board(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_board(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# GUI functionality
class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()

        solve_button = tk.Button(root, text="Solve", command=self.solve)
        solve_button.grid(row=9, column=3, columnspan=3, pady=10)

    def create_grid(self):
        for row in range(9):
            for col in range(9):
                entry = tk.Entry(self.root, width=3, font=("Arial", 18), justify="center", bd=1)
                entry.grid(row=row, column=col, padx=2, pady=2)
                self.entries[row][col] = entry

    def get_board(self):
        board = []
        for row in range(9):
            row_data = []
            for col in range(9):
                val = self.entries[row][col].get()
                row_data.append(int(val) if val.isdigit() else 0)
            board.append(row_data)
        return board

    def fill_board(self, board):
        for row in range(9):
            for col in range(9):
                self.entries[row][col].delete(0, tk.END)
                self.entries[row][col].insert(0, str(board[row][col]))

    def solve(self):
        board = self.get_board()
        if solve_board(board):
            self.fill_board(board)
            messagebox.showinfo("Success", "Sudoku Solved!")
        else:
            messagebox.showerror("Error", "No solution exists!")

# Run the GUI app
if __name__ == "__main__":
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()
