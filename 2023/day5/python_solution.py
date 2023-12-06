from collections import defaultdict
import re

f = open(r"2023\day5\data.txt")
data = f.read()
data = data.split("\n\n")


### destination range start >>> source range start >>> range length

seed = data[0].split(":")[1]
seed = [int(x) for x in re.findall(r"-?\d+", seed)]

sts, stf, ftw, wtl, ltt, tth, htl = data[1:]
labels = sts, stf, ftw, wtl, ltt, tth, htl




def mapping_func(seed,label):
    for row in label:
        destination, source, rang = [int(x) for x in row.split()]
        if source<=seed<source+rang:
            return (seed-source) + destination
    return seed

        
location = []

for s in seed:
    s = int(s)
    for label in labels:
        Stage = label.split("\n")
        s = mapping_func(s,Stage[1:])
    location.append(s)
    
    
print("Part 1: ",min(location))

new_seeds = []   
new_ranges = []  
        
for x in seed:
    if len(new_seeds) <= len(new_ranges):
        new_seeds +=[x]
    else:
        new_ranges +=[x]


new_seed_values = []

for i, seed in enumerate(new_seeds):
    new_seed_values +=[seed]
    value = new_ranges[i]
    print(value)
    while value != 0:
        new_seed_values +=[seed+1]
        value += -1
        
        
        
        
    
    


