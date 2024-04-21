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
N, M = Mi()
A = Li()
B = Li()
n = 0
m = 0
a_ans = []
b_ans = []
for i in range(1, N+M+1):
    if n == N:
        b_ans.append(i)
    elif m == M:
        a_ans.append(i)
    elif A[n] < B[m]:
        a_ans.append(i)
        n += 1
    else:
        b_ans.append(i)
        m += 1
print(*a_ans)
print(*b_ans)
