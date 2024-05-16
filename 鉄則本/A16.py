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
A = Li()
B = Li()
dp = [0] * (N+1)
dp[2] = A[0]
for i in range(3, N+1):
    dp[i] = min(dp[i-1]+A[i-2], dp[i-2]+ B[i-3])
print(dp[-1])