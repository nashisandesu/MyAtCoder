import sys, bisect
import math
import numpy as np
sys.setrecursionlimit(10**8)
from collections import deque
import itertools
from itertools import combinations
from itertools import permutations
from atcoder.dsu import DSU
from more_itertools import distinct_permutations
from heapq import heappush, heappop, heapify

I = lambda: int(input())
S = lambda: str(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
N, M, K = Mi()
v_list = [Li() for _ in range(M)]
ans = float('Inf')
for comb in combinations(range(M), N - 1):
    uf = DSU(N)
    cost = 0
    for node in comb:
        u, v, w = v_list[node]
        u -= 1
        v -= 1
        uf.merge(u,v)
        cost += w
        cost %= K
    if uf.size(0) == N:
        ans = min(ans, cost)
        
print(ans % K)