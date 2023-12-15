import re
with open("test.txt") as f:
    lines = re.split(r"\n+",f.read().rstrip("\n"))
seedsToFind = map(int,re.findall(r"\d+",lines[0]))
mappa = {}
group = []
for en,line in enumerate(lines[1:],2):
    if mat:=re.match(r"([a-z]+-to-[a-z]+)",line):
        groupName = mat.group()
        group = mappa[groupName] = []
    else:
        dest,sour,rng = map(int,re.findall(r"\d+",line))
        group.append((sour,dest,rng))

locs = []
for seed in seedsToFind:
    loc = seed
    for conv,rngs in mappa.items():
        for rng in rngs:
            print(loc,rng)
            if rng[0]<=loc<rng[0]+rng[2]:
                loc+=rng[1]-rng[0]
                break
    locs.append(loc)
print(min(locs))