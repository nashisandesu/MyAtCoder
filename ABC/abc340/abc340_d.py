import sys, bisect
import math
# import numpy as np
from atcoder.lazysegtree import LazySegTree
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
dist = [0] * (N+1)
sum_dist = [0] * (N+1)
data = [0]
for _ in range(N-1):
    data.append(Li())
todo = []
heapq.heappush(todo,(data[1][0], 2))
heapq.heappush(todo,(data[1][1], data[1][2]))
visit = [0] * (N + 1)
visit[1] = 1
while todo:
    dist, stage = heapq.heappop(todo)
    if visit[stage] == 1:
        continue
    else:
        visit[stage] = 1
    if stage == N:
        print(dist)
        break
    A, B, X = data[stage]
    if not visit[stage + 1]:
        heapq.heappush(todo,(dist+A, stage+1))
    if not visit[X]:
        heapq.heappush(todo,(dist+ B, X))