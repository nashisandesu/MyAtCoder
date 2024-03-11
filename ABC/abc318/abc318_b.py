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
sheet = [[0]*100 for _ in range(100)]
for i in range(N):
    A, B, C, D = Mi()
    for i in range(A, B):
        for j in range(C, D):
            sheet[i][j] = 1

ans = 0
for i in range(100):
    ans += sum(sheet[i])
print(ans)