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
N, M = Mi()

A = [Li() for _ in range(M)]
for i in range(M):
    num = 0
    for a in A[i]:
        num *= 2
        num += a
    A[i] = num
dp = [[float('Inf')] * 2 ** N for _ in range(M+1)]
dp[0][0] = 0
for i in range(1, M+1):
    for j in range(2**N):
        dp[i][j] = min(dp[i-1][j], dp[i][j])
        dp[i][A[i-1]|j] = min(dp[i-1][j] + 1, dp[i][A[i-1]|j])
if dp[-1][-1] == float('Inf'):
    print(-1)
else:
    print(dp[-1][-1])