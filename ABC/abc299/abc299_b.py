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
N, T = Mi()
c_data = Li()
r_data = Li()
data = {}
for i in range(N):
    data.setdefault(c_data[i],[])
    heapq.heappush(data[c_data[i]], (-r_data[i],i+1))
if T in data:
    print(heapq.heappop(data[T])[1])
else:
    print(heapq.heappop(data[c_data[0]])[1])