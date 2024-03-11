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
from functools import cache

@cache
def f(x):
    ans = 0
    for y in edge[x]:
        ans = max(ans, f(y) + 1)
    return ans

N, M = Mi()
dp = [0] * (N+1)
xy = [Li() for _ in range(M)]
edge = [[] for _ in range(N + 1)]
for x, y in xy:
    edge[x].append(y)
result = 0
for i in range(1, N + 1):
    result = max(result, f(i))

print(result)