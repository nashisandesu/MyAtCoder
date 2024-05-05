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
min_edge = []
A_data = set()
for i in range(M):
    K, C = Mi()
    A = Li()
    for a in A:
        A_data.add(a)
    heapq.heappush(min_edge, (C, A))
if len(A_data) != N:
    print(-1)
    exit()
uf = DSU(N)
cnt = 0
cost = 0
visit = [0] * (N+1)
while min_edge:
    c, a_list = heapq.heappop(min_edge)
    first, *rest = a_list
    for next in rest:
        if uf.same(first - 1, next - 1) == False:
            uf.merge(first - 1, next - 1)
            cnt += 1
            cost += c
        if cnt == N-1:
            print(cost)
            exit()