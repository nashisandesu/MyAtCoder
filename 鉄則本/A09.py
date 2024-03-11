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
H, W, N = Mi()
snow = [[0] * (W+1) for _ in range(H+1)]
for i in range(N):
    A, B, C, D = Mi()
    snow[A-1][B-1] += 1
    snow[C][D] += 1
    snow[A-1][D] -= 1
    snow[C][B-1] -= 1

for h in range(H):
    for w in range(1, W):
        snow[h][w] += snow[h][w-1]

for w in range(W):
    for h in range(1, H):
        snow[h][w] += snow[h-1][w]

for i in range(H):
    for j in range(W):
        if j == W - 1:
            print(snow[i][j])
        else:
            print(snow[i][j], end = ' ')