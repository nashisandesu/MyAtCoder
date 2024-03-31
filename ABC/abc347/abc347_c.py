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
N, A, B = Mi()
D = Li()
week = A+B
mod_D = set()
for i in range(N):
    mod_D.add(D[i] % week)
mod_D = list(mod_D)
mod_D.sort()
mod_D_len = len(mod_D)
ans_min = mod_D[-1] - mod_D[0] + 1
for j in range(1, mod_D_len):
    ans_min = min(ans_min, mod_D[j-1] + week - mod_D[j] + 1)

if ans_min <= A:
    print('Yes')
else:
    print('No')
