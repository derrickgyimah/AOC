
time =  [52, 94,75,94]
distance = [426, 1374,1279, 1216]


scores = []
for i,t in enumerate(time):
    valid_finish = 0
    for x in range(1,t):
        held = x
        rem_distance = t-x
        total_travelled = held * rem_distance
        if total_travelled > distance[i]:
            valid_finish += 1
    scores.append(valid_finish)
            
print("Part 1 : ", scores[0]*scores[1]*scores[2]*scores[3])

Time = 52947594
Distance = 426137412791216

reps = 0
for x in range(1,Time):
    if x*(Time-x) > Distance:
        reps +=1

print("Part 2 : ", reps)
        
    