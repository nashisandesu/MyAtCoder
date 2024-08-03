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
N, T = Mi()
s = input()
X = Li()
sei = []
hu = []
for i in range(N):
    if s[i] == '0':
        hu.append(X[i])
    else:
        sei.append(X[i])
hu.sort()
sei.sort()
ans = 0
for x in sei:
    idx_left = bisect.bisect_right(hu, x)
    idx_right = bisect.bisect_right(hu, x + T * 2)
    ans += idx_right - idx_left
print(ans)