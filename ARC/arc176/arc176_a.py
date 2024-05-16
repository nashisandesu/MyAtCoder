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
first = [Li() for _ in range(M)]
cnt = 0
visit = []
print(N*M)
for i in range(M):
    a_0, b_0 = first[i]
    if (b_0-a_0) % N in visit: 
        cnt += 1
    else:
        visit.append((b_0-a_0) % N)
        print(a_0, b_0)
        for j in range(1, N):
            a_j, b_j = (a_0 - 1 + j) % N + 1, (b_0 - 1 + j) % N + 1
            print(a_j, b_j)
idx = 1
while cnt > 0:
    if (idx-1) % N not in visit:
        visit.append((idx - 1) % N)
        a_0, b_0 = 1, idx
        print(a_0, b_0)
        for j in range(1, N):
            a_j, b_j = (a_0 - 1 + j) % N + 1, (b_0 - 1 + j) % N + 1
            print(a_j, b_j)
        cnt -= 1
    idx += 1
