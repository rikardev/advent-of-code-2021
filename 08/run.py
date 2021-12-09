def sorted_string(input_str: str) -> str:
    return ''.join(sorted(input_str))

def parse_line(line: str) -> tuple[list[str], list[str]]:
    parts = line.rstrip().split(' | ')
    input = [sorted_string(s) for s in parts[0].split(' ')]
    output = [sorted_string(s) for s in parts[1].split(' ')]
    return (input, output)

# "2", "3", "5"  -> least distance between the others = "3"
def find_three(input: list[str]) -> str:
    fives = [s for s in input if len(s) == 5]
    for s in fives:
        if sum([len(set(s)-set(s0)) for s0 in fives]) == 2:
            return s

def find_nine(input: list[str], mapping: dict[int, str]) -> str:
    sixes = [s for s in input if len(s) == 6]
    three = set(mapping[3])
    for s in sixes:
        if len(set(s) - three) == 1:
            return s

def find_five(input: list[str], mapping: dict[int, str]) -> str:
    fives = [s for s in input if len(s) == 5]
    d = set(mapping[4]) - set(mapping[1])
    for s in fives:
        if len(set(s) & d) == 2:
            return s

def find_two(input: list[str], mapping: dict[int, str]) -> str:
    return [s for s in input if len(s) == 5 and s != mapping[3] and s != mapping[5]][0]

def find_six(input: list[str], mapping: dict[int,str]) -> str:
    six_set = set(mapping[8]) - (set(mapping[4]) - set(mapping[5]))
    return ''.join(sorted(six_set))

def find_zero(input: list[str], mapping: dict[int,str]) -> str:
    others = set([v for _, v in mapping.items()])
    return ''.join(sorted(set(input) - others))

with open('input1') as f:
    lines = [parse_line(l) for l in f.readlines()]

    out_sum = 0
    for (input,output) in lines:
        mapping = {
            1: [s for s in input if len(s) == 2][0],
            4: [s for s in input if len(s) == 4][0],
            7: [s for s in input if len(s) == 3][0],
            8: [s for s in input if len(s) == 7][0]
        }

        mapping[3] = find_three(input)
        mapping[5] = find_five(input, mapping)
        mapping[9] = find_nine(input, mapping)
        mapping[2] = find_two(input, mapping)
        mapping[6] = find_six(input, mapping)
        mapping[0] = find_zero(input, mapping)
               
        inv_mapping = {v:k for k,v in mapping.items()}

        out = int(''.join([str(inv_mapping[out]) for out in [sorted_string(s) for s in output]]))
        out_sum += out

    print(out_sum)
