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
data = [3, 1, 4, 1, 5, 9]
p, q = Ls()
a = ord(p) - 65
b = ord(q) - 65
if a > b:
    temp = a
    a = b
    b = temp
ans = 0
for i in range(a, b):
    ans += data[i]
print(ans)
