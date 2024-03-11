import sys, bisect
import math
import numpy as np
sys.setrecursionlimit(10**8)
from collections import deque
from itertools import combinations
from itertools import permutations

I = lambda: int(input())
S = lambda: str(input())
Sl = lambda: list(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
N, K = Mi()
A = Li()
left_sa = [0] * (K // 2 + 1)
right_sa = [0] * (K // 2 + 1)
for i in range(1, K // 2 + 1):
    left_sa[i] = left_sa[i-1] + A[(i - 1) * 2 + 1] - A[(i - 1) * 2]
for i in range(1, K // 2 + 1):
    right_sa[i] = right_sa[i-1] + A[(- i) * 2 + 1] - A[(- i) * 2]
if K % 2 == 0:
    cnt = 0
    for i in range(K // 2):
        cnt += A[2 * i + 1] - A[2 * i]
    print(cnt)
else:
    now = left_sa[0] + right_sa[-1]
    for i in range(len(left_sa)):
        now = min((left_sa[i] + right_sa[-1-i]), now)
    print(now)

