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
N = I()
A = Li()
min_two_cnt = 10 ** 9
min_three_cnt = 10 ** 9
ans = 0
for i in range(N):
    two_cnt = 0
    while True:
        if A[i] % 2 == 0:
            A[i] //= 2
            two_cnt += 1
        else:
            break
    
    three_cnt = 0
    while True:
        if A[i] % 3 == 0:
            A[i] //= 3
            three_cnt += 1
        else:
            break

    ans += two_cnt
    ans += three_cnt
    min_two_cnt = min(min_two_cnt, two_cnt)
    min_three_cnt = min(min_three_cnt, three_cnt)
    
if A == [A[0]] * N:
    print(ans - (min_two_cnt + min_three_cnt) * N)
else:
    print(-1)

