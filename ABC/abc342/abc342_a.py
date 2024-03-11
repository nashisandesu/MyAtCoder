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
S = list(input())
N = len(S)
first = S[0]
second = S[1]
if first == second:
    for i in range(2, N):
        if S[i] != first:
            print(i+1)
            exit()
else:
    third = S[2]
    if first == third:
        print(2)
    else:
        print(1)