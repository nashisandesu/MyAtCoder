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
kukan = [Li() for _ in range(N)]
kukan.sort()
l = [kukan[i][0] for i in range(N)]
r = [kukan[i][1] for i in range(N)]
ans = 0
for i in range(N):
    edge = r[i]
    idx = bisect.bisect_right(l, edge)
    ans += idx - (i+1)
print(ans)