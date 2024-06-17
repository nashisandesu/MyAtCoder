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
#遅延セグ
def op(data1, data2):
    return data1 ^ data2

def mapping(lazy_upper, data_lower):
    return data_lower + lazy_upper

def composition(lazy_upper, lazy_lower):
    return lazy_upper + lazy_lower

A = [1,2,3,4,5]
l_st = LazySegTree(op=min, e=float('Inf'), mapping=lambda f, x: f+x, composition= lambda f, g: f + g, id_ = 0, v = A)
#恒等写像 id とは、全ての a に対してmapping(id, a) = a となるものを指します。

N, Q = Mi()