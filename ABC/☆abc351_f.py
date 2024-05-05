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
N = I()
A = Li()

sum_A = [0] * (N+1)
for i in range(N):
    sum_A[i+1] = sum_A[i] + A[i]

cnt_A = {}
for i in range(N):
    cnt_A.setdefault(A[i], [0, 0])
    cnt_A[A[i]][0] += A[i] 
    cnt_A[A[i]][1] += 1 
data = list(cnt_A.items())

data.sort()

idx = {}
idx[data[0][0]] = 0
data[0] = data[0][1]

for i in range(1, len(data)):
    idx[data[i][0]] = i
    data[i] = [data[i-1][0] + data[i][1][0], data[i-1][1] + data[i][1][1]]


def mapping(lazy_upper, data_lower):
    return [data_lower[0] - lazy_upper[0], data_lower[1]- lazy_upper[1]]

def composition(lazy_upper, lazy_lower):
    return [lazy_upper[0] + lazy_lower[0], lazy_upper[1] + lazy_lower[1]]

l_st = LazySegTree(op=min, e=[float('Inf'), float('Inf')], mapping= mapping, composition= composition, id_ = [0,0], v = data)

ans = 0
for i in range(N-1):
    ans += sum_A[N] - sum_A[i + 1]
    ans -= (N - i - 1) * A[i]
    a, b =  l_st.get(idx[A[i]])

    if b > 0:
        ans += b * A[i] - a
    l_st.apply(idx[A[i]], len(data), [A[i], 1])
print(ans)



