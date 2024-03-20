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
A = [Li() for _ in range(H)]
B = [Li() for _ in range(H)]
if H > W:
    sa = [[0] * H for _ in range(W)]
    for h in range(H):
        for w in range(W):
            sa[w][h] = B[h][w] - A[h][w]
    temp = H
    H = W
    W = temp
else:
    sa = [[0] * W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            sa[h][w] = B[h][w] - A[h][w]
cnt = 0
for i in range(H-1):
    for j in range(i):
        yoko = sa[i][j]
        sa[i][j] = 0
        sa[i][j+1] -= yoko
        sa[i+1][j] -= yoko
        sa[i+1][j+1] -= yoko
        cnt += abs(yoko)

        tate = sa[j][i]
        sa[j][i] = 0
        sa[j][i+1] -= tate
        sa[j+1][i] -= tate
        sa[j+1][i+1] -= tate
        cnt += abs(tate)
    mid = sa[i][i]
    sa[i][i] = 0
    sa[i][i+1] -= mid
    sa[i+1][i] -= mid
    sa[i+1][i+1] -= mid
    cnt += abs(mid)

for i in range(H-1):
    if sa[H-1][i] != 0:
        print('No')
        exit()
for i in range(H-1, W-1):
    for j in range(H-1):
        tate = sa[j][i]
        sa[j][i] = 0
        sa[j][i+1] -= tate
        sa[j+1][i] -= tate
        sa[j+1][i+1] -= tate
        cnt += abs(tate)
    if sa[H-1][i] != 0:
        print('No')
        exit()
for i in range(H):
    if sa[i][W-1] != 0:
        print('No')
        exit()
print('Yes')
print(cnt)