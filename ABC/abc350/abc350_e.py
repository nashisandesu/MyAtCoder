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
N, A, X, Y = map(float, input().split())
from functools import cache
@cache
def f(N):
    if N == 0:
        return 0
    sumall = f(N//2) + f(N//3) + f(N//4) + f(N//5) + f(N//6)
    return min(X + f(N//A), Y * 1.2 + (sumall) / 5)
print(f(N))