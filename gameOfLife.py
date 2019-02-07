#!/usr/bin/env python3

import copy

# Create grid size, initialise iteration to 1st and create empty grid
width = 5
height = 5
iterations = 1
empty_grid = [[0 for i in range(width)] for j in range(height)]


def print_grid(current_grid, item):
    print("Output of iteration...{0}".format(item))
    output = ""
    for row in current_grid:
        for cell in row:
            if cell == 0:
                output += "- "
            else:
                output += "# "
        output += "\n"
    print(output)


def next_generation(current_grid, width, height):
    next_gen = copy.deepcopy(empty_grid)

    # Visit each interior cell
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            # Find live neighbouring cells
            live_cells = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    live_cells += current_grid[x + i][y + j]
            live_cells -= current_grid[x][y]

            # Apply rules of the game
            if current_grid[x][y] == 0 and live_cells == 0:
                next_gen[x][y] = 0

            elif current_grid[x][y] == 1 and live_cells < 2:
                next_gen[x][y] = 0

            elif current_grid[x][y] == 1 and (live_cells == 2 or live_cells == 3):
                next_gen[x][y] = 1

            elif current_grid[x][y] == 0 and live_cells == 3:
                next_gen[x][y] = 1
    return next_gen


def run_iterations(current_grid, iterations):
    item = 0
    print_grid(current_grid, item)
    for item in range(1, iterations + 1):
        new_grid = next_generation(current_grid, width, height)
        current_grid = new_grid
        print_grid(current_grid, item)


# Test case 1 - Grid with no live cells
scenario1 = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

# Test case 2 - Initial state as defined in the question
scenario2 = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 1, 1, 1, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

# print_grid(next_gen, 1)
# next_generation(scenario2, 5, 5)
run_iterations(scenario2, 3)
