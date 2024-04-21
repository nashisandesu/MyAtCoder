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
H, W = map(int, input().split())
result = []
for i in range(H):
    data = list(input())
    flag = 0
    for j in range (W):
        if data[j] == "T":
            if flag == 1:
                data[j-1] = "P"
                data[j] = "C"
                flag = 0
            else:
                flag = 1
        else:
            flag = 0
    print("".join(data))