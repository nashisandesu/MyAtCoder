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
V1, V2, V3 = Mi()

def cal_1(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    pass

def cal_2(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    x_l_12, x_r_12 = min(a1 + 7, a2), -93
    y_l_12, y_r_12 = min(b1 + 7, b2), -93
    z_l_12, z_r_12 = min(c1 + 7, c2), -93

    x_l_13, x_r_13 = min(a1 + 7, a3), -93
    y_l_13, y_r_13 = min(b1 + 7, b3), -93
    z_l_13, z_r_13 = min(c1 + 7, c3), -93 

    x_l_23, x_r_23 = min(a2 + 7, a3), -93
    y_l_23, y_r_23 = min(b2 + 7, b3), -93
    z_l_23, z_r_23 = min(c2 + 7, c3), -93 

    v1 = min

def cal_3(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    x_l_12, x_r_12 = min(a1 + 7, a2), -93
    y_l_12, y_r_12 = min(b1 + 7, b2), -93
    z_l_12, z_r_12 = min(c1 + 7, c2), -93

    x_l_13, x_r_13 = min(a1 + 7, a3), -93
    y_l_13, y_r_13 = min(b1 + 7, b3), -93
    z_l_13, z_r_13 = min(c1 + 7, c3), -93

    x_l_123, x_r_123 = min(x_l_12, x_l_13), min(x_r_12, x_r_13)
    y_l_123, y_r_123 = min(y_l_12, y_l_13), min(y_r_12, y_r_13)
    z_l_123, z_r_123 = min(z_l_12, z_l_13), min(z_r_12, z_r_13)

    return min(x_r_123 - x_l_123, 0)*min(y_r_123 - y_l_123, 0)*min(z_r_123 - z_l_123, 0)


if V1 + V2 * 2 + V3 * 3 != 1029:
    print('No')
else:
    for x in range(-100, 101):
        for y in range(-100, 101):
            for z in range(-100, 101):
        
                pass