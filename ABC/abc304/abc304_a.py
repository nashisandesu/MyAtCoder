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
N = int(input())
list1 = []
list2 = []
min = -1
point = None
for i in range(N):
    name, age = input().split()
    list1.append(name)
    list2.append(age)
    if min == -1 or min > int(age):
        min = int(age) 
        point = i
for i in range(N):
    print(list1[(point + i) % N])
