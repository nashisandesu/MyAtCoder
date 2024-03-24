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
W, B = Mi()
data = list('wbwbwwbwbwbw')
data = data * 15
for i in range(12):
    now = data[i:i+W+B]
    if now.count('w') == W and now.count('b') == B:
        print('Yes')
        break
else:
    print('No')
