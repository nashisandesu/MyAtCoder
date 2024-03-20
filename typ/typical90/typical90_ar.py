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
# dequeでゴリ押し
# N, Q = Mi()
# A = Li()
# A = deque(A)
# for _ in range(Q):
#     t, x, y = Mi()
#     if t == 1:
#         temp = A[x-1]
#         A[x-1] = A[y-1]
#         A[y-1] = temp
#     elif t == 2:
#         temp = A.pop()
#         A.appendleft(temp)
#     else:
#         print(A[x-1])

#見かけ上の変化
N, Q = Mi()
A = Li()
slide = 0
for _ in range(Q):
    t, x, y = Mi()
    if t == 1:
        x = (x - 1 - slide) % N
        y = (y - 1 - slide) % N
        temp = A[x]
        A[x] = A[y]
        A[y] = temp
    elif t == 2:
        slide += 1
    else:
        x = (x - 1 - slide) % N
        print(A[x])
