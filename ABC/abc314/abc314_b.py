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
cost = {}
for i in range(37):
    cost[i] = []
for i in range(N):
    C = I()
    A = Li()
    for a in A:
        cost[a].append((C, i+1))
X = I()

target = cost[X]
heapq.heapify(target)
try:
    mincost = heapq.heappop(target)
except:
    print(0)
    print()
    exit()
ans = [mincost[1]]

while target:
    p = heapq.heappop(target)
    if p[0] == mincost[0]:
        ans.append(p[1])
    else:
        break
print(len(ans))
print(*ans)