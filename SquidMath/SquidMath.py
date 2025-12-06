file = open('input.txt')
grid = []
for line in file:
    grid.append(line.strip('\n'))
grand_sum = 0
equations = []
while '+' in grid[-1] or '*' in grid[-1]:
    next_add = grid[-1].find('+', 1)
    next_mult = grid[-1].find('*', 1)
    next_pos = 0
    equation = [grid[-1][0]]
    if next_add == -1 and next_mult != -1:
        next_pos = next_mult
    elif next_mult == -1 and next_add != -1:
        next_pos = next_add
    elif next_mult == -1 and next_add == -1:
        for row in grid[:-1]:
            equation.append(row)
        equations.append(equation)
        break
    else:
        next_pos = min(next_add, next_mult)
    for num, row in enumerate(grid[:-1]):
        equation.append(row[:next_pos-1])
        grid[num] = row[next_pos:]
    grid[-1] = grid[-1][next_pos:]
    equations.append(equation)

for equation in equations:
    op = equation[0]
    max_val = -1
    for val in equation[1:]:
        max_val = max(max_val, len(val))
    total = 0 if op == '+' else 1
    for i in range(max_val):
        num = 0
        for val in equation[1:]:
            if len(val) <= i:
                continue
            elif val[i] == ' ':
                continue
            else:
                num = num * 10 + int(val[i])
        if op == '+':
            total += num
        else:
            total *= num
    grand_sum += total
print(grand_sum)