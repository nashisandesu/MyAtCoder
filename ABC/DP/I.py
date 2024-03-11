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
N = I()
dp = [[0] * (N+1) for _ in range(N+1)]
p_list = list(map(float, input().split()))
dp[0][0] = 1
for i in range(1, N+1): #i回目
    p = p_list[i-1]
    for j in range(i+1): #表j回
        dp[i][j] = dp[i-1][j] * (1-p) + dp[i-1][j-1] * p

ans = 0
for i in range(N//2 + 1):
    ans += dp[N][N-i]
print(ans)