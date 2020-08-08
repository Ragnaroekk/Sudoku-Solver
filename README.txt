An implementation of a Sudoku game and solver.

A brief introduction to Sudoku.
From https://www.researchgate.net/publication/220174445_A_Survey_of_NP-Complete_puzzles pg. 25-26:
"Sudoku(also known as Number Place) was first published in Dell Magazines in 197910. It is currently
attracting more attention than other puzzles, perhaps because it is featured regularly in daily news articles.
It is played on an n^2×n^2 grid that is divided into n×n equal segments. Initially some cells in the grid
contain a number between1...n2. An action inserts a number between1...n2into an empty cell. The goal is
to fill the grid with numbers such that every row, column, and segment contains the numbers1...n2without any
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
You can adjust the board as needed for different puzzles. Then run sudoku.py to see the solution printed to
console if one exists.
