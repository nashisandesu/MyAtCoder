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
D = I()
N = I()
B = [0] * (D+1)
for i in range(N):
    L, R = Mi()
    B[L-1] += 1
    B[R] -= 1
S = [0] * D
S[0] = B[0]
print(S[0])
for i in range(1, D):
    S[i] = B[i] + S[i-1]
    print(S[i])
