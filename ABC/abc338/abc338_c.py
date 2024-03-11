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
N = I()
Q = Li()
A = Li()
B = Li()
Amax = 10**6
Bmax = 10**6
for i in range(N):
    if A[i] != 0:
        if Amax > Q[i] // A[i]:
            Amax = Q[i] // A[i]
    if B[i] != 0:
        if Bmax > Q[i] // B[i]:
            Bmax = Q[i] // B[i]   
ans = max(Amax, Bmax)
for i in range(1, Amax + 1):
    Bnow = 10**6
    for j in range(N):
        if B[j] != 0:
            if Bnow > (Q[j] - (A[j] * i)) // B[j]:
                Bnow = (Q[j] - (A[j] * i)) // B[j]
    if Bnow + i > ans:
        ans = Bnow + i
print(ans)