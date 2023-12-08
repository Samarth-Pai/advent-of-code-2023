import re
with open("input.txt") as f:
    lines = f.read().splitlines()
cardPoints = {}
instances = 0
def hover(cards):
    global instances
    for card in cards:
        cardInfo = cardPoints[card]
        instances+=1
        hover(cardInfo[1])

for en,line in enumerate(lines):
    nums = re.findall(r"Card\s+\d+:([\s\d]+)\|([\s\d]+)",line)
    wins,mine = nums[0]
    wins = wins.split()
    mine = mine.split()
    common = set(wins).intersection(set(mine))
    noMatches = len(common)
    cardPoints[en+1] = (noMatches,[*range(en+2,en+noMatches+2)])
hover([*range(1,en+2)])
print(instances)