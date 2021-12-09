from collections import Counter

num_days = 256

with open('input1') as f:
    fish_counter = Counter([int(f) for f in f.readline().rstrip().split(',')])
    fishes = []
    for i in range(9):
        fishes.append(fish_counter[i])
    
    for i in range(num_days):
        births = fishes[0]
        fishes = fishes[1:] 
        fishes[6] += births
        fishes.append(births)
        print(fishes)
   
    print(sum(fishes))
