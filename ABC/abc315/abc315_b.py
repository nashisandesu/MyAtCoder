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
M = I()
D = Li()
year = sum(D)
mid = year // 2
for i in range(M):
    if mid > D[i]:
        mid -= D[i]
    elif mid == D[i]:
        print(i + 2, 1)
        break
    else:
        print(i + 1, mid + 1)
        break