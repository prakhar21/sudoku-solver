def possible_cells(A, B):
    return [s+t for s in A for t in B]

rows = 'ABCDEFGHI'
cols = '123456789'
boxes = possible_cells(rows, cols)
row_units = [possible_cells(r, cols) for r in rows]
column_units = [possible_cells(rows, c) for c in cols]
square_units = [possible_cells(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
unitlist = row_units + column_units + square_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)


def grid_values(grid):
    possibility = cols
    initial_state = {}
    for b, g in zip(boxes, grid):
        if g=='.':
            initial_state[b] = possibility
        else:
            initial_state[b] = g
    return initial_state


def eliminate(values):
    for k, v in values.items():
        if len(v)==1:
            for p in peers[k]:
                values[p] = values[p].replace(v,'')        
    return values


def only_choice(values):
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values



def reduce_puzzle(values):
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        if solved_values_before==81:
            stalled=True
        else:
            values = eliminate(values)
 
        values = only_choice(values)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
    return values
    
    
def search(values):
    values = reduce_puzzle(values)
    if values != False:
        cell_few_poss = sorted(values.items(), key=lambda x: len(x[1]), reverse=False)
        cell_few_poss = [i for i in cell_few_poss if len(i[1])>1]
        
        if len(cell_few_poss)==0:
            return values
        
        cell = cell_few_poss[0][0]
        possibilities = cell_few_poss[0][1]
        
        for p in possibilities:
            new_sudoku = values.copy()
            new_sudoku[cell] = p
            attempt = search(new_sudoku)
            if attempt:
                return attempt
    else:
        return False
        
def display(values):
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': 
            print(line)
    print
