import heapq
from itertools import product
from functools import reduce

# part 1
max_y = 0
y_v = 91
y = 0
for s in range(10000):
    y += y_v
    y_v -= 1
    max_y = max(max_y, y)
    if y < 0:
        break
print(s, y, max_y)

# part 2

#max_x = 30
#min_x = 20
#max_y = -5
#min_y = -10

max_x = 318
min_x = 277
max_y = -53
min_y = -92

# find tuples of x velocities and how many steps they can run within to not overshoot
x_tests = {}
for v in range(1, 400):
    valid_steps = set()
    x_v = v
    x = 0
    for s in range(1, 10000):
        x += x_v
        x_v -= 1
        if min_x-1 < x < max_x+1:
            valid_steps.add(s)
            if x_v == 0:
                # inifitely many steps above s possible with this velocity
                valid_steps.update([st for st in range(s,s+1000)])
        elif x > max_x:
            break
        if x_v == 0:
            break
    if len(valid_steps) > 0:
        x_tests[v] = valid_steps

# find tuple of y velocities and how many steps they can run within not to overshoot
y_tests = {}
for v in range(-300, 400):
    valid_steps = set()
    y_v = v
    y = 0
    for s in range(1, 10000):
        y += y_v
        y_v -= 1
        if min_y-1 < y < max_y+1:
            valid_steps.add(s)
        elif y <= min_y:
            break 
    if len(valid_steps) > 0:
        y_tests[v] = valid_steps

compatible = []

for x_v, x_steps in x_tests.items():
    for y_v, y_steps in y_tests.items():
        if x_steps & y_steps:
            compatible.append((x_v, y_v))

print(len(compatible))