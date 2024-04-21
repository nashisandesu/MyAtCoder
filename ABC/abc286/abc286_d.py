import sys, bisect
import math
import numpy as np
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
N, X = Mi()
data = [0] * (X+1)
data[0] = 1
for i in range(N):
    A, B = Mi()
    for x in reversed(range(X)):
        if data[x]:
            for b in range(1, B+1):
                if x + A * b <= X:
                    data[x+A*b] = 1
                else:
                    break

if data[-1]:
    print('Yes')
else:
    print('No')
    

