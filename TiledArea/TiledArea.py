from itertools import combinations

def onLine (px, py, x1, y1, x2, y2):
    product = (x2 - x1) * (py - y1) - (y2 - y1) * (px - x1)
    if abs(product) > 0:
        return False
    elif px < min(x1, x2) or px > max(x1, x2):
        return False
    elif py < min(y1, y2) or py > max(y1, y2):
        return False
    return True

def inPoly(px, py, polygon):
    inside = False
    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % len(polygon)]
        if onLine(px, py, x1, y1, x2, y2):
            return True
        if (py < y1) != (py < y2):
            x_int = (x2 - x1) * (py - y1) / (y2 - y1) + x1
            if px < x_int:
                inside = not inside
    return inside

def ccw(p1, p2, p3):
    res =  (p3[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    if res == 0:
        return res
    elif res > 0:
        return 1
    else:
        return -1

def intersect(p1, p2, p3, p4):
    return ccw(p1, p3, p4) * ccw(p2, p3, p4) < 0 and ccw(p1, p2, p3) * ccw(p1, p2, p4) < 0

def inBox(x1, y1, x2, y2, polygon):
    for px, py in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
        if not inPoly(px, py, polygon):
            return False

    for edge in [((x1, y1), (x2, y1)), ((x2, y1), (x2, y2)), ((x2, y2), (x1, y2)), ((x1, y2), (x1, y1))]:
        for i in range(len(polygon)):
            if intersect(edge[0], edge[1], polygon[i], polygon[(i + 1) % len(polygon)]):
                return False
    return True

file = open('input.txt')

def area(p_a, p_b):
    return (abs(p_a[0] - p_b[0]) + 1) * (abs(p_a[1] - p_b[1]) + 1)
boxes = []
max_area = -1
for line in file:
    box = tuple([int(val) for val in line.strip().split(',')])
    boxes.append(box)

for boxa, boxb in combinations(boxes, 2):
    x1, x2 = (min(boxa[0], boxb[0]), max(boxa[0], boxb[0]))
    y1, y2 = (min(boxa[1], boxb[1]), max(boxa[1], boxb[1]))
    if inBox(x1, y1, x2, y2, boxes):
        vol = area(boxa, boxb)
        if vol > max_area:
            max_area = vol
print(max_area)