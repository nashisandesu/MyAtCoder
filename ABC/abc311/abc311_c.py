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
# N = I()
# A = [0] + Li()
# visit = [0] * (N+1)
# for i in range(1, N + 1):
#     if visit[i]:
#         continue
#     now = i
#     ans = [now]
#     root = set()
#     root.add(now)
#     while True:
#         next = A[now]
#         root.add(next)
#         ans.append(next)
#         if len(root) != len(ans):
#             end = ans[-1]
#             flag = 0
#             result = []
#             for a in ans:
#                 if flag:
#                     result.append(a)
#                 else:
#                     if a == end:
#                         flag = 1
#             print(len(result))
#             print(*result)
#             exit()
#         if visit[next]:
#             break
#         else:
#             visit[next] = 1
#         now = next
#     visit[i] = 0

#あらかじめN回移動しておく
N = I()
A = [0] + Li()
now = 1
for _ in range(N): now = A[now]
start = now
ans = [now]
while start != A[now]:
    ans.append(A[now])
    now = A[now]
print(len(ans))
print(*ans)