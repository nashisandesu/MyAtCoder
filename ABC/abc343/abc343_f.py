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
N, Q = Mi()
A = Li()
def op(data1, data2):
    data_a, data_b = data1
    a, b = data_a[0], data_b[0]
    num_a, num_b = data_a[1], data_b[1]

    data_c, data_d = data2
    c, d = data_c[0], data_d[0]
    num_c, num_d = data_c[1], data_d[1]    
    if a > c:
        ans1 = a
        ans1_num = num_a
        if b > c:
            ans2 = b
            ans2_num = num_b
        elif b == c:
            ans2 = b
            ans2_num = num_b + num_c
        else:
            ans2 = c
            ans2_num = num_c

    elif a == c:
        ans1 = a
        ans1_num = num_a + num_c
        if b > d:
            ans2 = b
            ans2_num = num_b
        elif b == d:
            ans2 = b
            ans2_num = num_b + num_d
        else:
            ans2 = d
            ans2_num = num_d
    else:
        ans1 = c
        ans1_num = num_c
        if a > d:
            ans2 = a
            ans2_num = num_a
        elif a == d:
            ans2 = a
            ans2_num = num_a + num_d
        else:
            ans2 = d
            ans2_num = num_d
    return ((ans1, ans1_num), (ans2, ans2_num))


for i in range(N):
    A[i] = ((A[i], 1), (0, 0))
seg = SegTree(op, ((0, 0), (0, 0)), A)
for _ in range(Q):
    one, two, three = Mi()
    if one == 1:
        p = two - 1
        x = three
        seg.set(p, ((x, 1), (0, 0)))
    else:
        l = two - 1
        r = three
        ans = seg.prod(l, r)
        print(ans[1][1])
