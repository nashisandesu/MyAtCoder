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
from itertools import combinations_with_replacement
from itertools import product
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
data = [Li() for _ in range(N)]
for i in range(N):
    now = 0
    ans = 0
    for j in range(N):
        if i != j:
            dist = ((data[i][0]-data[j][0])**2 + (data[i][1]-data[j][1])**2)**0.5
            if dist > now:
                ans = j + 1
                now = dist
    print(ans)