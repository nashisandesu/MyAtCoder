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
N, M = map(int, input().split())
deta_list = []
for i in range(M):
    C = int(input())
    a = set(map(int, input().split()))
    deta_list.append(a)

count = 0
for j in range(1, 2 ** M):
    syugou = set()
    for k in range(M):
        if j % 2 == 1:
            syugou |= deta_list[k]
        j //= 2
    if len(syugou) == N:
        count += 1
print(count)
    
