import sys, bisect
import math
import numpy as np
from atcoder.lazysegtree import LazySegTree
sys.setrecursionlimit(10**8)
from collections import deque
from itertools import combinations
from itertools import permutations

I = lambda: int(input())
S = lambda: str(input())
Sl = lambda: list(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
def min_moves_to_meet(grid, N):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 右、左、下、上
    players = [(i, j) for i in range(N) for j in range(N) if grid[i][j] == 'P']

    queue = deque([(players[0], players[1], 0)])  
    visited = [[0] * (N * N) for _ in range(N*N)]


    while queue:
        (x1, y1), (x2, y2), moves = queue.popleft()

        if (x1, y1) == (x2, y2):
            return moves

        for dx, dy in directions:
            nx1, ny1 = x1 + dx, y1 + dy
            nx2, ny2 = x2 + dx, y2 + dy

            if not (0 <= nx1 < N and 0 <= ny1 < N and grid[nx1][ny1] != '#'):
                nx1, ny1 = x1, y1

            if not (0 <= nx2 < N and 0 <= ny2 < N and grid[nx2][ny2] != '#'):
                nx2, ny2 = x2, y2

            if visited[nx1*N+ny1][nx2*N+ny2] == 0:
                visited[nx1*N+ny1][nx2*N+ny2] = 1
                queue.append(((nx1, ny1), (nx2, ny2), moves + 1))
    return -1

N = I()
data = [Sl() for _ in range(N)]
print(min_moves_to_meet(data, N))