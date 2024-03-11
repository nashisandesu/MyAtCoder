import sys, bisect
import math
import numpy as np
sys.setrecursionlimit(10**8)
from collections import deque
from itertools import combinations
from itertools import permutations

I = lambda: int(input())
S = lambda: str(input())
I_M = lambda: map(int, input().split())
S_M = lambda: map(str, input().split())
I_L = lambda: list(map(int, input().split()))
S_L = lambda: list(map(int, input().split()))

#########################################################3

N = I()
dp = [[0] * 2 for _ in range(N)]

bA, bB = I_M()
dp[0][0] = 1
dp[0][1] = 1
mod = 998244353
for i in range(1, N):
    A, B = I_M()
    if A != bA:
        dp[i][0] += dp[i - 1][0]
        dp[i][0] %= mod
    if A != bB:
        dp[i][0] += dp[i - 1][1]
        dp[i][0] %= mod
    if B != bA:
        dp[i][1] += dp[i - 1][0]
        dp[i][1] %= mod
    if B != bB:
        dp[i][1] += dp[i - 1][1]
        dp[i][1] %= mod
    bA, bB = A, B
print((dp[-1][0] + dp[-1][1]) % mod)    
