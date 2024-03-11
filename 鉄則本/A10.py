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
A = Li()
D = I()
small = [0] * N
small[0] = A[0]
large = [0] * N
large[0] = A[-1]
for i in range(1, N):
    small[i] = max(small[i-1], A[i])
    large[i] = max(large[i-1], A[-1-i])
for _ in range(D):
    L, R = Mi()
    print(max(small[L-2], large[N-R-1]))