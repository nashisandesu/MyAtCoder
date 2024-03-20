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
T = I()
l, X, Y = Mi()
y = [0, -float(l)/2, 0, float(l)/2]
z = [0, float(l)/2, l, float(l)/2]
Q = I()
for _ in range(Q):
    e = I()
    _, amari = divmod(e, T)
    degree = math.radians(360 * float(amari) / T)

    ekun = [0, -math.sin(degree) * float(l) / 2, (1-math.cos(degree)) * float(l) / 2]
    height = ekun[2]
    dist = ((X-ekun[0]) ** 2 + (Y-ekun[1]) ** 2) ** 0.5
    print(math.degrees(math.atan(height/dist)))
