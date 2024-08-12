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

I = lambda: int(input())
S = lambda: str(input())
Sl = lambda: list(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
H, W = Mi()
s = [Sl() for _ in range(H)]
t = [Sl() for _ in range(H)]
s_tate = [[] for _ in range(W)]
t_tate = [[] for _ in range(W)]
for h in range(H):
    for w in range(W):
        s_tate[w].append(s[h][w])
        t_tate[w].append(t[h][w])
s_tate.sort()
t_tate.sort()
if s_tate == t_tate:
    print('Yes')
else:
    print('No')
