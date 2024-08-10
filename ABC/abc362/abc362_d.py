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
A = Li()
path = defaultdict(list)
for _ in range(M):
    u, v, b = Mi()
    path[u-1].append((v-1, b))
    path[v-1].append((u-1, b))

visited = [False] * N
node_cost = [float('inf')] * N
node_cost[0] = A[0]
todo = []
heapq.heappush(todo, (A[0], 0))
while todo:
    cost, node = heapq.heappop(todo)
    if visited[node]:
        continue
    visited[node] = True
    for next_node, b in path[node]:
        if visited[next_node]:
            continue
        if node_cost[next_node] > cost + b + A[next_node]:
            node_cost[next_node] = cost + b + A[next_node]
            heapq.heappush(todo, (node_cost[next_node], next_node))

print(*node_cost[1:])