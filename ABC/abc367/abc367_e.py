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
X = list(map(lambda x: int(x) - 1, input().split()))
A = Li()

# dp[i][j] i番目の要素を2^j回操作した結果の要素
dp = [[0] * (60 + 1) for _ in range(N)]

# 1回目の操作
for i in range(N):
    dp[i][0] = X[i]

# ダブリングの計算
for i in range(1, 60 + 1):
    for j in range(N):
        dp[j][i] = dp[dp[j][i-1]][i-1]

before = A[:]
after = A[:]
for i in range(60 + 1):
    if (K >> i) & 1:
        for j in range(N):
            after[j] = before[dp[j][i]]
        before = after[:]
print(*after)