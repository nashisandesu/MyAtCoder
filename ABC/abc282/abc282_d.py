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
N, M = Mi()
edges = [[] for _ in range(N)]
for _ in range(M):
    a, b = Mi()
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

def dfs(v, c):
    visited[v] = c
    count_color[c] += 1
    for nv in edges[v]:
        if visited[nv] == c:
            return False
        if visited[nv] == 0 and not dfs(nv, -c):
            return False
    return True

ans = N * (N-1) // 2
visited = [0] * N
for i in range(N):
    if visited[i] == 0:
        count_color = {1: 0, -1: 0}
        if not dfs(i, 1):
            print(0)
            exit()
        ans -= count_color[1] * (count_color[1]-1) // 2
        ans -= count_color[-1] * (count_color[-1]-1) // 2
print(ans-M)