from itertools import product
from toolz.itertoolz import sliding_window
from collections import Counter

# part 1
with open('input0') as f:
    start = f.readline().rstrip()
    f.readline()

    transforms = {}
    
    for line in f:
        t = line.rstrip().split(' -> ')
        transforms[(t[0][0], t[0][1])] = t[1]
    
    max_depth = 10
    counts = Counter(list(start))

    candidates = [(pair,0) for pair in sliding_window(2, start)]

    while len(candidates) > 0:
        (pair, depth) = candidates[0]
        candidates = candidates[1:]
        if depth < max_depth and pair in transforms:
            add = transforms[pair]
            counts.update([add])
            if depth+1 < max_depth:
                candidates.append(((pair[0], add), depth+1))
                candidates.append(((add, pair[1]), depth+1))

    len(counts)
    counter = Counter(counts).most_common()
    print(counter[0][1] - counter[-1][1])
    

# part 2
# iterate on the transformations instead of the input
with open('input1') as f:
    start = f.readline().rstrip()
    f.readline()

    transforms = {}
    
    for line in f:
        t = line.rstrip().split(' -> ')
        transforms[(t[0][0], t[0][1])] = ((t[0][0], t[1]), (t[1], t[0][1]))

    #print(transforms)
    
    transformations = {}
    for pair in sliding_window(2, start):
        transformations[pair] = transformations.get(pair, 0) + 1
    
    max_depth = 40
    for depth in range(max_depth):
        next_transformations = {}
        for transform, (left, right) in transforms.items():
            if transform in transformations:
                count = transformations[transform]
                next_transformations[left] = next_transformations.get(left, 0) + count
                next_transformations[right] = next_transformations.get(right, 0) + count
        transformations = next_transformations

    counter = {}
    for (a,b), count in transformations.items():
        counter[a] = counter.get(a, 0) + count
        counter[b] = counter.get(b, 0) + count

    counter[start[0]] += 1
    counter[start[-1]] += 1

    min, max = None, None
    min_letter, max_letter = None, None
    for letter, count in counter.items():
        if not min or min > count/2:
            min = count/2
            min_letter = letter
        if not max or max < count/2:
            max = count/2
            max_letter = letter

    print(counter)
    print(min, min_letter)
    print(max, max_letter)

    print(max-min)


