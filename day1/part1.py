with open("input.txt") as f:
    inp = f.readlines()
summ = 0
for s in inp:
    digits = [i for i in s if i.isdigit()]
    firstDigit,lastDigit = digits[0],digits[-1]
    num = int(firstDigit+lastDigit)
    summ+=num
print(summ)