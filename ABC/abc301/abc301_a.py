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
N = int(input())
S = list(input())
count_T = 0
count_A = 0
for i in range(N):
    if S[i] == "T":
        count_T += 1
    else:
        count_A += 1
if count_A > count_T:
    print("A")
elif count_T > count_A:
    print("T")
else:
    if S[N-1] == "T":
        print("A")
    else:
        print("T")