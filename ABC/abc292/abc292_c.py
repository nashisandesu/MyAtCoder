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
N = int(input())
ans = 0
num_list = [0] * N 
for i in range(1, N):
    for j in range(1, N):
        if i*j >= N:
            break
        num_list[i*j] += 1
for i in range(1, N):
    for j in range(1, N):
        if i*j >= N:
            break
        ans += num_list[N-i*j]
print(ans)