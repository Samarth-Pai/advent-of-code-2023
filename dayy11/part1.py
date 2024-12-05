import numpy as np
from itertools import combinations
with open("input.txt") as f:
    lines = f.read().splitlines()

lines = np.array([list(s) for s in lines])
m, n = lines.shape

def colIsEmpty(y):
    return all(c=="." for c in lines[:, y])

def rowIsEmpty(x):
    return all(c=="." for c in lines[x])

def findDist(c1, c2):
    return abs(c2[0] - c1[0]) + abs(c2[1] - c1[1])

# Double all empty columns
j = 0
while j<n:
    if colIsEmpty(j):
        lines = np.insert(lines, j+1, ".", axis = 1)
        j+=1
        n+=1
    j+=1
# Double all empty rows
i = 0
while i<m:
    if rowIsEmpty(i):
        lines = np.insert(lines, i+1, ".", axis = 0)
        i+=1
        m+=1
    i+=1
    
galaxies = [(i, j) for j in range(n) for i in range(m) if lines[i][j] == "#"]
galaxyCombs = list(combinations(galaxies, 2))
distSum = sum(findDist(c1, c2) for c1, c2 in galaxyCombs)
print(distSum)