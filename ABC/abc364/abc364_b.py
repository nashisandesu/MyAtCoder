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
H, W = Mi()
si, sj = Mi()
si -= 1
sj -= 1
grid = [input() for _ in range(H)]
X = input()
for x in X:
    if x == 'U':
        if si - 1 >= 0 and grid[si-1][sj] == '.':
            si -= 1
    elif x == 'D':
        if si + 1 < H and grid[si+1][sj] == '.':
            si += 1
    elif x == 'L':
        if sj - 1 >= 0 and grid[si][sj-1] == '.':
            sj -= 1
    elif x == 'R':
        if sj + 1 < W and grid[si][sj+1] == '.':
            sj += 1
print(si+1, sj+1)
