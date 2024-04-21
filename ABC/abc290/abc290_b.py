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
N, K = map(int, input().split())
S = input()
S_list = [x for x in S]
count = 0
for i in range(N):
    if count == K:
        S_list[i] = "x"
    elif S_list[i] == "o":
        count += 1
for i in range(len(S_list)-1):
    print(S_list[i], end="")
print(S_list[-1])