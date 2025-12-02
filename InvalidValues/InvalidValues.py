import re

file = open('input.txt')
total = 0
for ranges in file.readline().strip().split(","):
    span = ranges.split("-")
    minval = int(span[0])
    maxval = int(span[1])
    for val in range(minval, maxval+1):
        res = re.search("^(.+)\\1+$", str(val))
        if res is not None:
            print(val)
            total += val
print(total)