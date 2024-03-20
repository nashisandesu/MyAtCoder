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
def cnt(keta, small, big):
    temp = (small + big) % mod
    temp *= (big - small + 1) % mod
    return (keta * temp * pow(2, mod - 2, mod)) % mod #繰り返し二乗法

L, R = Mi()
small_keta, big_keta = len(str(L)), len(str(R))
mod = 10 ** 9 + 7
ans = 0
if small_keta == big_keta:
    ans = cnt(small_keta, L, R)
else:
    ans += cnt(small_keta, L, 10 ** small_keta - 1)
    for i in range(small_keta + 1, big_keta):
        maxv, minv = 10 ** i - 1, 10 ** (i-1)
        ans += cnt(i, minv, maxv)
    ans += cnt(big_keta, 10 ** (big_keta - 1), R)
    
print(ans % mod)