# A module of utility functions for manipulating 2-D arrays of size 4x4
# Fulufhelo Mulaudzi
# 15 April 2024

import copy

def create_grid(grid):
    """Creates a 4x4 array of zeroes within grid"""
    for i in range(4):
        grid.append([0, 0, 0, 0])
    return grid


def print_grid(grid):
    """Prints out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for row in grid:
        print("|", end="")
        for i in row:
            if i == 0:
                i = " "
            print('{:<4} '.format(i), end='')
        print("|")
    print("+--------------------+")


def check_lost(grid):
    """Returns True if there are no 0 values and there are no adjacent values that are equal; otherwise False"""
    for i in range(len(grid)):
        # Checks if any of the elements are zero
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                return False
        # Checks if an element is equal to the element to its sides
        for j in range(len(grid[i])-1):
            if grid[i][j] == grid[i][j+1]:
                return False
    # Checks if an element is equal to the element below it
    for i in range(len(grid)-1):
        for j in range(len(grid[i])):
            if grid[i][j] == grid[i+1][j]:
                return False
    return True


def check_won(grid):
    """Returns True if a value greater or equal to 32 is found in the grid; otherwise False"""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] >= 32:
                return True
    return False


def copy_grid(grid):
    """Returns a copy of the given grid"""
    grid_copy = copy.deepcopy(grid)
    return grid_copy


def grid_equal(grid1, grid2):
    """Checks if 2 grids are equal"""
    if grid1 == grid2:
        return True
    else:
        return False

