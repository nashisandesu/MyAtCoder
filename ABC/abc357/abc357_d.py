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
def Power(a, b, m):
    result = 1
    base = a % m
    while b > 0:
        if b % 2 == 1:
            result = (result * base) % m
        base = (base * base) % m
        b //= 2
    return result

N = input()
length = len(N)
ans = 0
mod = 998244353

r = 10 ** length

big = Power(r, int(N), mod)

bunbo = Power((r-1)%mod, mod-2, mod)

sn_base = (big - 1 ) * bunbo

sn_base %= mod

for i in range(length):
    a = int(N[length - i - 1])  * 10 ** i
    sn = a * sn_base
    ans += sn
    ans %= mod
print(ans)

