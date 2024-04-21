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
N, M = Mi()
uf = DSU(N)
for i in range(M):
    A, B = Mi()
    uf.merge(A-1, B-1)
data = uf.groups()
cnt = 0
for i in range(len(data)):
    cnt += (len(data[i]) - 1) * len(data[i]) // 2 
print(cnt - M)

