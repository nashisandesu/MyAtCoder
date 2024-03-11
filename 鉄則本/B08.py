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
P = [tuple(map(int, input().split())) for _ in range(N)]
XY = [[0] * 1501 for _ in range(1501)]
for i in range(N):
    XY[P[i][0]][P[i][1]] += 1


XY_S = [[0] * 1501 for _ in range(1501)]
for x in range(1, 1501):
    for y in range(1, 1501):
        XY_S[x][y] = XY_S[x][y - 1] + XY[x][y]

for y in range(1, 1501):
    for x in range(1, 1501):
        XY_S[x][y] = XY_S[x - 1][y] + XY_S[x][y]

Q = I()
for _ in range(Q):
    a, b, c, d = Mi()
    print(XY_S[c][d] - XY_S[c][b-1] - XY_S[a-1][d] + XY_S[a-1][b-1])