with open("test.txt") as f:
    lines = f.read().splitlines()
summ = 0
for line in lines:
    seq = [int(i) for i in line.split()]
    while not all(True if i==0 else False for i in seq):
        summ+=seq[-1]
        seq = [j-i for i,j in zip(seq,seq[1:])]
print(summ)