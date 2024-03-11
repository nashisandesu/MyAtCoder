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
B = Li()
C = Li()
D = Li()
AB = []
CD = set()
for i in range(N):
    for j in range(N):
        AB.append(A[i] + B[j])
        CD.add(C[i] + D[j])

for ab in AB:
    if K - ab in CD:
        print('Yes')
        break
else:
    print('No')