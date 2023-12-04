# Using readline
f = open(raw"2023\day1\data.txt", "r")
data = readlines(f)


p1 = 0
for (i, string) in enumerate(data)
    numbers = [parse(Int64, x) for x in string if isdigit(x)]
    a = numbers[1]
    b = numbers[end]

    total = (10 * a) + b
    global p1 += total
end

println(p1)

# Part 2
p2 = 0
mapping = Dict("one" => 1, "two" => 2, "three" => 3, "four" => 4, "five" => 5, "six" => 6, "seven" => 7, "eight" => 8, "nine" => 9, "1" => 1, "2" => 2, "3" => 3, "4" => 4, "5" => 5, "6" => 6, "7" => 7, "8" => 8, "9" => 9)


for (i, line) in enumerate(data)
    while ! any(startswith(line, string(key)) for key in keys(mapping))
        line = line[2:end]
        
    end
    x = 0
    y = 0
    while ! any(endswith(line,string(key)) for key in keys(mapping))
        line = line[begin:end-1]
        
    end
    for num in keys(mapping)
        if startswith(line,num)
            x = mapping[num]
        end
        if endswith(line,num)
            y = mapping[num]
        end
    end
    global p2 += (x*10) + y
end

println(p2)
