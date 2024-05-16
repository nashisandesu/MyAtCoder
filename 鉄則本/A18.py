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
N, S = Mi()
A = Li()
dp = [[False] * (S+1) for _ in range(N+1)]
dp[0][0] = True
for i in range(N):
    for j in range(S+1):
        if dp[i][j]:
            dp[i+1][j] = True
            if j + A[i] <= S:
                dp[i+1][j + A[i]] = True
if dp[-1][-1]:
    print('Yes')
else:
    print('No')