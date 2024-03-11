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
dp = [float('INF')] * (N+1)
dp[1] = 0
cost = Li()
cost.insert(0, 0)
for i in range(2, N+1):
    dp[i] = min(dp[i-2] + abs(cost[i-2] - cost[i]), dp[i-1] + abs(cost[i-1] - cost[i]))
print(dp[N])