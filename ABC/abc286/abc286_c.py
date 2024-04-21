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
S = lambda: str(input())
Sl = lambda: list(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
def check(s):
    rev_s = s[:]
    rev_s.reverse()
    dif = 0
    for i in range((len(s)+1)//2):
        if s[i] != rev_s[i]:
            dif += 1
    return dif
    
N, A, B = Mi()
s = Sl()
ans = float('Inf')
for i in range(0, N):
    now = s[i:] + s[:i]
    cost = A * i
    dif = check(now)
    ans = min(ans, cost + B * dif)

print(ans)

                  