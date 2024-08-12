import sys, bisect
import math
# import numpy as np
from atcoder.lazysegtree import LazySegTree
from atcoder.segtree import SegTree
from atcoder.dsu import DSU
sys.setrecursionlimit(10**8)
from collections import deque
from collections import defaultdict
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
Q = I()
add_data = defaultdict(lambda: [0, 0])
reset = 0
resenum = None
for _ in range(Q):
    q, *x = Mi()
    if q == 1:
        reset += 1
        resenum = x[0]
    elif q == 2:
        if add_data[x[0]][0] == reset:
            add_data[x[0]][1] += x[1]
        else:
            add_data[x[0]] = [reset, x[1]]
    else:
        if reset == 0:
            print(A[x[0]-1] + add_data[x[0]][1])
        else:
            if add_data[x[0]][0] == reset:
                print(resenum + add_data[x[0]][1])
            else:
                print(resenum)
