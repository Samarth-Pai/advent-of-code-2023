import re
with open("input.txt") as f:
    lines = re.split(r"\n+",f.read().rstrip("\n"))
seedsToFind = [(int(seed),int(seed)+int(lenn)) for seed,lenn in re.findall(r"(\d+) (\d+)",lines[0])]
mappa = {}
group = []
for en,line in enumerate(lines[1:],2):
    if mat:=re.match(r"([a-z]+-to-[a-z]+)",line):
        groupName = mat.group()
        group = mappa[groupName] = []
    else:
        dest,sour,rng = map(int,re.findall(r"\d+",line))
        group.append((sour,dest,rng))
def mapper(seed,end,sowedSeeds,rngs):
    for src,dest,lenn in rngs:
        ovlpStart = max(seed,src)
        ovlpEnd = min(end,src+lenn)
        if ovlpStart<ovlpEnd:
            sowedSeeds.append((ovlpStart-src+dest,ovlpEnd-src+dest))
            if seed<ovlpStart:
                seeds.append((seed,ovlpStart))
            if ovlpEnd<end:
                seeds.append((ovlpEnd,end))
            break
    else:
        sowedSeeds.append((seed,end))

seeds = seedsToFind.copy()
for conv,rngs in mappa.items():
    sowedSeeds =[]
    while len(seeds)>0:
        seed,end = seeds.pop()
        mapper(seed,end,sowedSeeds,rngs)
    seeds = sowedSeeds
print(min(seeds)[0])