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
H, W = Mi()
data = [['.'] * (W+2)] + [['.'] + list(input()) + ['.'] for _ in range(H)] + [['.'] * (W+2)]
def check(i, j):
    cnt = 1
    while True:
        if data[i + cnt][j + cnt] == data[i + cnt][j - cnt] == data[i - cnt][j + cnt] == data[i - cnt][j - cnt] == '#':
            cnt += 1
        else:
            return cnt - 1
        
ans = [0] * (min(H, W) + 1)
for h in range(2, H):
    for w in range(2, W):
        if data[h][w] == '#': 
            ans[check(h, w)] += 1
print(*ans[1:])