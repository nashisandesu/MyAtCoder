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
data = list(map(int, input().split()))
count = 0
data_dic = {}
for i in range(len(data)):
    if data[i] in data_dic:
        data_dic[data[i]] += 1
    else:
        data_dic[data[i]] = 1
for values in data_dic.values():
    count += values // 2

print(count)