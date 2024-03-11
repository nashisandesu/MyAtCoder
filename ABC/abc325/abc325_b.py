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
Xl = [0] * 24
for _ in range(N):
    W, X = Mi()
    start, end = (9 + X)% 24, (18 + X - 1) % 24
    if start < end:
        for i in range(start, end + 1):
            Xl[i] += W
    else:
        for i in range(0, end + 1):
            Xl[i] += W
        for j in range(start, 24):
            Xl[j] += W
    

# sum_X = [0]*24
# sum_X[0] = Xl[0]
# for i in range(1,24):
#     sum_X[i] = Xl[i] +sum_X[i -1]
print(max(Xl))
# print(max(sum_X))