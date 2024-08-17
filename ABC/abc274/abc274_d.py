import sys, bisect
import math
# import numpy as np
from atcoder.lazysegtree import LazySegTree
from atcoder.segtree import SegTree
from atcoder.dsu import DSU
sys.setrecursionlimit(10**8)
from collections import deque
from collections import defaultdict
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
N, x, y = Mi()
A = Li()
A_max = max(A)
x_cnt = (N + 1) // 2
y_cnt = N - x_cnt
dp_x = [[False] * ((A_max * x_cnt) * 2 + 1) for _ in range(x_cnt+1)]
dp_y = [[False] * ((A_max * y_cnt) * 2 + 1) for _ in range(y_cnt+1)]
dp_x[0][A_max * x_cnt] = True
dp_y[0][A_max * y_cnt] = True
for i in range(1, N + 1):
    # xの方
    if i % 2 == 1:
        idx = i // 2 + 1
        for j in range(2 * x_cnt * A_max):
            if dp_x[idx-1][j]:
                dp_x[idx][j + A[i-1]] = True
                if idx != 1:
                    dp_x[idx][j - A[i-1]] = True
    # yの方
    else:
        idx = i // 2
        for j in range(2 * y_cnt * A_max):
            if dp_y[idx-1][j]:
                dp_y[idx][j + A[i-1]] = True
                dp_y[idx][j - A[i-1]] = True

if dp_x[-1][A_max * x_cnt + x] and dp_y[-1][A_max * y_cnt + y]:
    print('Yes')
else:
    print('No')

