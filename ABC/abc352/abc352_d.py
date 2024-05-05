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
# N, K = Mi()
# P = Li()
# idx_dic = {P[i]:i+1 for i in range(N)}
# #1-Kまで
# min_idx = []
# max_idx = []
# for i in range(1, K + 1):
#     heapq.heappush(min_idx, idx_dic[i])
#     heapq.heappush(max_idx, -idx_dic[i]) 
# small = heapq.heappop(min_idx)
# big = heapq.heappop(max_idx)
# ans = (-big) - small
# heapq.heappush(min_idx, small)
# heapq.heappush(max_idx, big)

# print(min_idx)
# print(max_idx)
# for i in range(2, N-K+2):
#     heapq.heappush(min_idx, idx_dic[i-1+K])
#     heapq.heappush(max_idx, -idx_dic[i-1+K]) 
#     while True:
#         b = heapq.heappop(max_idx)
#         if P[(-b) - 1] >= i:
#             heapq.heappush(max_idx, b)
#             break
#     while True:
#         s = heapq.heappop(min_idx)
#         if P[s - 1] >= i:
#             heapq.heappush(min_idx, s)
#             break
#     ans = min(ans, -b-s)
# print(ans)

N, K = Mi()
P = Li()
idx_list = [(P[i] - 1, i) for i in range(N)]
idx_list.sort()
st1 = SegTree(max, 0, [idx_list[i][1] for i in range(N)])
st2 = SegTree(min, float('Inf'), [idx_list[i][1] for i in range(N)])
ans = float('Inf')
for i in range(N-K+1):
    max_idx = st1.prod(i, i+K)
    min_idx = st2.prod(i, i+K)
    ans = min(ans, max_idx - min_idx)
print(ans)