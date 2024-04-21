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
s = Sl()
t = Sl()
start = [0] * (len(t) + 1)
start[0] = 1
end = [0] * (len(t) + 1)
end[0] = 1
for i in range(1, len(t) + 1):
    if (s[i-1] == t[i-1] or s[i-1] == '?' or t[i-1] == '?') and (start[i-1]):
        start[i] = 1
    if (s[-i] == t[-i] or s[-i] == '?' or t[-i] == '?') and (end[i-1]):
        end[i] = 1

for i in range(len(t)+1):
    if start[i] and end[-i-1]:
        print('Yes')
    else:
        print('No')