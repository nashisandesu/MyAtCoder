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
sum_A = [A[0]%M]
for i in range(1, 2 * N - 1):
    sum_A.append((sum_A[-1] + A[i % N])%M)

mod_list = [0] * M
for i in range(N-1):
    mod_list[sum_A[i]] += 1
ans = mod_list[0] 
for i in range(N-1):
    mod_list[sum_A[i + N - 1]] += 1
    mod_list[sum_A[i]] -= 1
    ans += mod_list[sum_A[i]]
print(ans)
