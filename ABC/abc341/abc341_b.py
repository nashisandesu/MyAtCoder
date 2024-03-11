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
A = Li()
ST = [Li() for _ in range(N-1)]
for i in range(N-1):
    if A[i] >= ST[i][0]:
        sho, amari = divmod(A[i], ST[i][0])
        A[i+1] += sho * ST[i][1]
print(A[-1])