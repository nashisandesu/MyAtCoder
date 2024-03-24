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
s = Sl()

C = Li()
zero = [0] * N
one = [0] * N
for i in range(N):
    if s[i] == '1':
        zero[i] = C[i]
    else:
        one[i] = C[i]

if N % 2 == 0:
    left_sum = [0] * (N+1)
    right_sum = [0] * (N+1)
    left_sum2 = [0] * (N+1)
    right_sum2 = [0] * (N+1)
    for i in range(1, N + 1):
        left_sum[i] = left_sum[i-1] + zero[i-1] * (i % 2) + one[i-1] * ((i+1) % 2)
        right_sum[i] = right_sum[i-1] + zero[-i] * (i % 2) + one[-i] * ((i+1) % 2)

        left_sum2[i] = left_sum2[i-1] + zero[i-1] * ((i+1) % 2) + one[i-1] * (i % 2)
        right_sum2[i] = right_sum2[i-1] + zero[-i] * ((i+1) % 2) + one[-i] * (i % 2)
    ans = float('Inf')
    for i in range(1, N):
        ans = min(ans, left_sum[i] + right_sum[-i-1], left_sum2[i] + right_sum2[-i-1])

else:
    left_sum = [0] * (N+1)
    right_sum = [0] * (N+1)
    left_sum2 = [0] * (N+1)
    right_sum2 = [0] * (N+1)
    for i in range(1, N + 1):
        left_sum[i] = left_sum[i-1] + zero[i-1] * ((i+1) % 2) + one[i-1] * (i % 2)
        right_sum[i] = right_sum[i-1] + zero[-i] * (i % 2) + one[-i] * ((i+1) % 2)

        left_sum2[i] = left_sum2[i-1] + zero[i-1] * (i % 2) + one[i-1] * ((i+1) % 2)
        right_sum2[i] = right_sum2[i-1] + zero[-i] * ((i+1) % 2) + one[-i] * (i % 2)
    ans = float('Inf')
    for i in range(1, N):
        ans = min(ans, left_sum[i] + right_sum[-i-1], left_sum2[i] + right_sum2[-i-1])

print(ans)