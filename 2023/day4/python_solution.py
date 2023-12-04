import re
from collections import defaultdict
f = open(r"C:\Users\dggyi\Documents\adventofcode\day4\data.txt")
data = f.read()
data = data.split("\n")

ans1 = 0
ans2 = 0

all_wins = []
total2 = 0
cards = defaultdict(int)
for i, row in enumerate(data,start=1):
    cards[i] += 1
    num = [int(x) for x in re.findall(r"-?\d+", row)]
    game = num[0]
    my_cards = num[1:11]
    all_nums = num[11:]
    
    winning_nums = 0
    for x, number in enumerate(my_cards):
        if number in all_nums:
            winning_nums += 1
        if winning_nums == 0:
            score = 0
        else:
            score = 2**(winning_nums-1)
        #print(winning_nums)
    for n in range(winning_nums):
        cards[i+n+1] += cards[i]
    ans1 += score

ans2 = sum(cards.values())

print(ans1)
print(ans2)

   


