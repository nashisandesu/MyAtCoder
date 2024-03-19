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
def make_kakko(now, l, r):
    if l == r == N // 2:
        print(now)
        return
    
    if l < N // 2:
        make_kakko(now + '(', l + 1, r)
        
    if l > r and r < N // 2:
        make_kakko(now + ')', l, r + 1)    
N = I()
if N % 2:
    print()
else:
    make_kakko('(', 1, 0)