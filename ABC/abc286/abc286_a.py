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
N, P, Q, R, S = Mi()
b = [0] + Li()

ans = b[1:P] + b[R:S+1] + b[Q+1:R] + b[P:Q+1] + b[S+1:]
print(*ans)

#天才
# A = Li()
# A[P - 1 : Q], A[R - 1 : S] = A[R - 1 : S], A[P - 1 : Q]
# print(*A)