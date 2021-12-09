from collections import Counter
lines = []

def parse_coords(str) -> tuple[tuple[int, int], tuple[int, int]]:
    line = str.rstrip()
    point_strs = line.split(' -> ')
    coords = point_strs[0].split(',')
    from_coord = (int(coords[0]), int(coords[1]))
    coords = point_strs[1].split(',')
    to_coord = (int(coords[0]), int(coords[1]))
    return (from_coord, to_coord)

def to_line(x, y) -> list[tuple[int, int]]:
    d0 = y[0] - x[0]
    d1 = y[1] - x[1]
    d = min(abs(d0), abs(d1))
    if d == 0:
        d = max(abs(d0), abs(d1))
    d0 = int(d0 / d)
    d1 = int(d1 / d)

    points = [x]
    while points[-1] != y:
        point = (points[-1][0]+d0, points[-1][1]+d1)
        points.append(point)

    return points


with open('input1') as f:
    lines = []
    for line in f:
        (from_coord, to_coord) = parse_coords(line)
        points = to_line(from_coord, to_coord)
        if not points:
            continue
        lines.extend(points)

    c = sum([1 for (point, count) in Counter(lines).most_common() if count > 1])
    print(c)