import re
with open("input.txt") as f:
    inp = f.readlines()
summ = 0
searches = [*map(str,range(1,10)),"one","two","three","four","five","six","seven","eight","nine"]
for line in inp:
    results = []
    for search in searches:
        for res in re.finditer(search,line):
            results.append((res.span(),search))
    num = int(str(searches.index(min(results)[1])%9+1)+str(searches.index(max(results)[1])%9+1))
    summ+=num
print(summ)