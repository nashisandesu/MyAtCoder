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
K, G, M = Mi()
nowG = 0
nowM = 0
for i in range(K):
    if nowG == G:
        nowG = 0
    elif nowM == 0:
        nowM = M
    else:
        if nowG + nowM <= G:
            nowG = nowG + nowM
            nowM = 0
        else:
            nowM = nowM - (G - nowG)
            nowG = G
print(nowG, nowM)