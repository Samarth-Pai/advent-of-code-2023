import re
with open("input.txt") as f:
    lines = f.read().splitlines()
points = 0
for en,line in enumerate(lines):
    nums = re.findall(r"Card\s+\d+:([\s\d]+)\|([\s\d]+)",line)
    wins,mine = nums[0]
    wins = wins.split()
    mine = mine.split()
    common = set(wins).intersection(set(mine))
    if common:
        points+=2**(len(common)-1)

print(points)