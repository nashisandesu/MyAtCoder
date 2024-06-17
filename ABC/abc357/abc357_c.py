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
N = I()
def solve(data, num):
    ans = []
    for i in range(3**(num)):
        ans.append(data[i]*3)
    for i in range(3**(num)):
        ans.append(data[i] + '...'*(3**(num-1)) + data[i])
    for i in range(3**(num)):
        ans.append(data[i]*3)

    return ans
ans = ['###', '#.#','###']
if N == 0:
    print('#')
    exit()
for i in range(N-1):
    ans = solve(ans, i+1)

for i in range(len(ans)):
    print(ans[i])
