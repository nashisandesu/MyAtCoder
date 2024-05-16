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
A = [0] + Li()
# dp = [0] * (N+1)
LEN = 0
L = []
for i in range(1, N+1):
    pos = bisect.bisect_left(L, A[i])
    # dp[i] = pos
    if pos >= LEN:
        L.append(A[i])
        LEN += 1
    else:
        L[pos] = A[i]
print(LEN)
