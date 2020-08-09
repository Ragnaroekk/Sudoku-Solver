# Author: Ray Franklin
# CS 325 HW 6 Portfolio Project
An implementation of a Sudoku game and solver. Based on the standard 9 x 9 board.
Uses numpy to print the broad as a matrix and was built on python 3.8.

A brief introduction to Sudoku.
From https://www.researchgate.net/publication/220174445_A_Survey_of_NP-Complete_puzzles pg. 25-26:
Sudoku:
"It is played on an n^2 × n^2 grid that is divided into n×n equal segments. Initially some cells in the grid
contain a number between 1...n^2. An action inserts a number between 1...n^2 into an empty cell. The goal is
to fill the grid with numbers such that every row, column, and segment contains the numbers 1...n^2 without any
repetitions. Deciding the solvability of Sudoku has been shown to be NP-Complete by Yato and Seta (2003)
(asis the closely related problem of constructing Latin squares from partially filled squares
(Colbourn, Colbourn,and Stinson, 1984)). Rodrigues Pereira, de Castro Dutra, and Clicia Stelling de Castro (2001)
apply constraint programming techniques to Sudoku. Nicolau and Ryan (2006) offer an evolutionary approach to
Sudoku. Werefer to Eppstein (2005), Lynas and Stoddart (2005), and Lewis (2007) for other approaches to Sudoku.
Theworld wide web is littered with Sudoku solvers. See http://www.sudoku.org.uk/ for some sample problems that
can be attempted online."

This program takes a list of lists where zeros are the empty squares as the Sudoku board. The board is listed in
sudoku.py and can be changed as required for different puzzles. Example layout:
        [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]
You can adjust the board as needed for different puzzles by changing out numbers as needed.
It is currently built to handle a 3^2 x 3^2 board but it could be changed to handle larger boards. Given the time
complexity to solve grows in exponential time, I've only worked with the standard 9 x 9 board.

To see the solution run "python sudoku.py" and it will print to console if one exists.
Example output:
 [[5 3 4 6 7 8 9 1 2]
 [6 7 2 1 9 5 3 4 8]
 [1 9 8 3 4 2 5 6 7]
 [8 5 9 7 6 1 4 2 3]
 [4 2 6 8 5 3 7 9 1]
 [7 1 3 9 2 4 8 5 6]
 [9 6 1 5 3 7 2 8 4]
 [2 8 7 4 1 9 6 3 5]
 [3 4 5 2 8 6 1 7 9]]



