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
A.sort()
Q = I()
ans = []
for _ in range(Q):
    b = I()
    idx = bisect.bisect_left(A, b)
    if idx == 0:
        ans.append(A[idx] - b)
    elif idx == N:
        ans.append(b - A[N-1])
    else:
        l, r = idx - 1, idx
        ans.append(min(A[r]-b, b-A[l]))
for i in range(Q):
    print(ans[i])
