from functools import cache

file = open('input.txt')

graph = dict()

@cache
def num_paths(node, hadFFT, hadDAC):
    if node == "out":
        return 1 if hadFFT and hadDAC else 0
    total = 0
    for next in graph[node]:
        total += num_paths(next, True if node == 'fft' else hadFFT, True if node == 'dac' else hadDAC)
    return total

for line in file:
    tokens = line.strip().split()
    graph[tokens[0][:-1]] = tokens[1:]

print(num_paths("svr", False, False))