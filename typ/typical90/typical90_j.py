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
N = I()
data = [[0] * (N+1) for _ in range(2)]
for i in range(N):
    c, p = Mi()
    if c == 1:
        data[0][i+1] = data[0][i] + p
        data[1][i+1] = data[1][i]
    else:
        data[0][i+1] = data[0][i]
        data[1][i+1] = data[1][i] + p
Q = I()
for _ in range(Q):
    l, r = Mi()
    print(data[0][r]-data[0][l-1],data[1][r]-data[1][l-1])