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
N, M = Mi()
eat = [0] * N
wait = list(range(N))
goaway = []
for i in range(M):
    t, w, s = Mi()
    while goaway:
        comeback = heapq.heappop(goaway)
        if comeback[0] <= t:
            heapq.heappush(wait, comeback[1])
        else:
            heapq.heappush(goaway, comeback)
            break
    if wait:
        person = heapq.heappop(wait)
        eat[person] += w
        heapq.heappush(goaway, (t + s, person))
for i in range(N):
    print(eat[i])