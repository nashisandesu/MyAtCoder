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
N, D, P = Mi()
F = Li()
F.sort(reverse=True)
now = 0
ans = 0
for i in range(0, N):
    now += F[i]
    if (i+1) % D == 0:
        if now > P:
            ans += P
            now = 0
        else:
            ans += now
            now = 0

if now:
    if now > P:
        ans += P
        now = 0
    else:
        ans += now

print(ans)