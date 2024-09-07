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
N = I()
L, R = None, None
ans = 0
for i in range(N):
    a, s = Ms()
    a = int(a)
    if s == 'L':
        if L is None:
            L = a
        else:
            ans += abs(a - L)
            L = a
    else:
        if R is None:
            R = a
        else:
            ans += abs(a - R)
            R = a
print(ans)