from functools import reduce
from itertools import product
from copy import deepcopy

class GraphIter():
    def __init__(self, node: str):
        self.node = node
        self.path = [node]
        self.visited = set([node])
        self.can_revisit = True

    def move_to(self, next_node: str):
        next = deepcopy(self)
        next.node = next_node
        # add this to visited if it's a small cave
        if next_node.islower():
            next.visited.add(next_node)
            if next_node in self.visited:
                next.can_revisit = False

        next.path.append(next_node)
        return next
    
    def can_visit(self, node):
        return node.isupper() or self.can_revisit or not node in self.visited 

# part 1 & 2
with open('input1') as f:
    edges = {}
    for edge_str in f:
        edge = edge_str.rstrip().split('-')
        if edge[0] in edges:
            edges[edge[0]].add(edge[1])
        else:
            edges[edge[0]] = set([edge[1]])

        if edge[1] in edges:
            edges[edge[1]].add(edge[0])
        else:
            edges[edge[1]] = set([edge[0]])
        
    
    origin = 'start'
    target = 'end'

    iterators = [GraphIter(origin)]
    paths = []

    rounds = 0

    while len(iterators) > 0:
        current = iterators[0]
        iterators = iterators[1:]
        if current.node == target:
            paths.append(current.path)
            continue

        iterators.extend([current.move_to(next) for next in edges[current.node] if current.can_visit(next) and next != 'start'])
        rounds += 1
        if rounds % 100 == 0:
            print(len(iterators))

    print(len(paths))