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
A = [Li() for _ in range(N)]
M = I()
wrong = [[0] * N for _ in range(N)]
ans = float('Inf')
for _ in range(M):
    x, y = Mi()
    wrong[x-1][y-1] = 1
    wrong[y-1][x-1] = 1

for run_list in permutations(range(N), N):
    time = 0
    for i in range(N-1):
        if wrong[run_list[i]][run_list[i+1]]:
            time = float('Inf')
            break
        else:
            time += A[run_list[i]][i]
    time += A[run_list[N-1]][N-1]
    ans = min(ans, time)

if ans == float('Inf'):
    print(-1)
else:
    print(ans)