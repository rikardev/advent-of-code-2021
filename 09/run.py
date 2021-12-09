from functools import reduce

with open('input1') as f:
    matrix = []
    for line in f.readlines():
        row = [int(c) for c in line.rstrip()]
        matrix.append(row)

    num_cols = len(matrix[0])
    num_rows = len(matrix)

    # part 1
    min_points = []
    for r in range(num_rows):
        for c in range(num_cols):
            if c > 0 and matrix[r][c-1] <= matrix[r][c]:
                continue
            if c+1 < num_cols and matrix[r][c+1] <= matrix[r][c]:
                continue
            if r > 0 and matrix[r-1][c] <= matrix[r][c]:
                continue
            if r+1 < num_rows and matrix[r+1][c] <= matrix[r][c]:
                continue
            min_points.append((r, c))

    # part 2
    visited = set()

    def explore_basin(start: tuple[int, int]) -> list[tuple[int, int]]:
        basin = []
        to_visit = [start]
        while len(to_visit) > 0:
            point = to_visit[0]
            to_visit = to_visit[1:]
            
            if point in visited:
                continue
            
            visited.add(point)
            
            row, col = point
            if matrix[row][col] == 9:
                # not part of basin
                continue
            
            basin.append(point)
            
            if row > 0:
                if not (row-1, col) in visited:
                    to_visit.append((row-1, col))
            if row+1 < num_rows:
                if not (row+1, col) in visited:
                    to_visit.append((row+1, col))
            if col > 0:
                if not (row, col-1) in visited:
                    to_visit.append((row, col-1))
            if col+1 < num_cols:
                if not (row, col+1) in visited:
                    to_visit.append((row, col+1))
        
        return basin

    basins = []

    for r in range(num_rows):
        for c in range(num_cols):
            point = (r, c)
            if not point in visited and matrix[r][c] != 9:
                basin = explore_basin(point)
                if len(basin) > 0:
                    basins.append(basin)

    basins.sort(key=len, reverse=True)
    for basin in basins:
        print(len(basin), basin)
    

    print(reduce(lambda x, y: x*y, [len(b) for b in basins[:3]]))
    