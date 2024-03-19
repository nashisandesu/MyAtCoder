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
one = [1,
       80,
       9800,
       998000,
       99980000,
       9999800000,
       999998000000,
       99999980000000,
       9999999800000000,
       999999998000000000
       ]

sec = [[0, 0],
       [90, 109],
       [9900, 10099],
       [999000, 1000999],
       [99990000, 100009999],
       [9999900000, 10000099999],
       [999999000000, 1000000999999],
       [99999990000000, 100000009999999],
       [9999999900000000, 10000000099999999],
       [999999999000000000, 1000000000999999999]]

sec_num = [1, 20, 200, 2000, 20000, 200000, 2000000, ]
T = I()
for i in range(T):
    N = I()
    ans = 0
    for i in range(len(sec)):
        if N < sec[i][1]:
            if N >= sec[i][0]:
                ans += N - sec[i][0] + 1 + 1
            elif N >= one [i]:
                ans += 1
            break
        else:
            if i == 0:
                ans += 1
            else:
                ans += 2 * (10**i) + 1
    print(ans)