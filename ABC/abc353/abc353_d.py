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
N = I()
A = Li()
ans = 0
mod = 998244353
sum_A =[0] * (N+1)
keta_A = [0] * (N+1)
for i in range(N):
    sum_A[i+1] = sum_A[i] + A[i]
    sum_A[i+1] %= mod
    keta_A[i+1] = keta_A[i] + 10 ** len(str(A[i]))

ans = 0
for i in range(N):
    ans += A[i] * (keta_A[N] - keta_A[i+1]) % mod
    ans  += sum_A[N] - sum_A[i + 1]
    ans %= mod

print(ans % mod)