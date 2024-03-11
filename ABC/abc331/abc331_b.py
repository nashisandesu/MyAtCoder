import sys, bisect
import math
import numpy as np
sys.setrecursionlimit(10**8)
from collections import deque
from itertools import combinations
from itertools import permutations

I = lambda: int(input())
# S = lambda: str(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
N, S, M, L = Mi()
dp = [0]* 101

for i in range(1, N+1):
    if i < 6:
        dp[i] = min(S,M,L)
    elif i < 8:
        dp[i] = min(dp[i-6] + S,M,L)
    elif i < 12:
        dp[i] = min(dp[i-6] + S, dp[i-8]+M, L)
    else:
        dp[i] = min(dp[i-6] + S, dp[i-8]+M, dp[i-12]+L)

print(dp[N])