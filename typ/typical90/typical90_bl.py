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
# セグでゴリ押し
# def op(data1, data2):
#     return abs(data1) + abs(data2)

# N, Q = Mi()
# A = [0] + Li()
# data = [0] * (N+1)
# for i in range(1, N + 1):
#     data[i] = A[i] - A[i-1]

# seg = SegTree(op, 0, data)
# for _ in range(Q):
#     l, r, v = Mi()
#     seg.set(l, seg.get(l) + v)
#     if r != N: 
#         seg.set(r + 1, seg.get(r + 1) - v)
#     print(seg.prod(2, N+1))

# 差分だけを計算
N, Q = Mi()
A = Li()
data = [0] * (N)
now = 0
for i in range(1, N):
    data[i] = A[i] - A[i-1]
    now += abs(data[i])

for _ in range(Q):
    l, r, v = Mi()
    if l != 1:
        l_now = data[l-1]
        l_next = data[l-1] + v
        now = now - abs(l_now) + abs(l_next)
        data[l-1] = l_next
    if r != N:
        r_now = data[r]
        r_next = data[r] - v
        now = now - abs(r_now) + abs(r_next)
        data[r] = r_next
    print(now)