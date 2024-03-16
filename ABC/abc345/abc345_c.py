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
s = Sl()
N = len(s)
data = {}
ans = N * (N-1) // 2
for i in range(N):
    data.setdefault(s[i],0)
    data[s[i]] += 1

flag = 0
for key, value in data.items():
    if value > 2:
        flag = 1
        ans -= value * (value-1) // 2

print(ans + flag)
