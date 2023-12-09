import re
from collections import defaultdict
f = open(r"2023\day8\data.txt")
data = f.read()
data = data.split("\n\n")


directions = [x for x in data[0]]*2000000

routing = data[1].replace("=","").replace(",","").replace("  "," ").replace("(","").replace(")","")
routing = [x for x in routing.split("\n")]
routing = [x.split() for x in routing]


# start = "AAA"
# finish = "ZZZ"

# ans1 = 0

# current = "AAA"
# for D in directions:
#     while current != finish:
#         if D == "L":
#             location = [x for x in routing if x[0] == current][0]
#             current = location[1]
#         if D == "R":
#             location = [x for x in routing if x[0] == current][0]
#             current = location[2]
#         ans1 +=1
#         break
        
# print(ans1)   

ans2 = 0     

current_group = [x[0] for x in routing if x[0][2] == "A"]

for D in directions:
    while list(set([x[2] for x in current_group])) != ["Z"]:
        print(ans2,list(set([x[2] for x in current_group])))
        ans2 +=1
        locations = []
        if D == "L":
            for i, string in enumerate(current_group):
                for j,route in enumerate(routing):
                    if string == route[0]:
                        locations.append(route[1])
        if D == "R":
            locations = []
            for i, string in enumerate(current_group):
                for j,route in enumerate(routing):
                    if string == route[0]:
                        locations.append(route[2])
        current_group = locations
        break
    
        
            
                        


            

