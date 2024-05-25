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
N, T = Mi()
A = Li()
tate = [0] * N
yoko = [0] * N
naname1, naname2 = 0, 0
for i in range(T):
    t = (A[i] - 1) // N
    y = (A[i] - 1) % N
    tate[t] += 1
    yoko[y] += 1
    if t == y:
        naname1 += 1
    if t + y == N - 1:
        naname2 += 1
    if N in [tate[t], yoko[y], naname1, naname2]:
        print(i+1)
        break
else:
    print(-1)