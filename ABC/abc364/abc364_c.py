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
N, X, Y = Mi()
A = Li()
B = Li()
C = []
D = []
for i in range(N):
    C.append((A[i], B[i]))
    D.append((B[i], A[i]))
C.sort(reverse=True)
D.sort(reverse=True)
sweet1, salty1 = 0, 0
sweet2, salty2 = 0, 0
for i in range(N):
    sweet1 += C[i][0]
    salty1 += C[i][1]
    if sweet1 > X or salty1 > Y:
        print(i+1)
        exit()
    sweet2 += D[i][1]
    salty2 += D[i][0]
    if sweet2 > X or salty2 > Y:
        print(i+1)
        exit()
else:
    print(N)