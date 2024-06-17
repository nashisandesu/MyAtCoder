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
A = Li()
B = Li()
A.sort(reverse=True)
B.sort(reverse=True)
idx = 0
rest = []
ans = 0
for i in range(M):
    while idx < N and A[idx] >= B[i]:
        heapq.heappush(rest, A[idx])
        idx += 1
    if not rest:
        print(-1)
        exit()
    ans += heapq.heappop(rest)
print(ans)