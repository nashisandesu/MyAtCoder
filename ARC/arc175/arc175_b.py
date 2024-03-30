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
N, A, B = Mi()
s = Sl()
left, right = 0, 0
for i in range(2*N):
    if s[i] == '(':
        left += 1
    else:
        right += 1

if A >= B * 2:
    A = B * 2

cost = B * abs(N-left)
if left < right:
    rest = right - N
    now_l, now_r = 0, 0
    swap = 0
    for i in range(2 * N):
        if s[i] == '(':
            if now_l == N:
                now_r += 1
            else:
                now_l += 1
        elif now_l == now_r:
            swap += 1
            now_l += 1
        elif now_l > now_r:
            now_r += 1
    print(cost + (swap - rest) * A)

elif left >= right:
    rest = left - N
    now_l, now_r = 0, 0
    swap = 0
    cnt = 0
    for i in range(2 * N):
        if s[i] == '(':
            if now_l == N:
                now_r += 1
                cnt += 1
            else:
                now_l += 1
        elif now_l == now_r:
            swap += 1
            now_l += 1
        elif now_l > now_r:
            now_r += 1  
    print(cost + swap * A)


