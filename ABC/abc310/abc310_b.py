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
N, M = Mi()
data = [Li() for _ in range(N)]
for i, j in combinations(range(N), 2):
    if data[i][0] > data[j][0]:
        data_i, data_j = data[i], data[j]
    elif data[i][0] < data[j][0]:
        data_i, data_j = data[j], data[i]
    else:
        if data[i][1] < data[j][1]:
            data_i, data_j = data[i], data[j]
        elif data[i][1] > data[j][1]:
            data_i, data_j = data[j], data[i]
        else:
            continue
    i_F, j_F = data_i[2:], data_j[2:]
    for i in range(data_i[1]):
        if i_F[i] not in j_F:
            break
    else:
        print('Yes')
        exit()
else:
    print('No')

    