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
A = input()
A_list = [x for x in A]
for i in range(len(A_list)):
    if A_list[i] == "0":
        A_list[i] = "1"
    else:
        A_list[i] = "0"
for i in range(len(A_list)-1):
    print(A_list[i], end="")
print(A_list[-1])