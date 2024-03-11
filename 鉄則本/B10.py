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
Q = I()
hit = [0]
nonhit = [0]
for i in range(N):
    hit.append(hit[i] + A[i])
    nonhit.append(nonhit[i] + 1 - A[i])
for i in range(Q):
    L, R = Mi()
    win = hit[R] - hit[L - 1]
    lose = nonhit[R] - nonhit[L - 1]
    if win == lose:
        print('draw')
    elif win > lose:
        print('win')
    else:
        print('lose')