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
N, M, K = Mi()
data = [Ls() for _ in range(M)]
cnt = 0
for i in range(1 << N):
    num = list(format(i, f'0{N}b'))
    for j in range(M):
        c, *A, r = data[j]
        ok = 0
        for k in range(int(c)):
            if num[int(A[k])-1] == '1':
                ok += 1
        if ok >= K and r == 'x':
            break
        elif ok < K and r == 'o':
            break
    else:
        cnt += 1
print(cnt)
