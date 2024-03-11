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
N, M = Mi()
route = [[] for _ in range(N+1)]
for i in range(M):
    l, d, k, c, A, B = Mi()
    route[B].append([-(l + (k-1)*d), l, d, k, c, A])

todo = route[N][:]
heapq.heapify(todo)
visit = [0] * (N+1)
visit[N] = 1
ans = ['Unreachable'] * (N+1)
while todo:
    now = heapq.heappop(todo)
    time_start, l, d, k, c, A = now
    if visit[A] == 0:
        visit[A] = 1
        ans[A] = -time_start
        next = route[A][:] #こうしないとnextも更新されてしまう
        for n in next:
            n_time_start, n_l, n_d, n_k, n_c, n_A = n
            if visit[n_A] == 0:
                start = - time_start - n_c
                if n_l <= start:
                    n_time_start = -(n_l + n_d * min(n_k-1, (start - n_l) // n_d))
                    heapq.heappush(todo,[n_time_start, n_l, n_d, n_k, n_c, n_A])               
for i in range(1, N):
    print(ans[i])

