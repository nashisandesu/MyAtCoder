import sys, bisect
import math
import numpy as np
sys.setrecursionlimit(10**8)
from collections import deque
import itertools
from itertools import combinations
from itertools import permutations
from more_itertools import distinct_permutations

I = lambda: int(input())
S = lambda: str(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
N, W = Mi()
data = [Li() for _ in range(N)]
MAXV = 100001
dp = [[float('INF')] * (MAXV+1) for _ in range(N+1)] #dp[i][v]:i番目までみた時に、ちょうど価値がvになる最小の重さを記録する。
dp[1][0] = 0
for i in range(1, N+1):
    w, v = data[i-1]
    for sum_v in range(MAXV+1):
        if sum_v == v: 
            dp[i][sum_v] = w
        elif sum_v > v:
            if dp[i - 1][sum_v - v] + w <= W:
                dp[i][sum_v] = dp[i - 1][sum_v - v] + w
        dp[i][sum_v] = min(dp[i][sum_v], dp[i-1][sum_v])
for i in range(MAXV):
    if dp[N][-i-1] != float('Inf'):
        print(MAXV-i)
        break