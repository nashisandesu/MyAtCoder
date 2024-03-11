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
M, D = Mi()
y, m, d = Mi()
ans = [0]*3
if d== D:
    ans[2] = 1
    m += 1
else:
    ans[2] = d+1
if m - 1 == M:
    ans[1] = 1
    y+= 1
else:
    ans[1] = m
ans[0] = y
print(' '.join(map(str, ans)))