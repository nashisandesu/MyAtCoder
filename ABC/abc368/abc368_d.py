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
N, K = Mi()
node = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = Mi()
    node[a].append(b)
    node[b].append(a)

V = Li()
set_V = set(V)
todo = deque()
todo.append(V[0])
visited = [False] * (N+1)
visited[V[0]] = True
before = [0] * (N+1)
before[V[0]] = -1
ans = set()
ans.add(V[0])
while todo:
    now = todo.popleft()
    if now in set_V:
        check = now
        ans.add(now)
        while True:
            ans.add(check)
            if before[check] == -1:
                break
            elif before[check] not in ans:
                check = before[check]
            else:
                break                

    for next in node[now]:
        if visited[next]:
            continue
        visited[next] = True
        todo.append(next)
        before[next] = now


print(len(ans))