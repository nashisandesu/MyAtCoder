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
left, right = Mi()
ans = []
while True:
    cnt = 0
    while left % (2**(cnt+1)) == 0 and left + 2 ** (cnt + 1) <= right:
        cnt += 1
    i, j = cnt, left //(2**cnt)
    ans.append((left, 2 ** i * (j+1)))
    left = 2 ** i * (j+1)
    if left == right:
        print(len(ans))
        for i in range(len(ans)):
            print(*ans[i])
        exit()
