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
N, K = Mi()
A = Li()
sum_A = [0] * (N+1)
sum_A[0] = 0
for i in range(N):
    sum_A[i+1] = sum_A[i] + A[i]
now = 1
ans = 0
for i in range(1, N + 1):
    while now < N + 1 and K >= sum_A[now] - sum_A[i - 1]:
        now += 1
    ans += now - i
print(ans)