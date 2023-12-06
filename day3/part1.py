import re
with open("input.txt") as f:
    lines = f.read().splitlines()
validNums = []
noLines = len(lines)
noCol = len(lines[0])
for en,line in enumerate(lines):
    nums = re.finditer(r"\d+",line)
    for num in nums:
        s,e = num.span()
        for i in range(max(en-1,0),min(en+2,noLines)):
            for j in range(max(s-1,0),min(e+1,noCol)):
                char = lines[i][j]
                if re.fullmatch(r"[^\d.]",char):
                    validNums.append(int(num.group()))
            else:
                continue
            break
print(sum(validNums))