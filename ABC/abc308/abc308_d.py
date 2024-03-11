import sys
sys.setrecursionlimit(10**8)
from collections import deque

H, W = map(int, input().split())


data = [list(input()) for _ in range(H)]
todo = deque([(0, 0)])
dxdy = [(0,1), (0, -1), (1, 0), (-1, 0)]

def check_area(x, y):
    if x == -1 or y == -1 or x == H or y == W:
        return False
    else:
        return True

snuke = list('snuke')
visit = set()
start_i, start_j = (0, 0)
if data[0][0] != snuke[0]:
    print('No')
    exit()

while todo:
    i, j = todo.pop()
    if i == H - 1 and j == W - 1:
        print('Yes')
        exit()
    for dx, dy in dxdy:
        next_i, next_j = i + dx, j + dy
        if check_area(next_i, next_j):
            if data[next_i][next_j] == snuke[(snuke.index(data[i][j]) + 1) % 5]:
                if (next_i, next_j) not in visit:
                    visit.add((next_i, next_j))
                    todo.append((next_i, next_j))
print('No')
