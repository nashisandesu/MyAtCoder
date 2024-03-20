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
data = [0] * (N+1)
for _ in range(M):
    a, b = Mi()
    small, big = min(a,b), max(a,b)
    data[big] += 1

cnt = 0
for i in range(1, N+1):
    if data[i] == 1:
        cnt += 1
print(cnt)