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
N, Q = Mi()
C = [{int(x)} for x in input().split()]
for i in range(Q):
    a, b = Mi()
    a -= 1
    b -= 1
    if len(C[b]) < len(C[a]):
        C[a].update(C[b])
        C[b] = C[a]
        C[a] = set()
    else:
        C[b].update(C[a])
        C[a] = set()
    print(len(C[b]))
