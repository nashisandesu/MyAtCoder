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
left, right = 0, 0
LR = [Li() for _ in range(N)]
for i in range(N):
    L, R = LR[i]
    left += L
    right += R
if left <= 0 <= right:
    rest = right
    ans = []
    for i in range(N):
        L, R = LR[i]
        if rest == 0:
            ans.append(R)
        elif R - rest > L:
            ans.append(R - rest)
            rest = 0
        else:
            rest -= R - L
            ans.append(L)
    print('Yes')
    print(*ans)
else:
    print('No')