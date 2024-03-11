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
N = I()
A = Li()
Q = I()
query = [Li() for _ in range(Q)]
data = {}
for i in range(N):
    if i == 0:
        if N == 1:
            data[A[i]] = [-1, -1]
        else:
            data[A[i]] = [-1, A[i+1]]
        first = A[i]
    elif i == N-1:
        data[A[i]] = [A[i-1], -1]
    else:
        data[A[i]] = [A[i-1], A[i+1]]

for i in range(Q):
    if query[i][0] == 1:
        _, x, y = query[i]
        pre, next = data[x]
        data[x] = [pre, y]
        data[y] = [x, next]
        if next != -1:
            data[next][0] = y 
    else:
        _, x = query[i]
        pre, next = data[x]
        del data[x]
        if pre == -1:
            data[next][0] = -1
            first = next
        elif next == -1:
            data[pre][1] = -1
        else:
            data[pre][1] = next
            data[next][0] = pre
now = first
ans = [now]
while True:
    pre, next = data[now]
    if next == -1:
        break
    else:
        ans.append(next)
        now = next

print(*ans)