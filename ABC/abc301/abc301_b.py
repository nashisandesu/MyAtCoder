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
A = list(map(int, input().split()))
for j in range(N - 1):
    print(A[j], end = " ")
    if abs(A[j] - A[j + 1]) != 1:
        if A[j] < A[j + 1]:
            for k in range(A[j] + 1, A[j + 1]):
                print(k, end=" ")
        else:
            for k in range(A[j] - 1, A[j + 1], -1):
                print(k, end=" ")
print(A[N - 1])
