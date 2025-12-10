import numpy.linalg
import scipy.optimize

file = open('input.txt')
total = 0
for line in file:
    segments = line.strip().split()
    goal = segments[0][1:-1]
    moves = []
    i = 1
    while segments[i].startswith('('):
        moves.append(set([int(val) for val in segments[i][1:-1].split(',')]))
        i+= 1
    consts = [int(val) for val in segments[i][1:-1].split(',')]
    c = [1] * len(moves)
    matrix = [[] for _ in range(len(consts))]
    for move in moves:
        for i in range(len(matrix)):
            if i in move:
                matrix[i].append(1)
            else:
                matrix[i].append(0)
    print(matrix)
    res = scipy.optimize.linprog(c, A_eq=matrix, b_eq=consts, method='highs', integrality=True)
    total += int(res.fun)
print(total)