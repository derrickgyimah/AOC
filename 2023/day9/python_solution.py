import re
from collections import defaultdict
f = open(r"2023\day9\data.txt")
data = f.read()
data = data.split("\n")



data = [[int(x) for x in y.split()] for y in data]




part1 = 0

for x, string in enumerate(data):
    new_set = string
    iterations = 0
    next_num = 0
    while len(list(set(new_set))) != 1:
        iterations +=1
        next_num += new_set[-1]
        new_nums = []
        for i, num in enumerate(new_set[:-1]):
            ans =  new_set[i+1] - num
            new_nums.append(ans)
        new_set = new_nums
        
    next_num = next_num+new_set[-1]
    part1 += next_num 

        
print("Part 1 : ",part1)


part2 = 0

for x, string in enumerate(data):
    new_set = string[::-1] ### Reverse the list
    iterations = 0
    next_num = 0
    while len(list(set(new_set))) != 1:
        iterations +=1
        next_num += new_set[-1]
        new_nums = []
        for i, num in enumerate(new_set[:-1]):
            ans =  new_set[i+1] - num
            new_nums.append(ans)
        new_set = new_nums
        
    next_num = next_num+new_set[-1]
    part2 += next_num 

        
print("Part 2 : ",part2)
