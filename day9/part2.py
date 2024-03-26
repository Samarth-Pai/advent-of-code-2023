with open("input.txt") as f:
    lines = f.read().splitlines()
summ = 0
for line in lines:
    firstVals = []
    seq = [int(i) for i in line.split()]
    while not all(True if i==0 else False for i in seq):
        firstVals.append(seq[0])
        seq = [j-i for i,j in zip(seq,seq[1:])]
    diff = 0
    for val in reversed(firstVals):
        diff = val - diff
    summ+=diff
print(summ)