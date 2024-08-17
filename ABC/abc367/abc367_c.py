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
def dfs(seq):
    if len(seq) == N:
        if sum(seq) % K == 0:
            ans.append(seq)
    else:
        for i in range(1, r[len(seq)] + 1):
            dfs(seq + [i])

N, K = Mi()
r = Li()
ans = []
for i in range(1, r[0] + 1):
    dfs([i])
ans.sort()

for a in ans:
    print(*a)
