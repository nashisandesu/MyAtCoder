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
N, Q = Mi()
S = list(input())
tonari = [0] * (N+1)
for i in range(1, N):  
    if S[i-1] == S[i]:
        tonari[i] = tonari[i-1] + 1
    else:
        tonari[i] = tonari[i-1]
for j in range(Q):
    l, r = Mi()
    print(tonari[r-1]-tonari[l-1])