
import itertools

from toolz.itertoolz import sliding_window

with open('input1_1') as f:
    print(sum(1 for (a,b) in itertools.pairwise(int(line.rstrip()) for line in f) if b > a))


input = [
199,
200,
208,
210,
200,
207,
240,
269,
260,
263,
]

with open('input1_2') as f:
    print(print(sum(1 for (a, b) in sliding_window(2, sliding_window(3, (int(line) for line in f))) if sum(b) > sum(a))))

