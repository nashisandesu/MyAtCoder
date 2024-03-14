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
data = [list(input()) for _ in range(N)]
ans = [0] * N
for i in range(N):
    if i == 0:
        ans[i] = [data[1][0]] + data[0][:-1]
    elif i == N-1:
        ans[i] = data[N-1][1:] + [data[N-2][-1]]
    else:
        ans[i] = [data[i+1][0]] + data[i][1:-1] + [data[i-1][-1]]
for i in range(N):
    print(''.join(ans[i]))
