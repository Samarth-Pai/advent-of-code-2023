import re
with open("input.txt") as f:
    lines = f.readlines()
gameIds = []
for line in lines:
    gameNo,sets = line.removesuffix("\n").split(":")
    gameNo = int(gameNo.split(" ")[1])
    for sett in re.split("[;,] ",sets):
        noOfCubes,color = sett.strip().split(" ")
        noOfCubes = int(noOfCubes)
        if any([color=="red" and noOfCubes>12,color=="green" and noOfCubes>13,color=="blue" and noOfCubes>14]):
            valid = False
            break
    else:
         gameIds.append(gameNo)
print(sum(gameIds))