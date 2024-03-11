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
ans = 0
data = dict()
for i in range(N):
    data.setdefault(A[i], list())
    data[A[i]].append(i)
for v in data.values():
    if len(v) >= 2:
        left = 0
        right = len(v) - 1
        while True:
            if left == right:
                left += 1
                right = len(v) - 1
                if left == len(v) -1:
                    break
            else:
                ans += v[right] - v[left] - 1 - (right - left - 1)
                right -= 1
print(ans)