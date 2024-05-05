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
from itertools import combinations_with_replacement
from itertools import product
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
data = [Li() for _ in range(N)]
sum_A, sum_B = 0, 0
for i in range(N):
    sum_A += data[i][0]
    sum_B += data[i][1]
ans = 0
for i in range(N):
    ans = max(ans, sum_A - data[i][0] + data[i][1])
print(ans)