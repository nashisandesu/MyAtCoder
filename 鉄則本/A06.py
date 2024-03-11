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
N, Q = Mi()
A = Li()
S = [0]
for i in range(N):
    S.append(S[i] + A[i])
for i in range(Q):
    L, R = Mi()
    print(S[R] - S[L - 1])
