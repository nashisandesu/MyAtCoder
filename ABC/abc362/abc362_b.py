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
xa, ya = Mi()
xb, yb = Mi()
xc, yc = Mi()
AB = (xb - xa) ** 2 + (yb - ya) ** 2
BC = (xc - xb) ** 2 + (yc - yb) ** 2
CA = (xa - xc) ** 2 + (ya - yc) ** 2
if AB == BC + CA or BC == CA + AB or CA == AB + BC:
    print('Yes')
else:
    print('No') 