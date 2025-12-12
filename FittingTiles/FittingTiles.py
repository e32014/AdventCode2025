import re
from collections import defaultdict

file = open('input.txt')

shapes = defaultdict(list)
problems = []
consume = False
curr_shape = 0
shape_end = False
for line in file:
    if not consume and not shape_end:
        check = re.match('^(\\d+):', line.strip())
        if check:
            consume = True
            curr_shape = check.group(1)
        else:
            shape_end = True
            problems.append(line.strip())
    elif consume and line.strip() == '':
        consume = False
    elif consume and line.strip() != '':
        shapes[curr_shape].append(line.strip())
    elif shape_end:
        problems.append(line.strip())

print(shapes)

shape_volumes = dict()
for key, value in shapes.items():
    total = 0
    for row in value:
        total += sum([1 if val == '#' else 0 for val in row])
    shape_volumes[int(key)] = total
total = 0
for problem in problems:
    space, tiles = problem.split(': ')
    x_max, y_max = [int(val) for val in space.split('x')]
    tiles = [int(val) for val in tiles.split(' ')]
    total_volume = x_max  * y_max
    req_volume  = sum([shape_volumes[i] * val for i, val in enumerate(tiles)])
    total += 1 if req_volume <= total_volume else 0
print(total)