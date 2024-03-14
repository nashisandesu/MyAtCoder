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
N, D = Mi()
s = [list(input()) for _ in range(N)]
ans = 0
now = 0
for i in range(D):
    for j in range(N):
        if s[j][i] == 'x':
            now = 0
            break
    else:
        now += 1
        ans = max(ans, now)
print(ans)
