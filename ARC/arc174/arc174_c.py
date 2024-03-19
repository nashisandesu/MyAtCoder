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
def mod_cal(x, y):#x/y
    mod = 998244353
    denominator = pow(y, -1, mod)
    return x * denominator % mod

# def check(x):
#     for i in range(1, 100):
#         for j in range(1, 100):
#             if mod_cal(i, j) == x:
#                 return (i, j)
mod = 998244353
N = I()
p_dp = [[0] * 2 for _ in range(N+1)]
e_dp = [[0] * 2 for _ in range(N+1)]
p_dp[0][0] = 1
for i in range(1, N + 1):
    p_dp[i][0] = p_dp[i-1][0] * mod_cal(i-1, N+i-1) % mod + p_dp[i-1][1] * mod_cal(N, N+i-1) % mod
    p_dp[i][1] = p_dp[i-1][1] * mod_cal(i-1, N+i-1) % mod + p_dp[i-1][0] * mod_cal(N, N+i-1) % mod
    first = mod_cal(N*(i-1), N*N - (i-1) * (i-1))
    second = mod_cal((i-1)*(i-1), N*N - (i-1) * (i-1))
    e_dp[i][0] = (first * p_dp[i-1][0] + second * p_dp[i-1][1] + e_dp[i-1][0]) % mod
    e_dp[i][1] = (first * p_dp[i-1][1] + second * p_dp[i-1][0] + e_dp[i-1][1]) % mod

print(*e_dp[-1])

