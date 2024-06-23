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
sx, sy = Mi()
tx, ty = Mi()

tate = abs(ty - sy)
mid = sx + 1 if (sx + sy) % 2 == 0 else sx
left = mid - tate - 1
right = mid + tate

if left <= tx <= right:
    print(tate)
else:
    yoko = min((abs(tx - left) + 1) // 2, (abs(tx - right) + 1) // 2)
    print(tate + yoko)