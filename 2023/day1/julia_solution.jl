# Using readline
f = open(raw"", "r")
data = readlines(f)

for (i,string) in enumerate(data)
    numbers = [x for x in string if isdigit(x)]
    print(numbers)
end
    