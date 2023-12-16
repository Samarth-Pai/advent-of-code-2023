import re
with open("input.txt") as f:
    lines = f.read().splitlines()
instructions = lines[0]
insLen = len(instructions)
nodes = {}
for line in lines[2:]:
    print(line)
    key,left,right = re.findall(r"[A-Z]{3}",line)
    nodes[key] = (left,right)
index = 0
node = "AAA"
while node!="ZZZ":
    ins = instructions[index%insLen]
    node = nodes[node][ins=="R"]
    index+=1
print(index)