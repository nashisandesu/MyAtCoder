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
N, L = Mi()
dp = [0] * (N+1)
dp[0] = 1
for i in range(1, N + 1):
    if i - L >= 0:
        dp[i] = dp[i-1] + dp[i-L]
    else:
        dp[i] = dp[i-1]

mod = 10 ** 9 +7
print(dp[-1] % mod)