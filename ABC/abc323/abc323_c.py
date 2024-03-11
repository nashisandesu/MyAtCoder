import sys, bisect
import math
import numpy as np
sys.setrecursionlimit(10**8)
from collections import deque
from itertools import combinations
from itertools import permutations

I = lambda: int(input())
S = lambda: str(input())
M = lambda: map(int, input().split())
I_L = lambda: list(map(int, input().split()))
S_L = lambda: list(map(int, input().split()))

########################################################
N, M = M()
A = I_L()
now_point = [0] * N
rest = [[] for _ in range(N)]
for i in range(N):
    S = list(input())
    for j, s in enumerate(S):
        if s == 'o':
            now_point[i] += A[j]
        else:
            rest[i].append(A[j])
    now_point[i] += i + 1

top = max(now_point)
for i in range(N):
    sa = top - now_point[i]
    cnt = 0
    rest[i].sort()
    while sa > 0:
        sa -= rest[i][-1-cnt]
        cnt += 1
    print(cnt)
