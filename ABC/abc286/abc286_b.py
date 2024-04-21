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
ans = []
for i in range(N-1):
    if s[i] == 'n' and s[i+1] == 'a':
        s[i+1] = ''
        ans.append('nya')
    else:
        ans.append(s[i])
ans.append(s[-1])
print(''.join(ans))