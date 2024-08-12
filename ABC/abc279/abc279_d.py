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
A, B = Mi()
x_min = (2*B/A) ** (-2/3) - 1

x_ans = int(x_min)
x_ans2 = x_ans + 1

ans = x_ans * B + A / ((x_ans + 1) ** (0.5))
ans2 = x_ans2 * B + A / ((x_ans2 + 1) ** (0.5))

print( "{:.8f}".format(min(ans, ans2)))
