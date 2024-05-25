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
from functools import lru_cache
I = lambda: int(input())
S = lambda: str(input())
Sl = lambda: list(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
def int_to_bin_str(value, digits):
    return bin(value)[2:].zfill(digits)

@lru_cache(None)
def solve(rest_card):
    if rest_card == 0 or rest_card == 1:
        return False
    for i, j in canpick:
        if (rest_card & (1 << i)) and (rest_card & (1 << j)):
            rest_next = rest_card & ~(1 << i) & ~(1 << j)
            if solve(rest_next) == False:
                return True
    return False


N = I()
cards = [Li() for _ in range(N)]
rest_card = (1 << N) - 1
canpick = []
for i in range(N):
    for j in range(i+1, N):
        if cards[i][0] == cards[j][0]:
            canpick.append((i,j))
        elif cards[i][1] == cards[j][1]:
            canpick.append((i,j))
if solve(rest_card):
    print('Takahashi')
else:
    print('Aoki')
