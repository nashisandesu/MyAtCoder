import bisect

import math
import numpy as np

import sys
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
A, B, D = Mi()
ans = [A]
now = A
while(True):
    if now == B:
        break
    now += D
    ans.append(now)
print(' '.join(map(str,ans)))