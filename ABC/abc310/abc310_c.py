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
data = set()
cnt = 0
for _ in range(N):
    now = len(data)
    s = list(input())
    if ''.join(s) in data:
        continue
    rev_s = s[:]
    rev_s.reverse()
    if ''.join(rev_s) in data:
        continue
    else:
        data.add(''.join(s))
        data.add(''.join(rev_s))
    cnt += 1
print(cnt)