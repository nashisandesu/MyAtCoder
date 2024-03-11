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
maxT = 10**9
def check(T):
    done = 0
    for i in range(N):
        done += T // A[i] 
    if done >= K:
        return True
    else:
        return False
    
l = 0
r = maxT
while l < r:
    center = (l+r)//2
    if check(center):
        r = center
    else:
        l = center + 1
print(l)