import sys, bisect
import math
# import numpy as np
from atcoder.lazysegtree import LazySegTree
from atcoder.segtree import SegTree
from atcoder.dsu import DSU
sys.setrecursionlimit(10**8)
from collections import deque
from collections import defaultdict
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
N, M = Mi()
A = Li()
A.sort()
A_set = []
for a in A:
    if not A_set:
        A_set.append([a, 1])
    elif A_set[-1][0] == a:
        A_set[-1][1] += 1
    else:
        A_set.append([a, 1])

mod_data = defaultdict(int)
for num, cnt in A_set:
    mod_data[num % M] = max(num * cnt, mod_data[num % M])

mod_data = sorted(mod_data.items())
mod_data = mod_data * 2
before = mod_data[0][0]
max_sum = 0
now_sum = 0
for mod, s in mod_data:
    if mod == (before + 1) % M:
        now_sum += s
        before += 1
    else:
        max_sum = max(max_sum, now_sum)
        now_sum = s
        before = mod
else:
    max_sum = max(max_sum, now_sum)

print(max(0, sum(A) - max_sum))
