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
v = [Li() for _ in range(M)]
if N != M+1:
    print('No')
else:
    data = {}
    uf = DSU(N)
    for i in range(M):
        data.setdefault(v[i][0], 0)
        data.setdefault(v[i][1], 0)
        uf.merge(v[i][0]-1,v[i][1]-1)
        data[v[i][0]] += 1
        data[v[i][1]] += 1

    for v in data.values():
        if v > 2:
            print('No')
            exit()
 
    if uf.size(0) == N:
        print('Yes')
    else:
        print('No')