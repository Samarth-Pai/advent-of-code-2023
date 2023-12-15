import re
with open("input.txt") as f:
    lines = f.read().splitlines()
time,distance = (int("".join(re.findall(r"\d+",line))) for line in lines)
wins = 0
for i in range(time//2+1):
    speed = i
    tLeft = time-i
    wins+=speed*tLeft>distance
print(wins*2-(not time%2))