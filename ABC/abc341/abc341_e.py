import sys, bisect
import math
# import numpy as np
from atcoder.lazysegtree import LazySegTree
from atcoder.segtree import SegTree
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

#######################################################
N, Q = Mi()
S = list(map(int, list(input())))

#セグ
# relation = [0] * (N - 1)
# for i in range(N-1):
#     if i == 0:
#         relation[i] = 1
#     else:
#         if S[i] == S[i+1]:
#             relation[i] = 0
#         else:
#             relation[i] = 1

# seg = SegTree(op=lambda f,g: f+g, e=0, v = relation)
# for i in range(Q):
#     num, L, R = Mi()
#     if num == 1:
#         if L-2 >= 0:
#             seg.set(L-2, 1 - seg.get(L-2))
#         if R - 1 < N - 1: 
#             seg.set(R-1, 1 - seg.get(R-1))
#     if num == 2:
#         if seg.prod(L-1, R-1) == R - L:
#             print('Yes')
#         else:
#             print('No')

#遅延セグ
def op(data1, data2):
    if data1 == data2:
        return data1
    elif data1 == 2 or data2 == 2:
        return min(data1, data2)
    else:
        return -1

def mapping(lazy_upper, data_lower):
    if lazy_upper:
        if data_lower == -1:
            return data_lower
        else:
            return data_lower ^ 1
    else:
        return data_lower

def composition(lazy_upper, lazy_lower):
    return lazy_upper ^ lazy_lower

S.insert(0, 2)
vs = [S[i] ^ 1 if i%2 else S[i] for i in range(N + 1)]
l_st = LazySegTree(op = op, e = 2, mapping = mapping, composition = composition, id_ = 0, v = vs)
for i in range(Q):
    num, L, R = Mi()
    if num == 1:
        l_st.apply(L, R + 1, 1)
    if num == 2:
        if l_st.prod(L, R + 1) == -1:
            print('No')
        else:
            print('Yes')
        