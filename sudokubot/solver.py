from utils import search , display, grid_values, row_units
import sys

def solve(grid, format='string'):
    if len(grid) != 81:
        print 'ERROR: Sudoku length is not proper'
        sys.exit()
    
    values = search(grid_values(grid))
    if '' in values.values():
        print 'INFO: Invalid Sudoku'
        sys.exit()

    format_output = ""
    for row in row_units:
        for cell in row:
            format_output += values[cell]

    if format=='grid':
        display(values)
    else:
        print format_output

diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
solve(diag_sudoku_grid, 'grid')
