import sys, bisect
import math
import numpy as np
sys.setrecursionlimit(10**8)
from collections import deque
import itertools
from itertools import combinations
from itertools import permutations
from more_itertools import distinct_permutations

I = lambda: int(input())
S = lambda: str(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
A = np.array([Li() for _ in range(9)])
flag = 0
for i in range(9):
    if len(set(A[i,:])) != 9:
        print('No')
        break
    if len(set(A[:,i])) != 9:
        print('No')
        break
    h, w = i // 3, i % 3
    squre = set(A[h*3:(h+1)*3, w*3:(w+1)*3].flatten())
    if len(squre) != 9:
        print('No')
        break
else:
    print('Yes')        