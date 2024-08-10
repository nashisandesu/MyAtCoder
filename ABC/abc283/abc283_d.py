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
s = list(input())
cnt = deque()
cnt.append(0)
box = deque()
for moji in s:
    if moji == '(':
        cnt.append(0)
    elif moji == ')':
        del_num = cnt.pop()
        for _ in range(del_num):
            box.pop()
    else:
        if moji in box:
            print('No')
            exit()
        else:
            box.append(moji)
            cnt[-1] += 1
else:
    print('Yes')