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
B = Li()
C = Li()
data_A = {i:0 for i in range(46)}
data_B = {i:0 for i in range(46)}
data_C = {i:0 for i in range(46)}

for i in range(N):
    data_A[A[i]%46] += 1
    data_B[B[i]%46] += 1
    data_C[C[i]%46] += 1

ans = 0

for i in range(46):
    for j in range(46):
        ans += data_A[i] * data_B[j] * data_C[(46 * 2 - i - j) % 46]

print(ans)