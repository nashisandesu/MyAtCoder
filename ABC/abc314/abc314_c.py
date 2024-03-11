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
S = list(input())
C = Li()
data = {}
for i in range(1, M+1):
    data[i] = deque()
for i in range(N):
    data[C[i]].append(S[i])

for i in range(1, M+1):
    last = data[i].pop()
    data[i].appendleft(last)

ans = []
for i in range(N):
    now = data[C[i]].popleft()
    ans.append(now)
print(''.join(ans))