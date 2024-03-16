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
N, M, H, K = Mi()
s = Sl()
now = (0,0)
potion = {}
for _ in range(M):
    potion[tuple(map(int, input().split()))] = 1
for i in range(N):
    if H == 0:
        print('No')
        break
    else:
        H -= 1
        if s[i] == 'R':
            now = (now[0] + 1, now[1])
        elif s[i] == 'L':
            now = (now[0] - 1, now[1])
        elif s[i] == 'U':
            now = (now[0], now[1] + 1)
        elif s[i] == 'D':  
            now = (now[0], now[1] - 1)
        
        if now in potion and potion[now] > 0 and H < K:
            H = K
            potion[now] -= 1
else:
    print('Yes')
