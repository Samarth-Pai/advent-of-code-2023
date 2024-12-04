with open("input.txt") as f:
    lines = f.read().splitlines()
    
# Considering clockwise
# successors = {"F": ["-", "|"], "-": "7", "7": "|", "|": "J", "J": "-", "L": "|"}
for en1, line in enumerate(lines):
    if "S" in line:
        x, y = en1, line.index("S")
initialX, initialY = x, y
        
direction = None
steps = 0
nRows, nCols = len(lines), len(lines[0])

if x>0:
    if lines[x-1][y] == "7":
        x-=1
        direction = "w"
    elif lines[x-1][y] == "F":
        x-=1
        direction = "e"
    elif lines[x-1][y] == "|":
        x-=1
        direction = "n"
        
if direction is None and y<nCols-2:
    if lines[x][y+1] == "J":
        y+=1
        direction = "n"
    elif lines[x][y+1] == "7":
        y+=1
        direction = "s"
    elif lines[x][y+1] == "-":
        y+=1
        direction = "e"

if direction is None and x<nRows-2:
    if lines[x+1][y] == "J":
        x+=1
        direction = "w"
    elif lines[x+1][y] == "L":
        x+=1
        direction = "e"
    elif lines[x+1][y] == "|":
        x+=1
        direction = "s"
        
if direction is None and y>0:
    if lines[x][y-1] == "L":
        y-=1
        direction = "n"
    elif lines[x][y-1] == "F":
        y-=1
        direction = "s"
    elif lines[x][y-1] == "=":
        y-=1
        direction = "w"
        
while True:
    if direction == "n":
        if lines[x-1][y] == "F":
            direction = "e"
        elif lines[x-1][y] == "7":
            direction = "w"
        x-=1
    elif direction == "e":
        if lines[x][y+1] == "J":
            direction = "n"
        elif lines[x][y+1] == "7":
            direction = "s"
        y+=1
    elif direction == "s":
        if lines[x+1][y] == "L":
            direction = "e"
        elif lines[x+1][y] == "J":
            direction = "w"
        x+=1
    else:
        if lines[x][y-1] == "L":
            direction = "n"
        elif lines[x][y-1] == "F":
            direction = "s"
        y-=1
    steps+=1
    if x == initialX and y == initialY:
        break
    
ans = steps//2 + 1
print(ans)