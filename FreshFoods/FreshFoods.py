import heapq

file = open('input.txt')

ranges = []
fed = False
count = 0
for line in file:
    if line == '\n':
        fed = True
        continue
    if not fed:
        ends = line.strip().split("-")
        ranges.append((int(ends[0]), int(ends[1])))
    else:
        val = int(line.strip())
        for (min_val, max_val) in ranges:
            if min_val <= val <= max_val:
                count += 1
                break
print(count)
heapq.heapify(ranges)
solid_ranges = []
while len(ranges) > 0:
    if len(ranges) == 1:
        solid_ranges.append(heapq.heappop(ranges))
    elif len(ranges) > 1:
        (min_1, max_1) = heapq.heappop(ranges)
        (min_2, max_2) = heapq.heappop(ranges)
        if min_1 < min_2 and max_1 < min_2:
            solid_ranges.append((min_1, max_1))
            heapq.heappush(ranges, (min_2,max_2))
        elif  max_1 <= max_2:
            heapq.heappush(ranges, (min_1, max_2))
        elif  max_1 >= max_2:
            heapq.heappush(ranges, (min_1, max_1))

total = 0
for (min_val, max_val) in solid_ranges:
    total += max_val - min_val + 1
print(total)