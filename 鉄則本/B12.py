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
def search_x(n):
    l = 0.0
    r = float(n)
    while abs(n - fc(r)) > 0.001:
        center = (r+l)/2
        if fc(center) > n:
            r = center
        else:
            l = center
    return r
    
def fc(x):
    return x**3 + x

print(search_x(N))
