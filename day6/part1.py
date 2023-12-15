with open("input.txt") as f:
    lines = f.read().splitlines()
time = map(int,lines[0].split()[1:])
distance = map(int,lines[1].split()[1:])
prodOfWins = 1
for t,d in zip(time,distance):
    wins = 0
    for i in range(1,t//2+1):
        speed = i
        tLeft = t-i
        wins+=speed*tLeft>d
    wins*=2
    wins-=not t%2
    prodOfWins*=wins
print(prodOfWins)