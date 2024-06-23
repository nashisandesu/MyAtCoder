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
H = Li()
water = deque()
ans = [0] * N
time = 0

ans[0] = H[0] + 1
water.append((H[0], 1))
time = H[0] 
for i in range(1, N):
    sum_cnt = 0
    time += H[i]
    while water:
        height, cnt = water.pop()
        sum_cnt += cnt
        if height > H[i]:
            water.append((height, cnt))
            water.append((H[i], sum_cnt - cnt + 1))
            break
        elif height == H[i]:
            water.append((height, sum_cnt + 1))
            break
        else:
            time += (H[i] - height) * cnt
    else:
        water.append((H[i], sum_cnt + 1))
    ans[i] = time + 1
print(*ans)