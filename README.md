


# Sudoku Solver
![image](https://github.com/Runnes/sudoku_solver/assets/43543552/4a3aa6b2-99db-49c1-ac76-a14c2a4ca891)

## Introduction

This project is a Sudoku Solver that uses backtracking algorithm to solve Sudoku puzzles. The goal of this project is to create an efficient and user-friendly tool for solving Sudoku puzzles.

## How It Works

The Sudoku Solver works in the following steps:

1. **Input the Sudoku puzzle**: The user inputs the Sudoku puzzle into the program. The unsolved cells are represented by zeros.

2. **Solve the puzzle**: The program uses a backtracking algorithm to solve the puzzle. This algorithm tries out all possible numbers for each unsolved cell and backtracks whenever it encounters a cell where no number is valid.

3. **Output the solution**: Once the puzzle is solved, the program outputs the solution.

## Thinking Behind the Steps

The backtracking algorithm was chosen for this project because it is a simple and effective method for solving Sudoku puzzles. It works by filling in the empty cells in a row-wise manner. For each cell, it tries all numbers from 1 to 9. If a number can be placed in the current cell, it moves to the next cell. If it cannot find a number for the current cell, it backtracks to the previous cell and tries the next number. This process continues until the puzzle is solved.

## Future Plans

In the future, we plan to add a feature that allows users to scan an image of a Sudoku puzzle instead of inputting it manually. This will make the program more user-friendly and efficient.

## Conclusion

We hope you find this Sudoku Solver helpful and easy to use. If you have any suggestions or feedback, please feel free to contact us.




