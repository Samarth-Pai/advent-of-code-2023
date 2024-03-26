from collections import Counter
with open("input.txt") as f:
    lines = f.read().splitlines()
cards = [line.split() for line in lines]
cardDict = {"A":14,"K":13,"Q":12,"J":11,"T":10}
secondOrder = lambda x:-(cardDict.get(x) if not x.isdigit() else int(x))
def sorter(cardSet):
    card,bid = cardSet
    group = Counter(card)
    groupVal = list(group.values())
    maxx = max(groupVal)
    if maxx==5:
        return (1,tuple(map(secondOrder,card)))
    elif maxx==4:
        return (2,tuple(map(secondOrder,card)))
    elif maxx==3:
        if 2 in groupVal:
            return (3,tuple(map(secondOrder,card)))
        else:
            return (4,tuple(map(secondOrder,card)))
    elif maxx==2:
        if groupVal.count(2)==2:
            return (5,tuple(map(secondOrder,card)))
        else:
            return (6,tuple(map(secondOrder,card)))
    else:
        return (7,tuple(map(secondOrder,card)))
summ = 0
for en,cardSet in enumerate(sorted(cards,key=sorter,reverse=True),1):
    summ+=int(cardSet[1])*en
print(summ)