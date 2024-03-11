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
dp = [[0] * 3 for _ in range(N+1)]
dp[0] = 0
dp[1] = Li()
for i in range(2, N+1):
    abc = Li()
    for j in range(3):
        dp[i][j] = max(dp[i - 1][(j + 1) % 3] + abc[j], dp[i - 1][(j + 2) % 3] + abc[j])

print(max(dp[N]))