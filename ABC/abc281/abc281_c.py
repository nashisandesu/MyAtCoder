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
N, T = Mi()
A = Li()
sum_A = [0] * (N+1)
for i in range(N):
    sum_A[i+1] = sum_A[i] + A[i]
_, mod = divmod(T, sum_A[-1])
idx = bisect.bisect_left(sum_A, mod)
print(idx, mod - sum_A[idx-1])
