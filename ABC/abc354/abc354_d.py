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
A, B, C, D = Mi()
menseki = [[2, 1, 0, 1], [1, 2, 1, 0]]
start1 = A % 4
aida1, amari1 = divmod(C - A, 4)
yoko_one = 4 * aida1
yoko_two = 4 * aida1
for i in range(amari1):
    yoko_one += menseki[0][(start1 + i) % 4]

for i in range(amari1):
    yoko_two += menseki[1][(start1 + i) % 4]

start2 = B % 2
aida2, amari2 = divmod((D- B), 2)


ans = 0

ans += (yoko_one + yoko_two) * aida2
if amari2 == 1:
    if start2 == 0:
        ans += yoko_one
    else:
        ans += yoko_two
print(ans)
