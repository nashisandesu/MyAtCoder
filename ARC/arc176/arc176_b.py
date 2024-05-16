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
T = I()

def ans(n, m, k):
    waru_one_cnt = m - k
    if waru_one_cnt == 1:
        if n >= m - 1:
            return 0
        else:

            return (2 ** (((n-1)%4)+1)) % 10
    zero = k
    temp = max(0,(n - zero) // waru_one_cnt)
    amari = n - temp * waru_one_cnt + 1
    if amari == 0:
        return 0
    elif amari == 1:
        return 1
    else:
        _, rest = divmod(amari-1, 4)
        if rest == 1:
            return 2
        elif rest == 2:
            return 4
        elif rest == 3:
            return 8
        elif rest == 0:
            return 6

data = []
for _ in range(T):
    N, M, K = Mi()
    data.append(ans(N, M, K))
# print(*data)
for i in range(T):
    print(data[i])