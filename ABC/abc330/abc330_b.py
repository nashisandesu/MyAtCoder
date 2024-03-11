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
N, L , R = Mi()
A = Li()
ans = [0]*N
for i in range(N):
    if A[i] >= R:
        ans[i] = R
    elif A[i] <= L:
        ans[i] = L 
    else:
        ans[i] = A[i]
ans = map(str, ans)
print(' '.join(ans))
