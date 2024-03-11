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
A = Li()
data = dict()
for i in range(N):
    data[A[i]] = i + 1

result = list()
result.append(data[-1])
now = data[-1]
for i in range(N-1):
    result.append(data[now])
    now = data[now]

print(' '.join(map(str,result)))