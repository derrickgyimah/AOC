f = open(r"2018\day1\data.txt")
data = f.read()
data = data.split("\n")



ans1 = 0
ans2 = 0


for i,line in enumerate(data):
    ans1 +=int(line)
print("Part 1 : ", ans1)



data = 200*data
total = 0
frequencies = []
for i,line in enumerate(data):
    total +=int(line)
    if total not in frequencies:
        frequencies.append(int(total))
    else:
        ans2 = total
        break

    
print("Part 2 : ", ans2)


