from collections import defaultdict
f = open(r"2018\day2\data.txt")
data = f.read()
data = data.split("\n")


twos = 0
threes = 0

for i,line in enumerate(data):
    mapping = defaultdict(int)
    for l in line:
        mapping[l] += 1
    
    with2 = [key for key,values in mapping.items() if values == 2]
    with3 = [key for key,values in mapping.items() if values == 3]
    
    if len(with2) > 0:
        twos += 1
    
    if len(with3) > 0:
        threes += 1
        
ans1 = twos * threes

print("Part 1 : ",ans1)



for i,line in enumerate(data):
    
    for check in data:
        total = 0
        for l in range(len(check)):
            if check[l]  != data[l]:
                total += 1
        if total == 1:
            print(i,line) 
                