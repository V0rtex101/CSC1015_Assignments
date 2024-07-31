# Module that contains merging functions for 2048 game
# Fulufhelo Mulaudzi
# 15 April 2024

"""The fundamental logic of the following functions is mainly done in the push_left function and then all the other
 functions adapt the grid and call to this function whether directly or indirectly."""


def push_left(grid):
    """This function shifts all the elements in the given array to the left and makes sure to sum adjacent, equal
    elements together."""

    # This for loop is meant to iterate through the individual arrays in the grid
    for i in range(len(grid)):

        # This for loop pushes all non-zero elements to the left of the array
        for rep in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    grid[i][j] = grid[i][j + 1]
                    grid[i][j + 1] = 0

        # Makes sure that equal, adjacent elements are summed up to one spot, while leaving a zero in the other
        for j in range(3):
            if grid[i][j] == grid[i][j + 1]:
                grid[i][j] += grid[i][j + 1]
                grid[i][j + 1] = 0

        # Makes sure all non-zero elements are on the left
        for j in range(3):
            if grid[i][j] == 0:
                grid[i][j] = grid[i][j + 1]
                grid[i][j + 1] = 0


def push_right(grid):
    """This function moves all the elements in the grid to the right. It reverses the horizontal order each inside
    array and then makes use of the push_left function. After all that is done, it is reversed back to its original
    order to mimic a right shift of the array."""
    for row in grid:
        row.reverse()

    push_left(grid)

    for row in grid:
        row.reverse()


def push_up(grid):
    """This function shifts all the elements in the given array up and makes sure to sum adjacent, equal
    elements together."""
    # This for loop transposes the grid by opposing the rows and columns
    for i in range(4):
        for j in range(i, 4):
            temp = grid[i][j]
            grid[i][j] = grid[j][i]
            grid[j][i] = temp

    # After the grid is transposed, it is shifted left which mimics shifting it up in the original grid
    push_left(grid)

    # The grid is transposed back into the original arrangement after all the adjustments have been made
    for i in range(4):
        for j in range(i, 4):
            temp = grid[i][j]
            grid[i][j] = grid[j][i]
            grid[j][i] = temp


def push_down(grid):
    """This function pushes elements in the grid down. It works essentially the same way as the push_up function
    except that the push_right function is implemented instead of the push_left function so that it can mimic pushing
    all the elements down"""
    for i in range(4):
        for j in range(i, 4):
            temp = grid[i][j]
            grid[i][j] = grid[j][i]
            grid[j][i] = temp

    push_right(grid)

    for i in range(4):
        for j in range(i, 4):
            temp = grid[i][j]
            grid[i][j] = grid[j][i]
            grid[j][i] = temp
