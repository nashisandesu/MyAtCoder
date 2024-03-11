import sys, bisect
import math
import numpy as np
sys.setrecursionlimit(10**8)
from collections import deque
from itertools import combinations
from itertools import permutations
from atcoder.segtree import SegTree

I = lambda: int(input())
S = lambda: str(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
N, Q = Mi()
A = Li()
mex = [0] * (N+1)
cnt = dict()
for a in A:
    if a <= N:
        mex[a] = float('Inf')
        cnt.setdefault(a, 0)
        cnt[a] += 1

for i in range(N+1):
    if mex[i] == 0:
        mex[i] = i

seg = SegTree(min, float('Inf'), mex)

for i in range(Q):
    i, after = Mi()
    i -= 1
    before = A[i]
    if before <= N:
        cnt[before] -= 1
        if cnt[before] == 0:
            seg.set(before, before)
        
    A[i] = after
    if after > N:
        print(seg.all_prod())
        continue

    cnt.setdefault(after, 0)
    cnt[after] += 1
    if cnt[after] == 1:
        seg.set(after, float('Inf'))
    print(seg.all_prod())
