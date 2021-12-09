

with open('input1') as f:
    h, v = 0, 0
    for line in f:
        parts = line.rstrip().split(' ')
        match parts[0]:
            case 'forward':
                h += int(parts[1])
            case 'up':
                v -= int(parts[1])
            case 'down':
                v += int(parts[1])

    print(h, v, h*v)

with open('input1') as f:
    h, v, a = 0, 0, 0
    for line in f:
        parts = line.rstrip().split(' ')
        match parts[0]:
            case 'forward':
                h += int(parts[1])
                v += a*int(parts[1])
            case 'up':
                a -= int(parts[1])
            case 'down':
                a += int(parts[1])

    print(h, v, h*v)