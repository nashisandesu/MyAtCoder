import sys, bisect
import math
# import numpy as np
from atcoder.lazysegtree import LazySegTree
from atcoder.segtree import SegTree
from atcoder.dsu import DSU
sys.setrecursionlimit(10**8)
from collections import deque
from itertools import combinations
from itertools import permutations
from itertools import combinations_with_replacement
from itertools import product
import heapq

I = lambda: int(input())
S = lambda: str(input())
Sl = lambda: list(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
H, W = Mi()
grid = [input() for _ in range(H)]
N = I()
rce = [Li() for _ in range(N)]

visit = [[0] * W for _ in range(H)]
potion = [[0] * W for _ in range(H)] 
for h in range(H):
    for w in range(W):
        if grid[h][w] == 'S':
            start = (h, w)
        elif grid[h][w] == 'T':
            end = (h, w)

for i in range(N):
    r, c, e = rce[i]
    potion[r-1][c-1] = e

def check(rest, x, y):
    if 0 <= x < H and 0 <= y < W:
        if grid[x][y] == '#':
            return
        elif (x, y) == end:
            print('Yes')
            exit()
        elif potion[x][y] > -rest:
            rest = -potion[x][y]

        if rest == 0:
            return
        elif - visit[x][y] < - rest:
            visit[x][y] = rest
            heapq.heappush(todo, (rest, x, y))  
    else:
        return          

if potion[start[0]][start[1]] == 0:
    print('No')
else:
    todo = []
    heapq.heappush(todo, (- potion[start[0]][start[1]], start[0], start[1]))
    visit[start[0]][start[1]] = - potion[start[0]][start[1]]
    while todo:
        ene, h_now, w_now = heapq.heappop(todo)
        ene = - (- ene - 1)
        check(ene, h_now + 1, w_now)
        check(ene, h_now - 1, w_now)
        check(ene, h_now, w_now + 1)
        check(ene, h_now, w_now - 1)
    print('No')