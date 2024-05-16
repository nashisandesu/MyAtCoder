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
s = input()
t = input()

dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)] 
for i in range(len(s) + 1):
    for j in range(len(t) + 1):
        if i > 0 and j > 0 and s[i-1] == t[j-1]:
            dp[i][j] = min(dp[i-1][j] + 1, dp[i-1][j] + 1, dp[i-1][j-1])
        elif i > 0 and j > 0:
            dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 1)
        elif i > 0:
            dp[i][j] = dp[i-1][j] + 1
        elif j > 0:
            dp[i][j] = dp[i][j-1] + 1
print(dp[-1][-1])