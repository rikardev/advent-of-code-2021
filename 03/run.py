
'''
with open('input1') as f:
    a = []
    for line in f:
        line = line.rstrip()
        if len(a) == 0:
            a = [0] * len(line)
        for i, v in enumerate(line):
            match v:
                case '0':
                    a[i]-=1
                case '1':
                    a[i]+=1
    
    gamma, epsilon = '', ''
    for d in a:
        if d > 0:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    
    print(int(gamma, 2) *int(epsilon, 2))
'''

def most_common(nums, i):
    c = 0
    for num in nums:
        if num[i] == '0':
            c -= 1
        elif num[i] == '1':
            c += 1
    return c

with open('input1') as f:
    oxygen = []
    carbon = []
    for line in f:
        oxygen.append(line.rstrip())
        carbon.append(line.rstrip())

    i = 0
    while len(oxygen) > 1:
        common = most_common(oxygen, i)
        #print(i, common, oxygen)
        if common >= 0:
            oxygen_keep = lambda x: x[i] == '1'
        else:
            oxygen_keep = lambda x: x[i] == '0'
        new_oxygen = []
        for o in oxygen:
            if oxygen_keep(o):
                new_oxygen.append(o)
        oxygen = new_oxygen
        i += 1

    i = 0
    while len(carbon) > 1:
        common = most_common(carbon, i)
        #print(i, common, carbon)
        if common >= 0:
            carbon_keep = lambda x: x[i] == '0'
        else:
            carbon_keep = lambda x: x[i] == '1'
        new_carbon = []
        for c in carbon:
            if carbon_keep(c):
                new_carbon.append(c)
        carbon = new_carbon
        i += 1   
    

    print(len(oxygen), oxygen[0], int(oxygen[0], 2))
    print(len(carbon), carbon[0], int(carbon[0], 2))
    print(int(oxygen[0], 2) * int(carbon[0], 2))



