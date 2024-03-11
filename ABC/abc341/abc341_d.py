import sys, bisect
import math
# import numpy as np
from atcoder.lazysegtree import LazySegTree
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
N, M, K = Mi()
small, big = min(N, M), max(N, M)
lcm_num = math.lcm(N, M)
cycle = lcm_num // small + lcm_num // big - 2
sho, amari = divmod(K, cycle)
if amari == 0:
    amari = cycle
    sho -= 1
s_cnt, b_cnt = 0, 0
for i in range(amari):
    if (s_cnt + 1) * small > (b_cnt + 1) * big:
        b_cnt += 1
        if i == amari-1:
            print(sho*lcm_num + big*b_cnt)

    else:
        s_cnt += 1
        if i == amari-1:
            print(sho*lcm_num + small * s_cnt)
