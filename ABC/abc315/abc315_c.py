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
N = I()
ice = []
for i in range(N):
    f, s = Mi()
    ice.append((s,f))
ice.sort(reverse=True)

if ice[0][1] != ice[1][1]:
    print(ice[0][0]+ice[1][0])
else:
    flavor = ice[0][1]
    now = ice[0][0] + ice[1][0] // 2
    for i in range(2, N):
        if flavor != ice[i][1]:
            if ice[0][0] + ice[i][0] > now:
                print(ice[0][0] + ice[i][0])
            else:
                print(now)
            break
    else:
        print(now)

