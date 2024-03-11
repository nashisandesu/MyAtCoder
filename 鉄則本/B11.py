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
A.sort()
Q = I()
def search(a: list, x: int):
    l = 0
    r = N - 1
    while l <= r:
        center = (r+l) // 2
        if a[center] >= x:
            r = center - 1
        else:
            l = center + 1
    return l
for _ in range(Q):
    X = I()
    print(search(A, X))
    # print(bisect.bisect_left(A, X))
