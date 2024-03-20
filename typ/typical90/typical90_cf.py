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
#愚直
# N = I()
# s = Sl()
# data = {'o': [], 'x': []}
# for i in range(N):
#     data[s[i]].append(i)
# data['o'].append(N)
# data['x'].append(N)

# ans = 0
# for i in range(N):
#     if s[i] == 'o':
#         idx = bisect.bisect_left(data['x'], i)
#         ans += N - data['x'][idx]
#     elif s[i] == 'x':
#         idx = bisect.bisect_left(data['o'], i)
#         ans += N - data['o'][idx]
# print(ans)


#ランレングス圧縮
N = I()
s = Sl()
pre = s[0]
cnt = 1
ans = 0
for i in range(1, N):
    if s[i] == pre:
        cnt += 1
    else:
        pre = s[i]
        ans += cnt * (cnt-1) // 2
        cnt = 1
else:
    ans += cnt * (cnt-1) // 2
print(N * (N-1) // 2 - ans)
