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
A = Li()
M = I()
B = Li()
L = I()
C = Li()
Q = I()
X = Li()

data = {}

for i in range(N):
    for j in range(M):
        for k in range(L):
            data.setdefault(A[i] + B[j] + C[k], 1)

for i in range(Q):
    if X[i] in data:
        print('Yes')
    else:
        print('No')