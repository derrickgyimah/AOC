import re
f = open(r"2023\day3\data.txt")
data = f.read()
data = data.split("\n")

# data = ["467..114..",
# "...*......",
# "..35..633.",
# "......#...",
# "617*......",
# ".....+.58.",
# "..592.....",
# "......755.",
# "...$.*....",
# ".664.598.."]

new_data = []
for row in data:
    row = str(".")+row+str(".")
    new_data.append(row)

new_data.insert(0,"."*145)
new_data.insert(len(data),"."*142)
new_data.insert(len(data),"."*142)

data = new_data


ans1 = 0
ans2 = 0

symbols = []
for i,row in enumerate(data):
    for string in row:
        if (not string.isdigit()) and (string != ".") and (string not in symbols):
            symbols.append(string)

pattern = r'\d+'

all_numbers = []
for i,row in enumerate(data):
        numbers = re.findall(pattern,row)
        all_numbers.append(numbers)


for i,row in enumerate(all_numbers,start=0):
     for x, number in enumerate(row):
        index = data[i].index(str(number))-1
        length = len(number)+2
        above_row = [x for x in data[i-1][index:index+length]]
        same_row = [x for x in data[i][index:index+length]]
        try:
            below_row = [x for x in data[i+1][index:index+length]]
        except:
            pass
     
        surrounding_elements = same_row + above_row + below_row
        surrounding_elements = list(set(surrounding_elements) & set(symbols))
        if surrounding_elements != []:
            ans1 += int(number)
print(ans1)
