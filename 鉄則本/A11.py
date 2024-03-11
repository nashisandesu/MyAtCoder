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
N, X = Mi()
A = Li()
l = 0
r = N - 1
while l < r:
    center = (r+l)//2
    if A[center] >= X:
        r = center
    else:
        l = center + 1
print(r + 1)