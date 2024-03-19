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

for _ in range(T):
    A = Li()
    P = [0] + Li()
    value = 0
    for i in range(5):
        value += A[i] * (i + 1 - 3)
    if value >= 0:
        print(0)
    else:
        if value % 2 == 0:
            four = - value
            five = - value // 2
            print(min(four * P[4], five * P[5]))
        else:
            four = - value
            five = (- value // 2) + 1
            print(min(four * P[4], five * P[5], P[4] + (five-1) * P[5]))
