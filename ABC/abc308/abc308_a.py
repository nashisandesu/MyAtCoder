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
s = Li()
if s[0] % 25 == 0 and 100 <= s[0] <= 675:
    for i in range(1, 8):
        if s[i-1] <= s[i] and s[i] % 25 == 0 and 100 <= s[i] <= 675:
            continue
        else:
            print('No')
            break
    else:
        print('Yes')
else:
    print('No')