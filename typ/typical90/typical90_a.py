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
def check(x):
    now = 0
    cnt = 0
    for i in range(N + 1):
        if A[i] - now >= x:
            cnt += 1
            now = A[i]
    return (cnt >= K + 1)

N, L = Mi()
K = I()
A = Li() + [L]
ans_max = L // (K + 1)

l = 0
r = ans_max + 1

while (r - l > 1):
    mid = (l + r) // 2
    if check(mid):
        l = mid
    else:
        r = mid

print(l)