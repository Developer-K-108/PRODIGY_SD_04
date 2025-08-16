import tkinter as tk
from tkinter import messagebox

# Backtracking Sudoku Solver
def is_valid(board, row, col, num):
    # Check row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check 3x3 box
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# GUI Part
def solve():
    board = []
    try:
        for i in range(9):
            row = []
            for j in range(9):
                val = entries[i][j].get()
                row.append(int(val) if val else 0)
            board.append(row)

        if solve_sudoku(board):
            for i in range(9):
                for j in range(9):
                    entries[i][j].delete(0, tk.END)
                    entries[i][j].insert(0, str(board[i][j]))
            messagebox.showinfo("Success", "Sudoku Solved Successfully!")
        else:
            messagebox.showwarning("Failure", "No solution exists for this Sudoku!")
    except ValueError:
        messagebox.showerror("Error", "Please enter only numbers 1-9 or leave blank.")

def clear():
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)

# Main Window
root = tk.Tk()
root.title("Sudoku Solver")
root.geometry("400x450")

frame = tk.Frame(root)
frame.pack(pady=10)

entries = [[None for _ in range(9)] for _ in range(9)]

for i in range(9):
    for j in range(9):
        e = tk.Entry(frame, width=2, font=("Arial", 18), justify="center")
        e.grid(row=i, column=j, padx=2, pady=2)
        entries[i][j] = e

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

solve_btn = tk.Button(btn_frame, text="Solve", command=solve, width=10, bg="lightgreen")
solve_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(btn_frame, text="Clear", command=clear, width=10, bg="lightcoral")
clear_btn.grid(row=0, column=1, padx=10)

exit_btn = tk.Button(btn_frame, text="Exit", command=root.destroy, width=10, bg="lightblue")
exit_btn.grid(row=0, column=2, padx=10)

root.mainloop()
