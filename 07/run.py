from statistics import mean

travel_costs = {}
def travel_cost(start: int, end: int) -> int:
    if (start, end) in travel_costs:
        return travel_costs[(start,end)]
    elif (end, start) in travel_costs:
        return travel_costs[(end,start)]
    else:
        c = sum([i for i in range(abs(end-start)+1)])
        travel_costs[(start,end)] = c
        return c
         

def cost(crabs: list[int], val: int) -> int:
    return sum([travel_cost(c, val) for c in crabs])

with open('input1') as f:
    crabs = [int(s) for s in f.readline().rstrip().split(',')]
    min_cost = min([cost(crabs, v) for v in range(min(crabs), max(crabs)+1)])
    print(min_cost)

    '''
    min_pos = None
    min_cost = 100000000000
    for v in range(min(crabs), max(crabs)+1):
        vc = cost(crabs, v)
        print(v, vc)
        if vc < min_cost:
            min_cost = vc
            min_pos = v

    print(min_pos, min_cost)
    '''

