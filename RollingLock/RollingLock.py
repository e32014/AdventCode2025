file = open("input.txt")

curr = 50
at_zero = 0

for line in file:
    dir = line.strip()[0]
    num = int(line.strip()[1:])
    print(dir, num, curr)
    for i in range(0, num):
        curr += 1 if dir == 'R' else -1
        curr = curr % 100
        if curr == 0:
            at_zero += 1

print(at_zero)