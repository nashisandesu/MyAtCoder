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
Ls = lambda: list(map(int, input().split()))

########################################################
T = I()
for _ in range(T):
    N, K = Mi()
    cnt = 0
    sho, amari = N // 3, N % 3
    cnt += amari
    while sho > 2:
        N //= 3
        sho, amari = N // 3, N % 3
        cnt += amari
    else:
        cnt += sho
    # print(cnt)
    if cnt > K:
        print("No")
    elif (K - cnt) % 2:
        print("No")
    else:
        print("Yes")        
    