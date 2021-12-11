from functools import reduce

opens = set(['(', '[', '{', '<'])
closes = set([')', ']', '}', '>'])

closed_by = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

# part 1
'''
with open('input1') as f:
    score = 0
    scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    for line in f:
        opened = []
        for char in line.rstrip():
            if char in opens:
                opened.append(char)
            elif char in closes:
                o = opened.pop()
                if char != closed_by[o]:
                    score += scores[char]
                    break 
    print(score)
'''


# part 2
with open('input1') as f:
    scoring = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    scores = []

    for line in f:
        corrupt = False
        opened = []
        for char in line.rstrip():
            if char in opens:
                opened.append(char)
            elif char in closes:
                o = opened.pop()
                if char != closed_by[o]:
                    corrupt = True
                    break
        if not corrupt:
            score = reduce(lambda s, c: (s*5)+scoring[c], [closed_by[o] for o in reversed(opened)], 0)
            scores.append(score)
    
    scores.sort()
    print(scores[int(len(scores)/2)])
    