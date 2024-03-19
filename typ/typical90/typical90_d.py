import sys, bisect
import math
import numpy as np
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
data = [Li() for _ in range(H)]
h_data = [0] * H
w_data = [0] * W
for h in range(H):
    for w in range(W):
        h_data[h] += data[h][w]

for w in range(W):
    for h in range(H):
        w_data[w] += data[h][w]

for h in range(H):
    ans = []
    for w in range(W):
        ans.append(h_data[h] + w_data[w] - data[h][w])
    print(*ans)