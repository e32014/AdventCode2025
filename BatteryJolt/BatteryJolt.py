import itertools

file = open('input.txt')
total = 0

for line in file:
    max_val = 0
    depth = 12
    curr_str = line.strip()
    next_str = ''
    curr = 0
    while depth > 0:
        for pos, val in enumerate(curr_str[0:len(curr_str) - depth + 1]):
            if curr * 10 + int(val) > max_val:
                max_val = curr * 10 + int(val)
                next_str = curr_str[pos + 1:]
        depth -= 1
        curr = max_val
        curr_str = next_str
    print(max_val)
    total += max_val
print(total)