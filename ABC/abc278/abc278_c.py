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
N, Q = Mi()
follow = defaultdict(lambda: defaultdict(int))
for _ in range(Q):
    t, a, b = Mi()
    if t == 1:
        follow[a][b] = 1
    elif t == 2:
        follow[a][b] = 0
    else:
        if follow[a][b] == 1 and follow[b][a] == 1:
            print('Yes')
        else:
            print('No')
    