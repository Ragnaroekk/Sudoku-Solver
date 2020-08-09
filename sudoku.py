# Author: Ray Franklin
# CS 325 HW 6 Portfolio Project
# Description: A sudoku solver.
# Code developed based on Python Sudoku Solver - Computerphile
# https://www.youtube.com/watch?v=G_UYXzGuqvM
# With additional research from https://medium.com/@littleowllabs/solving-sudoku-with-elixir-d36f40232499,
# http://norvig.com/sudoku.html, and https://www.researchgate.net/publication/220174445_A_Survey_of_NP-Complete_puzzles

import numpy as np

# adjust as needed to match your puzzle, zeros represent empty squares
board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]

print("Starting board:", '\n', np.matrix(board), '\n')


def check_possible(col, row, num):
    """
    A function to check if a number 1-9 can be entered into a given square.
    :param col: The column in our 9 x 9 board
    :param row: The row in our 9 x 9 board
    :param num: The number, 0 through 9 to check
    :return: False if the number cannot be added to the square based on Sudoku rules, otherwise returns true
    """
    # using global so we can access the object outside of scope
    global board

    # check if the number can be used in each column
    for x in range(0, 9):
        if board[col][x] == num:
            return False

    # check if the number can be used in each row
    for y in range(0, 9):
        if board[y][row] == num:
            return False

    # check each 3x3 square
    row_0 = (row // 3) * 3
    col_0 = (col // 3) * 3
    for y in range(0, 3):
        for x in range(0, 3):
            if board[col_0 + y][row_0 + x] == num:
                return False
    return True


def solution():
    """A function to check if a sudoku board has a solution and print the result if so."""
    # using global so we can access the object outside of scope
    global board

    # check each 'empty' square on the board
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                for num in range(1, 10):
                    if check_possible(y, x, num):
                        board[y][x] = num  # fill the square with the new number
                        solution()  # keep checking until a solution is found or we've exhausted all options
                        board[y][x] = 0  # back track and reset the square to zero if it didn't work
                return  # we didn't find a solution
    return print("Solution:", '\n', np.matrix(board))  # solution found, print it.


if __name__ == '__main__':
    solution()
