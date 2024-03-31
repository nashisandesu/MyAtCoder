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
N, Q = Mi()
x = [0] + Li()
A = [0] * (N+1)
data = {}
s = set()
add_data = [0] * (Q+1)
cnt = 0
for i in range(1, Q + 1):
    data.setdefault(x[i], 0)
    if data[x[i]]:
        A[x[i]] += add_data[i-1] - add_data[data[x[i]]-1]
        data[x[i]] = 0
        cnt -= 1
    else:
        data[x[i]] = i
        cnt += 1
    add_data[i] = add_data[i-1] + cnt

for key, value in data.items():
    if value == 0:
        continue
    else:
        A[key] += add_data[Q] - add_data[value-1]

print(*A[1:])