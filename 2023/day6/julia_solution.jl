
time =  [52, 94,75,94]
distance = [426, 1374,1279, 1216]


scores = []


for (i,t) in enumerate(time)
    global valid_finish = 0
    for x in range(1,t)
        if x*(t-x) > distance[i]
            global valid_finish += 1
        end
    end
    push!(scores,valid_finish)
end

ans1 = prod(scores)
println("Part 1 : ",ans1)


Time = 52947594
Distance = 426137412791216

ans2 = 0
for x in range(1,Time)
    if x*(Time-x) > Distance
        global ans2 +=1
    end
end

println("Part 2 : ",ans2)