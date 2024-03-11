import sys, bisect
import math
# import numpy as np
from atcoder.lazysegtree import LazySegTree
from atcoder.segtree import SegTree
from atcoder.dsu import DSU
sys.setrecursionlimit(10**8)
from collections import deque
from itertools import combinations
from itertools import permutations
import heapq

I = lambda: int(input())
# S = lambda: str(input())
Sl = lambda: list(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
T = list(input())
len_T = len(T)
T.insert(0,0)
N = I()
dp = [float('Inf')] * (len_T + 1)
dp[0] = 0

for i in range(N):
    A, *S = Ms()
    A = int(A)
    for d in reversed(range(len_T + 1)):
        for j in range(A):
            if dp[d] != float('Inf'):
                if d + len(S[j]) <= len_T and list(S[j]) == T[d+1 : d + len(S[j]) + 1]:
                    dp[d + len(S[j])] = min(dp[d + len(S[j])], dp[d] + 1)
                    
if dp[len(T)-1] == float('Inf'):
    print(-1)
else:
    print(dp[len(T)-1])

