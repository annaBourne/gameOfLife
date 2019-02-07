Game of Life
-------------

This project was written as a technical test for a Graduate Software Developer role. The Game of Life, or Life,
was created by John Conway in 1970 and is a cellular automaton. It is a zero-player game where a two-dimensional
grid of cells, which are either alive or dead, evolve based on a set of rules as defined in the game.

Rules of the game
-----------------

Scenario 0: No interactions
If there are no live cells, then in subsequent generations there will still be no live cells.

Scenario 1: Underpopulation
If a live cell has less than 2 live neighbours, this cell dies.

Scenario 2: Overcrowding
If a live cell has more than 3 neighbours, this cell dies.

Scenario 3: Survival
If a live cell has 2 or 3 neighbours, this cell remains alive.

Scenario 4: Creation of Life
If a cell is dead and has exactly 3 live neighbours, this cell becomes alive.

This implementation, built using Python 3.6, was built to display the results of two specific scenarios, as defined in
the candidate instructions: that of an initial grid with no live cells, and that of the classic blinker pattern grid.

Within the program, I have hard-coded the width and height of the grid matrix, purely because I had the two specific
scenarios to deal with. If I had free-reign, I would generate a grid matrix based on input from a user who could choose
their own size of grid. I could also create a random pattern of 1's and 0's to populate an initial grid.
Therefore to find the width and height without hard-coding, I would use something like:

width = len(grid)
height = len(input[0])

How to run the game
--------------------

To run this version of the game of life, you need to open a terminal or command line interface. You will need
Python 3 to be installed on your machine in order to run the program. Once you have navigated to the directory in which
gameOfLife.py resides, type python3 gameOfLife.py and the program will run.

References:

Creating a 2d matrix in python - https://stackoverflow.com/questions/4230000/creating-a-2d-matrix-in-python
Create a deep copy of a list of lists - https://stackoverflow.com/questions/19951816/python-changes-to-my-copy-variable-affect-the-original-variable