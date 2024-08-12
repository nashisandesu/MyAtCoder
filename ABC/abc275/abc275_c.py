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
def is_square(a, b, c, d):
    ab2 = (a[0]-b[0]) ** 2 + (a[1]-b[1]) ** 2
    bc2 = (b[0]-c[0]) ** 2 + (b[1]-c[1]) ** 2
    ca2 = (c[0]-a[0]) ** 2 + (c[1]-a[1]) ** 2
    if ab2 == bc2 and ab2 + bc2 == ca2:
        want_d = (a[0]+c[0]-b[0], a[1]+c[1]-b[1])
    elif bc2 == ca2 and bc2 + ca2 == ab2:
        want_d = (b[0]+a[0]-c[0], b[1]+a[1]-c[1])
    elif ca2 == ab2 and ca2 + ab2 == bc2:
        want_d = (c[0]+b[0]-a[0], c[1]+b[1]-a[1])
    else:
        return False
    
    if want_d == d:
        return True

ss = [input() for _ in range(9)]
porn = []
for i in range(9):
    for j in range(9):
        if ss[i][j] == '#':
            porn.append((i,j))
cnt = 0
for a, b, c, d in combinations(porn, 4):
    if is_square(a, b, c, d):
        cnt += 1

print(cnt)
