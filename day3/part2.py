import re
with open("input.txt") as f:
    lines = f.read().splitlines()
noLines = len(lines)
noCol = len(lines[0])
allPairs = []
for en,line in enumerate(lines):
    syms = re.finditer(r"[^\d.]",line)
    for sym in syms:
        s,e = sym.span()
        pairs = []
        for i in range(max(en-1,0),min(en+2,noLines)):
            for j in range(max(s-1,0),min(e+1,noCol)):
                char = lines[i][j]
                if re.fullmatch(r"\d",char):
                    for poss in re.finditer(r"\d+",lines[i]):
                        if j in range(*poss.span()):
                            if [poss.group(),i] not in pairs:
                                pairs.append([poss.group(),i])
        pairs = [i for i,j in pairs]
        if len(pairs)==2:
            allPairs.append(pairs)
print(sum(int.__mul__(*map(int,pair)) for pair in allPairs))