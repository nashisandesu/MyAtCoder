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
X = [Li() for _ in range(H)]
Z = [[0] * (W+1) for _ in range(H+1)]
for h in range(1, H + 1):
    for w in range(1, W + 1):
        Z[h][w] = Z[h][w - 1] + X[h - 1][w - 1]

for w in range(1, W + 1):
    for h in range(1, H + 1):
        Z[h][w] = Z[h - 1][w] + Z[h][w]    

Q = I()
for _ in range(Q):
    A, B, C, D = Mi()
    print(Z[C][D] - Z[C][B - 1] -Z[A - 1][D] + Z[A - 1][B - 1])