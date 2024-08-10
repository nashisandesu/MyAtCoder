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
s = list(input())
cnt = 0
i = 0
while i < len(s):
    if i == len(s) - 1:
        cnt += 1
        i += 1
    elif s[i] == '0' and s[i+1] == '0':
        cnt += 1
        i += 2
    else:
        cnt += 1
        i += 1
print(cnt)