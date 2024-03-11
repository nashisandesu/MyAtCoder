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
N = I()
done = [0] * (N+1)
must = [0] * (N+1)
for i in range(N):
    C, *P = Li()
    must[i+1] = P
task = deque(must[1])

ans = []
def dfs(book):
    if done[book] == 1:
        return
    elif len(must[book]) == 0:
        ans.append(book)
        done[book] = 1
        return
    else:
        while must[book]:
            next = must[book].pop()
            dfs(next)
        ans.append(book)
        done[book] = 1

dfs(1)
print(*ans[:-1])