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

dp = [[0] * (W+1) for _ in range(N+1)] #dp[i][w]:i番目までみた時に、ちょうど重さがwになる最大の価値を記録する。

for i in range(1, N+1):
    w, v = data[i-1]
    for sum_w in range(W+1):
        if sum_w - w >= 0:
            dp[i][sum_w] = max(dp[i-1][sum_w-w] + v, dp[i][sum_w])
        dp[i][sum_w] = max(dp[i][sum_w], dp[i-1][sum_w])
print(max(dp[N]))