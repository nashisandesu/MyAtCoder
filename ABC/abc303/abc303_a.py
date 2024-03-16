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
N = I()
s = Sl()
t = Sl()
for i in range(N):
    if s[i] == t[i]:
        continue
    elif (s[i] == '1' and t[i] == 'l') or (s[i] == 'l' and t[i] == '1'):
        continue
    elif (s[i] == '0' and t[i] == 'o') or (s[i] == 'o' and t[i] == '0'):
        continue
    else:
        print('No')
        break
else:
    print('Yes')