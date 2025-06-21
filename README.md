# SCT_SD_3

📌 Project Overview – Sudoku Solver with GUI

This project is developed as part of Task 03 for the SkillCraft Technology Internship – Software Development Track.

The goal of the task was to create a program that:

Automatically solves Sudoku puzzles

Accepts an input grid (with missing numbers)

Uses an efficient algorithm to compute the solution

Provides a user-friendly GUI for input and output


🧠 Problem Statement:

> "Create a program that solves Sudoku puzzles automatically.
The program should take an input grid representing an unsolved Sudoku puzzle and use an algorithm to fill in the missing numbers."


💡 Solution Approach:

The puzzle is solved using the backtracking algorithm, a recursive method well-suited for constraint satisfaction problems like Sudoku.

The interface is developed using Python's tkinter GUI library, which allows users to:

Enter their puzzle through input boxes

Solve the puzzle with one click

Clear the board and try a new puzzle


✅ Features:

User-driven application with GUI

Accepts custom input Sudoku puzzles

Validates and solves the puzzle using backtracking

Clear button to reset the board

Built with minimal dependencies (just Python and tkinter)
