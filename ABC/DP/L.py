import sys, bisect
import math
# import numpy as np
sys.setrecursionlimit(10**8)
from collections import deque
import itertools
from itertools import combinations
from itertools import permutations
from more_itertools import distinct_permutations
import heapq

I = lambda: int(input())
S = lambda: str(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
N = I()
a = Li()
a.insert(0, 0)
dp = [[float('Inf')] * (N + 1) for _ in range(N + 1)]
visit = [[0] * (N + 1) for _ in range(N + 1)]


def f(i, j, bool):
    if visit[i][j]:
        return dp[i][j]
    else:
        visit[i][j] = 1
    
    if bool:
        bool ^= 1
        if i + 1 == j:
            ans = max(a[i] - a[j], a[j] - a[i])
        else: 
            ans = max(f(i+1, j, bool) + a[i], f(i, j-1, bool) + a[j])
    else:
        bool ^= 1
        if i + 1 == j:
            ans = min(a[j] - a[i], a[i] - a[j])
        else:
            ans = min(f(i+1, j, bool) - a[i], f(i, j-1, bool) - a[j])
    dp[i][j] = ans
    return ans

if N == 1:
    print(a[1])
else:
    print(f(1, N, 1))
