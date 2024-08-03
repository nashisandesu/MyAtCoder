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
N, K = Mi()
MOD = 998244353

ans = 1
# (現在の位置の期待値) * (N-2)/N + (移動先の平均(=(N+1)/2)) * 2/N
for i in range(K):
    temp = ((N - 2) * ans) % MOD
    ans = (temp * pow(N, -1, MOD)) % MOD + ((N+1) * pow(N, -1, MOD)) % MOD
    ans %= MOD
print(ans)