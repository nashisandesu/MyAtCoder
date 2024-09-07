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
N = I()
A = [0] + Li()
dp = [[0] * 2 for _ in range(N + 1)]
dp[0][0] = 0
dp[0][1] = -10**18
for i in range(1, N + 1):
    dp[i][0] = dp[i-1][0]
    dp[i][1] = dp[i-1][1]

    dp[i][0] = max(dp[i-1][1] + 2 * A[i], dp[i][0])
    dp[i][1] = max(dp[i-1][0] + A[i], dp[i][1])
print(max(dp[N]))