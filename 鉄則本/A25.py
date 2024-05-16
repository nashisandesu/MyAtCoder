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
H, W = Mi()
c = [input() for _ in range(H)]
dp = [[0] * (W+1) for _ in range(H+1)]
for h in range(1, H + 1):
    for w in range(1, W + 1):
        if h == 1 and w == 1:
            dp[h][w] = 1
        elif c[h-1][w-1] == '.':
            if h >= 2:
                dp[h][w] += dp[h-1][w]
            if w >= 2:
                dp[h][w] += dp[h][w-1]
print(dp[-1][-1])