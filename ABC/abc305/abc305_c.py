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
data = [Sl() for _ in range(H)]
data2 = [[data[h][w] for h in range(H)] for w in range(W)]

cookie = [0, 0]
for h in range(H):
    cookie[0] = max(cookie[0], data[h].count('#'))

for w in range(W):
    cookie[1] = max(cookie[1], data2[w].count('#'))

for h in range(H):
    if data[h].count('#') == cookie[0] - 1:
        print(h + 1, end = ' ')
        break
for w in range(W):
    if data2[w].count('#') == cookie[1] - 1:
        print(w + 1)
        break

