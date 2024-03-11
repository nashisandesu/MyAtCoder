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
N, T = Mi()
point = [0] * (N+1)
point_dict = {0:N}
cnt = 1
for i in range(T):
    A, B = Mi()
    past = point[A]
    next = point[A] + B
    point[A] = next
    point_dict.setdefault(next, 0)
    if point_dict[past] == 1:
        cnt -= 1
    if point_dict[next] == 0:
        cnt += 1
    point_dict[past] -= 1
    point_dict[next] += 1
    print(cnt)
