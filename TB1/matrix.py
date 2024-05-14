import re

def matrix():
    with open('matrix.txt', 'r') as file:
        n, m = map(int, file.readline().split())
        matrix = [list(file.readline().strip().ljust(m, ' ')) for _ in range(n)]
    decoded = ''.join([''.join(item) for item in zip(*matrix)])
    print(re.sub(r'\b[^a-zA-Z0-9]+\b', r' ', decoded))

matrix()