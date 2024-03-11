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
road = [[-1] * (N+1) for _ in range(N + 1)]
visit = [0]*(N+1)

ans = 0

def dfs(now, cost):
    global ans
    visit[now] = 1
    for i in range(1, N+1):
        if visit[i] == 0 and road[now][i] != -1:
            dfs(i, cost + road[now][i])
    else:
        if cost > ans:
            ans = cost
    visit[now] = 0
    
for _ in range(M):
    A, B, C = Mi()
    road[A][B] = C
    road[B][A] = C

for i in range(1, N + 1):
    dfs(i, 0)

print(ans)