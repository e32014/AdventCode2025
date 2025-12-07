from collections import defaultdict
from functools import lru_cache

file = open('input.txt')
splitters = set()
graph = dict()

def find_nexts(starter: tuple[int, int], known: set[tuple[int, int]], max_y: int) -> list[tuple[int, int]]:
    r_val = []
    (s_x, s_y) = starter
    iterator = 0
    while (s_x - 1, s_y+iterator) not in known and s_y + iterator < max_y:
        iterator += 1
    if (s_x - 1, s_y + iterator) in known:
        r_val.append((s_x -1, s_y + iterator))
    else:
        r_val.append((s_x - 1, max_y))
    iterator = 0
    while (s_x + 1, s_y+iterator) not in known and s_y + iterator < max_y:
        iterator += 1
    if (s_x + 1, s_y + iterator) in known:
        r_val.append((s_x + 1, s_y + iterator))
    else:
        r_val.append((s_x + 1, max_y))
    return r_val

@lru_cache
def walk_graph(curr: tuple[int, int]) -> int:
    if curr not in graph or len(graph[curr]) == 0:
        return 1
    total = 0
    for adjs in graph[curr]:
        total += walk_graph(adjs)
    return total

start = (0,0)
for y, line in enumerate(file):
    for x, val in enumerate(line.strip()):
        if val == 'S':
            start = (x, y)
        if val == '^':
            splitters.add((x, y))

max_y = y

for i, split in enumerate(splitters):
    graph[split] = find_nexts(split, splitters, max_y)

(s_x, s_y) = start
iterator = 0
while (s_x, s_y+iterator) not in splitters and s_y + iterator < max_y:
    iterator += 1
if (s_x, s_y + iterator) in splitters:
    graph[start] = [(s_x, s_y + iterator)]

print(walk_graph(start))