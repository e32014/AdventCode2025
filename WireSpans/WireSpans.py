import heapq
import math
from functools import reduce
from operator import mul

file = open('input.txt')

def find_parent(curr, parents):
    if parents[curr] == curr:
        return curr

    parent = find_parent(parents[curr], parents)
    parents[curr] = parent
    return parent

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1]) **2 + (p1[2] - p2[2])**2)
boxes = []
queue = []
for line in file:
    point = line.strip().split(',')
    point = tuple([int(val) for val in point])
    for i, box in enumerate(boxes):
        heapq.heappush(queue, (dist(point,box), len(boxes), i))
    boxes.append(point)
parents = list(range(len(boxes)))
sizes = [1] * len(boxes)

n = 1000
while True:
    (_, p_a, p_b) = heapq.heappop(queue)
    a = find_parent(p_a, parents)
    b = find_parent(p_b, parents)
    if a == b:
        continue
    if sizes[a] < sizes[b]:
        parents[a] = b
        sizes[b] = sizes[b] + sizes[a]
    else:
        parents[b] = a
        sizes[a] = sizes[b] + sizes[a]
    if sizes[find_parent(p_a, parents)] == len(boxes):
        print(boxes[p_a][0] * boxes[p_b][0])
        break


print(reduce(mul, sorted(sizes, reverse=True)[:3]))