import sys, bisect
import math
# import numpy as np
from atcoder.lazysegtree import LazySegTree
from atcoder.segtree import SegTree
from atcoder.dsu import DSU
sys.setrecursionlimit(10**8)
from collections import deque
from collections import defaultdict
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
INF = float('Inf')
N, M = Mi()
bridges = []
cost = [[INF] * N for _ in range(N)]
for i in range(M):
    u, v, t = Mi()
    u -= 1
    v -= 1
    cost[u][v] = min(t, cost[u][v])
    cost[v][u] = min(t, cost[u][v])
    bridges.append((u, v, t))

for i in range(N):
    cost[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if cost[i][k] != INF and cost[k][j] != INF:
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
Q = I()
for _ in range(Q):
    K = I()
    B = Li()
    ans = INF
    for route in permutations(B, K):
        for i in range(1 << K):
            now = 0
            cnt = 0
            for j in range(K):
                u, v, t = bridges[route[j]-1]
                if i >> j & 1:
                    cnt += cost[now][u]
                    cnt += t
                    now = v
                else:
                    cnt += cost[now][v]
                    cnt += t
                    now = u
            cnt += cost[now][N-1]
            ans = min(ans, cnt)
    print(ans)