from itertools import product

# part 1
with open('input1') as f:
    dots = set()
    max_x = 0
    max_y = 0
    for row in f:
        row = row.rstrip()
        if row == '':
            break
        d = row.split(',')
        dot = (int(d[0]), int(d[1]))
        max_x = max(dot[0], max_x)
        max_y = max(dot[1], max_y)
        dots.add(dot)
        
    folds = []
    for row in f:
        row = row.rstrip()
        if row.startswith('fold along'):
            fold = row.split(' ')[-1]
            f = fold.split('=')
            folds.append((f[0], int(f[1])))

    
    for (dim, size) in folds:
        if dim == 'x':
            max_x -= size
        if dim == 'y':
            max_y -= size
        new_dots = set()
        while dots:
            dot = dots.pop()
            if dim == 'x' and dot[0] > size:
                diff = dot[0]-size
                new_dot = (size-diff, dot[1])
                new_dots.add(new_dot)
            elif dim == 'y' and dot[1] > size:
                diff = dot[1]-size
                new_dot = (dot[0], size-diff)
                new_dots.add(new_dot)
            else:
                new_dots.add(dot)
        dots = new_dots
    
    for y in range(max_y):
        row = []
        for x in range(max_x):
            row.append('.')
            if (x,y) in dots:
                row[-1] = '#'
        
        print(''.join(row))

    dots = sorted(list(dots))


    print(dots)
    print(len(dots))
    