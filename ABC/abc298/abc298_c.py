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
Q = I()
box = [[] for _ in range(2*10**5+1)]
card = [[] for _ in range(2*10**5+1)]
ans = []
for _ in range(Q):
    num, *where = Mi()
    if num == 1:
        i, j = where
        box[j].append(i)
        card[i].append(j)
    elif num == 2:
        i = where[0]
        box[i].sort()
        ans.append(box[i][:])
    else:
        i = where[0]
        card[i] = sorted(list(set(card[i])))
        ans.append(card[i][:])

for i in range(len(ans)):
    print(*ans[i])