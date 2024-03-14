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
N, M = Mi()
C = Ls()
D = Ls()
p0, *p = Li()
data = {}
for i in range(M):
    data[D[i]] = p[i]
ans = 0
for i in range(N):
    if C[i] not in data:
        ans += p0
    else:
        ans += data[C[i]]
print(ans)