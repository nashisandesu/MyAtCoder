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
N, K = Mi()
mod = 10 ** 9 + 7
if N == 1:
    print(K % mod)
elif N == 2:
    print(K * (K-1) % mod)
else:
    ans = K * (K-1) % mod
    print((ans * pow(K-2, N-2, mod)) % mod)
