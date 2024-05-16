import sys, bisect
import math
import numpy as np
sys.setrecursionlimit(10**8)
from collections import deque
from itertools import combinations
from itertools import permutations

I = lambda: int(input())
S = lambda: str(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
N = I()
p = [0] + [Li() for _ in range(N)]
dp = [[0] * (N+1) for _ in range(N+1)]

dp[1][N] = 0
for len in range(N - 1, -1, -1):
    for l in range(1, N - len + 1):
        r = l + len
        if l >= 2:
            if l-1 <= p[l-1][0] <= r:
                score1 = dp[l-1][r] + p[l-1][1]
            else:
                score1 = dp[l-1][r]
        else:
            score1 = 0

        if r <= N - 1:
            if l <= p[r+1][0] <= r+1:
                score2 = dp[l][r+1] + p[r+1][1]
            else:
                score2 = dp[l][r+1]
        else:
            score2 = 0

        dp[l][r] = max(score1, score2)
ans = 0

for i in range(1, N+1):
    ans = max(ans, dp[i][i])
print(ans)
        