import re,math
with open("input.txt") as f:
    lines = f.readlines()
gameIds = []
summ = 0
for line in lines:
    gameNo,sets = line.removesuffix("\n").split(":")
    gameNo = int(gameNo.split(" ")[1])
    colorDict = {}
    power = ""
    for sett in re.split("[;,] ",sets):
        noOfCubes,color = sett.strip().split(" ")
        noOfCubes = int(noOfCubes)
        try:
            col = colorDict[color]
            if col<noOfCubes:
                colorDict[color] = noOfCubes
        except:
            colorDict[color] = noOfCubes
    summ+=math.prod(colorDict.values())
print(summ)