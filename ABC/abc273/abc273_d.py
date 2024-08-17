import sys, bisect
import math
# import numpy as np
from atcoder.lazysegtree import LazySegTree
from atcoder.segtree import SegTree
from atcoder.dsu import DSU
sys.setrecursionlimit(10**8)
from collections import deque
from collections import defaultdict
from itertools import combinations
from itertools import permutations
from itertools import combinations_with_replacement
from itertools import product
import heapq
from sortedcontainers import SortedList

I = lambda: int(input())
S = lambda: str(input())
Sl = lambda: list(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
H, W, rs, cs = Mi()
N = I()
# 端を用意しておく(番兵)ことで、条件分岐を減らせる。ここでは0, H+1, W+1に壁があることにしている。
H_wall = defaultdict(lambda: SortedList([0, W + 1]))
W_wall = defaultdict(lambda: SortedList([0, H + 1]))
for _ in range(N):
    r, c = Mi()
    H_wall[r].add(c)
    W_wall[c].add(r)

Q = I()
for _ in range(Q):
    d, l = Ls()
    l = int(l)
    if d == 'L':
        idx = bisect.bisect_left(H_wall[rs], cs)
        cs = max(cs - l, H_wall[rs][idx-1] + 1)
    elif d == 'R':
        idx = bisect.bisect_left(H_wall[rs], cs)
        cs = min(cs + l, H_wall[rs][idx] - 1)
    elif d == 'U':
        idx = bisect.bisect_left(W_wall[cs], rs)
        rs = max(rs - l, W_wall[cs][idx-1] + 1)
    else:
        idx = bisect.bisect_left(W_wall[cs], rs)
        rs = min(rs + l, W_wall[cs][idx] - 1)

    print(rs, cs)