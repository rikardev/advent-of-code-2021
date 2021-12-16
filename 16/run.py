import heapq
from itertools import product
from functools import reduce

hex_to_binary = {"{0:X}".format(i): "{0:04b}".format(i) for i in range(16)}

def parse_packet(input):
    version = int(input[:3], 2)
    type = int(input[3:6], 2)

    input = input[6:]

    match type:
        case 4:
            # parse literal            
            binary = ''
            while True:
                chunk = input[:5]
                input = input[5:]
                binary += chunk[1:]
                if chunk[0] == '0':
                    break
            
            return (('LITERAL', version, int(binary, 2)), input)

        case _:
            # parse operator
            mode = input[0]
            input = input[1:]
            packs = []
            if mode == '0':
                pack_bits = int(input[:15], 2)
                input = input[15:]
                remaining = input
                while len(input)-len(remaining) < pack_bits:
                    pack, remaining = parse_packet(remaining)
                    packs.append(pack)
                input = remaining
            else:
                sub_packs = int(input[:11], 2)
                input = input[11:]
                remaining = input
                for _ in range(sub_packs):
                    pack, remaining = parse_packet(remaining)
                    packs.append(pack)
                input = remaining

            return (('OPERATOR', version, type, packs), input)

def part1(p):
    match p:
        case ('LITERAL', version, literal):
            return version
        case ('OPERATOR', version, type, packs):
            return version + sum([part1(p) for p in packs])


def part2(p):
    match p:
        case ('LITERAL', _, literal):
            return literal
        case ('OPERATOR', _, 0, packs): # sum
            return sum([part2(p) for p in packs])
        case ('OPERATOR', _, 1, packs): # product
            if len(packs) == 1:
                return part2(packs[0])
            else: 
                return reduce(lambda x, y: x * y, [part2(p) for p in packs])
        case ('OPERATOR', _, 2, packs): # min
            return min([part2(p) for p in packs])
        case ('OPERATOR', _, 3, packs): # max
            return max([part2(p) for p in packs])
        case ('OPERATOR', _, 5, packs): # greater than
            if part2(packs[0]) > part2(packs[1]):
                return 1
            else:
                return 0
        case ('OPERATOR', _, 6, packs): # less than  
            if part2(packs[0]) < part2(packs[1]):
                return 1
            else:
                return 0
        case ('OPERATOR', _, 7, packs): # equal  
            if part2(packs[0]) == part2(packs[1]): 
                return 1 
            else: 
                return 0

def parse_bin(s):
    return ''.join([hex_to_binary[hex] for hex in s])

def run_part1(s):
    p, _ = parse_packet(parse_bin(s))
    print(part1(p))

def run_part2(s):
    p, _ = parse_packet(parse_bin(s))
    print(part2(p))
    
run_part2('C200B40A82')
run_part2('04005AC33890')
run_part2('880086C3E88112')
run_part2('CE00C43D881120')
run_part2('D8005AC2A8F0')
run_part2('F600BC2D8F')
run_part2('9C005AC2F8F0')
run_part2('9C0141080250320F1802104A08')

with open('input1') as f:
    s = f.readline().rstrip()
    run_part1(s)
    run_part2(s)
    
    
    