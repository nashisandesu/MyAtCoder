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
def check_count(small):
    big = small + 1
    cnt_small, cnt_big = 0, 0
    for i in range(N):
        if small > A[i]:
            cnt_small += small - A[i]
        elif big < A[i]:
            cnt_big += A[i] - big
    return max(cnt_small, cnt_big)

N = I()
A = Li()
average = float(sum(A)) / N

if int(average) == average:
    print(min(check_count(int(average)), check_count(int(average - 1))))
else:
    print(check_count(int(average)))