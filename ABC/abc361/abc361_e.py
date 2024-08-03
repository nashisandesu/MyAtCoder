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
from collections import deque

def bfs(s):
    dist = [None] * N
    todo = deque([s])
    dist[s] = 0
    while todo:
        v = todo.popleft()
        d = dist[v]
        for w, c in G[v]:
            if dist[w] is not None:
                continue
            dist[w] = d + c
            todo.append(w)
    d = max(dist)
    return dist.index(d), d

N = int(input())

G= [[] for _ in range(N)] 

ans = 0
for _ in range(N-1):
    a, b, c = Mi()
    a -= 1
    b -= 1
    G[a].append((b, c))
    G[b].append((a, c))  
    ans += c

u, _ = bfs(0)
v, d = bfs(u)

print(ans * 2 - d)
print(d)