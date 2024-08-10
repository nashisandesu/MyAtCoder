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
N, K, D = Mi()
A = Li()
dp = [[[-1] * D for _ in range(K+1)] for _ in range(N+1)]
dp[0][0][0] = 0
# a_1-a_iからj個選んでDで割った余りがkであるような最大値
for i in range(N):
    for j in range(K+1):
        for k in range(D):
            # 配るDP
            if dp[i][j][k] == -1:
                continue
            else:
                # a_iを選ばない
                dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j][k])
                # a_iを選ぶ
                if j < K:
                    dp[i+1][j+1][(k+A[i])%D] = max(dp[i+1][j+1][(k+A[i])%D], dp[i][j][k] + A[i])
print(dp[N][K][0])