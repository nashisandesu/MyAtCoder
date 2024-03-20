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
#ちょっと早い
N = I()
coins = Li()
coins.sort()
ans = float('Inf')
for i in reversed(range(N // coins[-1] + 1)):
    next = N - i * coins[-1]
    for j in reversed(range(min(10000, next // coins[1] + 1))):
        next2 = next - j * coins[1]
        if next2 % coins[0] == 0:
            ans = min(ans, i + j + next2 // coins[0])
print(ans)

#愚直
# N = I()
# coins = Li()
# coins.sort()
# ans = float('Inf')
# for i in range(10000):
#     for j in range(10000):
#         next = N - i * coins[2] - j * coins[1]
#         if next >= 0 and next % coins[0] == 0:
#             ans = min(ans, i + j + next // coins[0])
# print(ans)
