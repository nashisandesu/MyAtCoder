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
A, M, L, R = Mi()
if A < L:
    left = A + ((L - A) // M) * M
    if left < L:
        left += M
    right = left + ((R - left) // M) * M
    print((right-left)//M + 1)
elif L <= A and A <= R:
    cnt = 1
    cnt += (A-L) // M
    cnt += (R-A) // M
    print(cnt)
else:
    right = A - ((A - R) // M) * M
    if right > R:
        right -= M
    left = right - ((right-L)//M) * M
    print((right-left)//M+ 1)
