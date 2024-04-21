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
S = list(input())
B_index = []
K_index = 0
R_index = []
for i in range(8):
    if S[i] == "B":
        B_index.append(i)
    elif S[i] == "K":
        K_index = i
    elif S[i] == "R":
        R_index.append(i)
if (B_index[1] - B_index[0]) % 2 != 0 and R_index[0] < K_index < R_index[1]:
        print("Yes")
else:
    print("No")