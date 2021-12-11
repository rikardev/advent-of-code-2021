from functools import reduce
from itertools import product

# part 1
with open('input1') as f:
    energy_levels = []
    for row in f:
        energy_levels.append([])
        for energy in row.rstrip():
            energy_levels[-1].append(int(energy))
    
    rows = len(energy_levels)
    cols = len(energy_levels[0])

    def find_neighbours(row, col):
        candidates = [ 
            (row-1, col-1), (row-1, col), (row-1, col+1),
            (row, col-1), (row, col+1),
            (row+1, col-1), (row+1, col), (row+1, col+1)
        ]
        return list(filter(lambda p: -1 < p[0] < rows and -1 < p[1] < cols, candidates))

    steps = 100
    flashes = 0
    

    for step in range(steps):
        to_increase = list(product(list(range(rows)), list(range(cols))))
        while len(to_increase) > 0:
            (row, col) = to_increase[0]
            to_increase = to_increase[1:]
            energy_levels[row][col] += 1
            if energy_levels[row][col] == 10:
                # this has just flashed
                neighbours = filter(lambda p: energy_levels[p[0]][p[1]] < 10, find_neighbours(row, col))
                to_increase.extend(neighbours)
                flashes += 1
        
        for row in range(rows):
            for col in range(cols):
                if energy_levels[row][col] > 9:
                    energy_levels[row][col] = 0

    print(flashes)
            

# part 2
with open('input1') as f:
    energy_levels = []
    for row in f:
        energy_levels.append([])
        for energy in row.rstrip():
            energy_levels[-1].append(int(energy))
    
    rows = len(energy_levels)
    cols = len(energy_levels[0])

    def find_neighbours(row, col):
        candidates = [ 
            (row-1, col-1), (row-1, col), (row-1, col+1),
            (row, col-1), (row, col+1),
            (row+1, col-1), (row+1, col), (row+1, col+1)
        ]
        return list(filter(lambda p: -1 < p[0] < rows and -1 < p[1] < cols, candidates))

    flash_target = rows*cols
    steps = 0

    while True:
        steps += 1
        flashes = 0
        to_increase = list(product(list(range(rows)), list(range(cols))))
        while len(to_increase) > 0:
            (row, col) = to_increase[0]
            to_increase = to_increase[1:]
            energy_levels[row][col] += 1
            if energy_levels[row][col] == 10:
                # this has just flashed
                neighbours = filter(lambda p: energy_levels[p[0]][p[1]] < 10, find_neighbours(row, col))
                to_increase.extend(neighbours)
                flashes += 1
        
        if flashes == flash_target:
            break

        for row in range(rows):
            for col in range(cols):
                if energy_levels[row][col] > 9:
                    energy_levels[row][col] = 0
        

    print(steps)