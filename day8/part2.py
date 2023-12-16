import re,math
with open("input.txt") as f:
    lines = f.read().splitlines()
instructions = lines[0]
insLen = len(instructions)
nodes = {}
allNode = []
for line in lines[2:]:
    key,left,right = re.findall(r"\w{3}",line)
    if key.endswith("A"):
        allNode.append(key)
    nodes[key] = (left,right)
nodeLen = len(allNode)
indices = []
for node in allNode:
    index = 0
    while not node.endswith("Z"):
        ins = instructions[index%insLen]
        node = nodes[node][ins=="R"]
        index+=1
    indices.append(index)
print(math.lcm(*indices))