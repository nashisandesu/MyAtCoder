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

max = 1500
paper = [[0] * (max + 2) for _ in range(max+2)]
for _ in range(N):
    A, B, C, D = Mi()
    paper[A][B] += 1
    paper[C][D] += 1
    paper[A][D] -= 1
    paper[C][B] -= 1
for h in range(max + 1):
    for w in range(1, max + 1):
        paper[h][w] += paper[h][w - 1]

for w in range(max + 1):
    for h in range(1, max + 1):
        paper[h][w] += paper[h - 1][w]
cnt = 0
for w in range(max + 1):
    for h in range(max + 1):
        if paper[h][w] >= 1:
            cnt += 1
print(cnt)