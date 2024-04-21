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
A = [0] + Li()
data_A = [0] * (N+1)
cnt = 0
ans = []
for i in range(1, N+1):
    data_A[A[i]] = i
for i in range(1, N+1):
    if A[i] == i:
        continue
    else:
        cnt += 1
        ans.append((i, data_A[i]))
        temp1 = A[i] #交換相手
        A[i] = i
        A[data_A[i]] = temp1


        data_A[temp1] = data_A[i]
        data_A[i] = i

print(cnt)
for i in range(cnt):
    print(*ans[i])