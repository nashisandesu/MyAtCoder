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
A = Li()
B = Li()
A.sort()
B.sort()

kouho = A + [B[i] + 1 for i in range(M)]
kouho.sort()

for ans in kouho:
    A_num = bisect.bisect_right(A, ans)
    B_num = M - bisect.bisect_left(B, ans)
    
    if A_num >= B_num:
        print(ans)
        break
