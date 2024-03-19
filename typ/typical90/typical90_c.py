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
def dfs(x, pre):
    for v in data[x]:
        if v == pre:
            continue
        else:
            dist[v] = dist[x] + 1
            if ans['max_dist'] < dist[v]:
                ans['max_dist'] = dist[v]
                ans['max_node'] = v
            dfs(v, x)

N = I()
data = {i:deque() for i in range(1, N+1)}
for _ in range(N-1):
    A, B = Mi()
    data[A].append(B)
    data[B].append(A)

dist = [float('Inf')] * (N+1)
dist[1] = 0
ans = {'max_dist':0, 'max_node':0}
dfs(1, 0)

dist = [float('Inf')] * (N+1)
dist[ans['max_node']] = 0
dfs(ans['max_node'], 0)
print(ans['max_dist'] + 1)



# def bfs(x):
#     todo = deque((data[x][i], 1) for i in range(len(data[x])))
#     visit[x] = 1
#     while todo:
#         next, cnt = todo.popleft()
#         visit[next] = 1
#         for i in range(len(data[next])):
#             if visit[data[next][i]] == 0:
#                 todo.append((data[next][i], cnt + 1))
#                 visit[data[next][i]] = 1
#     return (next, cnt)


# N = I()
# data = {i:deque() for i in range(1, N+1)}
# for _ in range(N-1):
#     A, B = Mi()
#     data[A].append(B)
#     data[B].append(A)

# #一回目の探索
# visit = [0] * (N+1)
# next, _ = bfs(1)

# #二回目の探索
# visit = [0] * (N+1)
# _, ans = bfs(next)

# print(ans+1)

