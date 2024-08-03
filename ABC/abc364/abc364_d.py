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
a = Li()
a.sort()
ans = []
for i in range(Q):
    b, k = Mi()
    if b <= a[0]:
        ans.append(a[k-1] - b)
    elif b >= a[-1]:
        ans.append(b - a[N-k])
    else:
        d_left = 0
        d_right = max(b-a[0], a[-1]-b)
        while d_right - d_left > 0:
            d_mid = (d_left + d_right) // 2
            left_bound = b - d_mid
            right_bound = b + d_mid
            search_left = bisect.bisect_left(a, left_bound)
            search_right = bisect.bisect_right(a, right_bound) - 1
            if search_right - search_left + 1 == k:
                ans.append(max(a[search_right] - b, b - a[search_left]))
                break
            if search_right - search_left + 1< k:
                d_left = d_mid + 1
            else:
                d_right = d_mid
        else:
            ans.append(d_left)
print(*ans, sep='\n')