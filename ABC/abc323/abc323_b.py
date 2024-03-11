import sys, bisect
import math
import numpy as np
sys.setrecursionlimit(10**8)
from collections import deque
from itertools import combinations
from itertools import permutations

I = lambda: int(input())
S = lambda: str(input())
M = lambda: map(int, input().split())
I_L = lambda: list(map(int, input().split()))
S_L = lambda: list(map(int, input().split()))

########################################################
N = I()
result = {}
for i in range(N):
    result.setdefault(i,0)
for i in range(N):
    S = list(input())
    for j in range(N):
        if i == j:
            continue
        else:
            if S[j] == 'o':
                result[i] += 1
            else:
                result[j] += 1
data = sorted(result.items(), key=lambda x:x[1], reverse = True)
for i in range(len(data)):
    if i == len(data) -1:
        print(data[i][0] + 1)
    else:
        print(data[i][0] + 1, end = ' ')
