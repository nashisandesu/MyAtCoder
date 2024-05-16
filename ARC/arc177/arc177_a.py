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
money_list = Li()
money = [1, 5,10,50,100,500]
N = I()
X = Li()
X.sort(reverse=True)
def cal(now, num):
    s, a = divmod(now, money[num])
    p = min(s, money_list[num])
    money_list[num] -= p
    now -= p * money[num]
    return now
for now in X:
    for i in reversed(range(6)):
        now = cal(now, i)
    if now == 0:
        continue
    else:
        print('No')
        break
else:
    print('Yes')