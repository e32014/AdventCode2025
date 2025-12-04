file = open('input.txt')
grid = set()
y = 0
for line in file:
    for x, val in enumerate(line.strip()):
        if val == '@':
            grid.add((x,y))
    y += 1
remove = None
removed = 0
while remove is None or len(remove) > 0:
    if remove is not None:
        grid = grid.difference(remove)
        removed += len(remove)

    remove = set()
    for (x, y) in grid:
        ads = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                if (x + dx, y + dy) in grid:
                    ads += 1
        if ads < 4:
            remove.add((x, y))
print(removed)