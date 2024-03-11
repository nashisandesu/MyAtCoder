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
N, M = Mi()
rope = [0] * N
data = []
uf = DSU(N)
circ = 0
for _ in range(M):
    A, B, C, D = Ls()
    a = int(A) - 1
    c = int(C) - 1  
    if uf.same(a,c):
        circ += 1
    else:
        uf.merge(a, c)

print(circ, len(uf.groups())-circ)

