f = open(raw"2023\day2\data.txt")
data = read(f, String)
close(f)

data = split(data, "\n")

ans1 = 0
ans2 = 0

red = 12
green = 13
blue = 14

colours = ["red", "green", "blue"]

all_scores = []
for (i, game) in enumerate(data)
    rounds = split(split(game, ":")[2], ";")
    games_played = length(rounds)
    reds = [0]
    greens = [0]
    blues = [0]
    for x in 1:games_played
        for colour in colours
            if occursin(colour, rounds[x])
                index = findfirst(colour, rounds[x])[1]
                current_colour = parse(Int64,strip(string(string(rounds[x][index - 3]), string(rounds[x][index - 2]))))
                if colour == "red"
                    push!(reds, current_colour)
                elseif colour == "green"
                    push!(greens, current_colour)
                elseif colour == "blue"
                    push!(blues, current_colour)
                end
                println(current_colour)
            end
        end
    end
    push!(all_scores, (maximum(reds), maximum(greens), maximum(blues)))
end
println(all_scores)

for (i, j) in enumerate(all_scores)
    if red >= j[1] && green >= j[2] && blue >= j[3]
        global ans1 += i + 1
    end
end
println(ans1)


for j in all_scores
    local ans = j[1] * j[2] * j[3]
    global ans2 += ans
end
println(ans2)

