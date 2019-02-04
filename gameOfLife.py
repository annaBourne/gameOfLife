# Create grid size and initialise iteration to 1st
width = 5
height = 5
iterations = 1
empty_grid = [[0 for i in range(width)] for j in range(height)]


def print_grid(grid):
    title = "Output of iteration..." + str(iterations)
    print(title)
    output = ""
    for row in grid:
        for cell in row:
            if cell == 0:
                output += "- "
            else:
                output += "# "
        output += "\n"
    print(output)


def next_generation(grid, width, height):
    next_gen = empty_grid

    # Visit each interior cell
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            # Find live neighbouring cells
            live_cells = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    live_cells += grid[x + i][y + j]
            live_cells -= grid[x][y]

            # Apply rules of the game
            if grid[x][y] == 0 and live_cells == 0:
                next_gen[x][y] = 0

            elif grid[x][y] == 1 and live_cells < 2:
                next_gen[x][y] = 0

            elif grid[x][y] == 1 and (live_cells == 2 or live_cells == 3):
                next_gen[x][y] = 1

            elif grid[x][y] == 0 and live_cells == 3:
                next_gen[x][y] = 1
    return next_gen


def run_iterations(grid, iterations):
    print_grid(grid)
    new_grid = empty_grid
    for i in range(0, iterations):
        new_grid = next_generation(grid, width, height)
    print_grid(new_grid)



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
#next_generation(scenario2, 5, 5)
run_iterations(scenario2, 2)
