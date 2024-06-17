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
bn = bin(N)[2:]
bm = bin(M)[2:]
bit_counts = [0] * 60
mod = 998244353
for i in range(N.bit_length()):
    sho, amari = divmod(N + 1, (2**(i+1)))
    bit_counts[i] += sho * (2 ** i)
    bit_counts[i] += max(0, amari - 2**i)
    bit_counts[i] %= mod
ans = 0
for i in range(M.bit_length()):
    if bm[-i-1] == '1':
        ans += bit_counts[i]
        ans %= mod
print(ans)
