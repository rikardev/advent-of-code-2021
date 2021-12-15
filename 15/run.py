import heapq
from itertools import product

# part 1
with open('input1') as f:
    matrix = []
    for row in f:
        matrix.append([int(i) for i in row.rstrip()])
    
    cols = len(matrix[0])
    rows = len(matrix)

    neighbours = {}
    risks = {}
    for (row, col) in list(product(list(range(rows)), list(range(cols)))):
        candidates = [ (row-1, col), (row, col-1), (row, col+1), (row+1, col)]
        ns = list(filter(lambda p: -1 < p[0] < rows and -1 < p[1] < cols, candidates))
        neighbours[(row, col)] = ns
        risks[(row, col)] = 999999999
        
    # risk, point
    candidates = [(0, (0,0))]
    target = (rows-1, cols-1)
    risks[(0,0)] = 0

    while len(candidates) > 0:
        (risk, point) = heapq.heappop(candidates)
        if point == target:
            print('end', risk)
            break
        
        if risks[point] < risk:
            continue
        
        for n in neighbours[point]:
            (row, col) = n
            n_risk = risk + matrix[row][col]
            if n_risk < risks[n]:
                heapq.heappush(candidates, (n_risk, n))
                risks[n] = n_risk
        

def increment(num: int, by: int) -> int:
    inc = num + by
    if inc > 9:
        return inc - 9
    else:
        return inc

# part 2
with open('input1') as f:
    matrix = []
    for line in f:
        original = [int(i) for i in line.rstrip()]
        row = []
        for add in range(5):
            row.extend([increment(i, add) for i in original])
        matrix.append(row)
    
    extended = []
    for add in range(5):
        for row in matrix:
            extended.append([increment(i, add) for i in row])

    matrix = extended

    cols = len(matrix[0])
    rows = len(matrix)

    neighbours = {}
    risks = {}
    for (row, col) in list(product(list(range(rows)), list(range(cols)))):
        candidates = [ (row-1, col), (row, col-1), (row, col+1), (row+1, col)]
        ns = list(filter(lambda p: -1 < p[0] < rows and -1 < p[1] < cols, candidates))
        neighbours[(row, col)] = ns
        risks[(row, col)] = 999999999
        
    # risk, point
    candidates = [(0, (0,0))]
    target = (rows-1, cols-1)
    risks[(0,0)] = 0

    while len(candidates) > 0:
        (risk, point) = heapq.heappop(candidates)
        if point == target:
            print('end', risk)
            break
        
        if risks[point] < risk:
            continue
        
        for n in neighbours[point]:
            (row, col) = n
            n_risk = risk + matrix[row][col]
            if n_risk < risks[n]:
                heapq.heappush(candidates, (n_risk, n))
                risks[n] = n_risk
        
