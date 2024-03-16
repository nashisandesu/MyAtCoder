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
data = [Sl() for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i != j:
            s = data[i] + data[j]
            rev_s = s[:]
            rev_s.reverse()
            if s == rev_s:
                print('Yes')
                exit()
print('No')