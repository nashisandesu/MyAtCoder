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
# 優先度付きキュー
# N, K = Mi()
# data = []
# A = [0] * N
# for i in range(N):
#     a, b = Mi()
#     heapq.heappush(data, (-b, i))
#     A[i] = -(a - b)

# ans = 0
# for i in range(K):
#     point, num = heapq.heappop(data)
#     ans += -point
#     if num != float('Inf'):
#         heapq.heappush(data, (A[num], float('Inf')))
# print(ans)

# 今回はb > a - b が保証されるので、部分点を取る前に満点(との差分)を取ることはない
N, K = Mi()
data = []
for i in range(N):
    a, b = Mi()
    data.append(b)
    data.append(a - b)
data.sort(reverse=True)
print(sum(data[:K]))
