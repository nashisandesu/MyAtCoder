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
T = I()
N = I()
sa = [0] * (T + 1)
for _ in range(N):
    L, R = Mi()
    sa[L] += 1
    sa[R] -= 1
exist = [0] * (T + 1)
exist[0] = sa[0]

for t in range(1, T + 1):
    exist[t] = exist[t - 1] + sa[t]

for t in range(T):
    print(exist[t])