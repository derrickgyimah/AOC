f = open(r"AOC/2023/day1/data.txt")
data = f.read()
data = data.split("\n")


total1 = 0
total2 = 0


mapping = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}


# Part 1

for i, string in enumerate(data):
    numbers = [int(x) for x in string if x.isdigit()]
    total1 += numbers[0] * 10 + numbers[-1]
print(total1)


# Part 2
striped_strings = []
for i, string in enumerate(data):
    while not any(string.startswith(str(i)) for i in mapping.keys()):
        string = string[1:]

    while not any(string.endswith(str(i)) for i in mapping.keys()):
        string = string[:-1]

    first_num = 0
    last_num = 0

    for number in mapping.keys():
        if string.startswith(number):
            first_num = mapping.get(number)

        if string.endswith(number):
            last_num = mapping.get(number)

    total2 += (first_num * 10) + last_num
print(total2)
