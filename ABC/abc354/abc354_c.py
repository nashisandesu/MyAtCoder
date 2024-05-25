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
data = []
for i in range(N):
    a, c = Mi()
    heapq.heappush(data, (-a, c, i+1))

ans = []
min_cost = float('Inf')
for i in range(N):
    a,c,idx = heapq.heappop(data)
    if c < min_cost:
        ans.append(idx)
        min_cost = c

ans.sort()
print(len(ans))
print(*ans)

