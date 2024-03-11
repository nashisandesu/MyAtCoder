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
T = 0
A = 0
for i in range(N):
    t, a = Mi()
    T += t
    A += a
if T > A:
    print('Takahashi')
elif A > T:
    print('Aoki')
else:
    print('Draw')