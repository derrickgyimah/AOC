from collections import defaultdict
f = open(r"2023\day7\data.txt")
data = f.read()
data = data.replace("A","E").replace("K","D").replace("Q","C").replace("J","1").replace("T","A")
data = data.split("\n")
data = [(x.split()[0],x.split()[1]) for x in data]


five = []
four = []
three_two = []
three_ones = []
two_two_one = []
two_one_one_one = []
ones = []


for i, (x,y) in enumerate(data):
    cards = defaultdict(int)
    for a in x:
        cards[a] += 1
        
    # all five cards have the same label
    if sorted(list(cards.values())) == [5]:
        five.append((x,y))
        
    # four cards have the same label and one card has a different label
    if sorted(list(cards.values())) == [1,4]:
        if "1" in sorted(list(cards.keys())):
            five.append((x,y))
        else:
            four.append((x,y))
            
    # three cards have the same label, and the remaining two cards share a different label 
    if sorted(list(cards.values())) == [2,3]:
        if "1" in sorted(list(cards.keys())):
            five.append((x,y))
        else:
            three_two.append((x,y))
            
    # three cards have the same label, and the remaining two cards are each different
    if sorted(list(cards.values())) == [1,1,3]:
        if "1" in sorted(list(cards.keys())):
            four.append((x,y))
        else:
            three_ones.append((x,y))
            
    #  two cards share one label, two other cards share a second label, and the remaining card has a third label    
    if sorted(list(cards.values())) == [1,2,2]:
        if len([c for c in x if c != "1"]) == 4:
            three_two.append((x,y))
            
        elif len([c for c in x if c != "1"]) == 3:
            four.append((x,y))
        else:
            two_two_one.append((x,y)) 
              
            
    #              
    if sorted(list(cards.values())) == [1,1,1,2]:
        if "1" in sorted(list(cards.keys())):
            three_ones.append((x,y))
        else:
            two_one_one_one.append((x,y))
            
    # all cards' labels are distinct
    if sorted(list(cards.values())) == [1,1,1,1,1]:
        if "1" in sorted(list(cards.keys())):
            two_one_one_one.append((x,y))
        else:
            ones.append((x,y))

ans = 0
number = 1000
for cat in [five, four,three_two,three_ones,two_two_one,two_one_one_one,ones]:
    for i,(x,y) in enumerate(sorted(cat,reverse=True)):
        if cat is five:
            ans += 1000*int(y)
            print(i,y,x,ans)
        else:
            ans += (number-i)*int(y)
            print(number-i,y,x,ans)
    number -= len(cat)
    
print(ans)