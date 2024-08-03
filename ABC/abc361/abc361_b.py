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
a, b, c, d, e, f = Mi()
g, h, i, j, k, l = Mi()
x = max(a, d) > min(g, j) and max(g, j) > min(a, d)
y = max(b, e) > min(h, k) and max(h, k) > min(b, e)
z = max(c, f) > min(i, l) and max(i, l) > min(c, f)
if x and y and z:
    print('Yes')
else:
    print('No')