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
N = I()
A = Li()
data = A[:] + A[:]
sum_A = [0] * (2 * N + 1)
size = 0
for i in range(2 * N):
    size += data[i]
    sum_A[i+1] = sum_A[i] + data[i]

size //= 2

if size % 10 == 0:
    want = size // 10
    for i in range(1, 2 * N + 1):
        now = sum_A[i]
        if now < size:
            continue
        else:
            search = now - want
            idx = bisect.bisect_left(sum_A, search)
            if sum_A[idx] == search:
                print('Yes')
                break
    else:
        print('No')
else:
    print('No')