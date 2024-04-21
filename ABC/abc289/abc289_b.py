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
N, M = map(int, input().split())
re_list = set(map(int, input().split()))
i = 1
new_list = []
while (i <= N):
    next = [i]
    for j in range(i, N+1):
        if j in re_list:
            next.append(j+1)
        else:
            break
    i = i + len(next) 
    for k in range(len(next)):
        new_list.append(next[len(next)-k-1])
for i in range(len(new_list)-1):
    print(new_list[i], end=" ")
print(new_list[-1])