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
s = input()
data = {}
for i in s:
    data.setdefault(i, 0)
    data[i] += 1

check = [0] * 101
for key, value in data.items():
    check[value] += 1

for i in range(101):
    if check[i] == 0 or check[i] == 2:
        continue
    else:
        print('No')
        break
else:
    print('Yes')