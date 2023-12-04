f = open(r"2023\day2\data.txt")
data = f.read()
data = data.split("\n")


ans1 = 0
ans2 = 0

red = 12
green = 13
blue = 14

colours = ["red", "green", "blue"]

all_scores = []
for i, game in enumerate(data):
    rounds = game.split(":")[1].split(";")
    games_played = len(data[i].split(":")[1].split(";"))
    reds = [0]
    greens = [0]
    blues = [0]
    for x in range(games_played):
        for colour in colours:
            if colour in rounds[x]:
                index = int(rounds[x].index(colour))
                current_colour = int(
                    "".join(
                        [str(rounds[x][index - 3]), str(rounds[x][index - 2])]
                    ).strip()
                )
                if colour == "red":
                    reds += [current_colour]
                if colour == "green":
                    greens += [current_colour]
                if colour == "blue":
                    blues += [current_colour]
                print(current_colour)
    all_scores.append((max(reds), max(greens), max(blues)))


for i,j in enumerate(all_scores):
    if red>=j[0] and green >=j[1] and blue >= j[2]:
        ans1 += i+1 
print(ans1)


for i,j in enumerate(all_scores):
    ans = j[0]*j[1]*j[2]
    ans2 += ans

print(ans2) 