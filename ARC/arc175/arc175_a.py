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
import heapq

I = lambda: int(input())
S = lambda: str(input())
Sl = lambda: list(input())
Mi = lambda: map(int, input().split())
Ms = lambda: map(str, input().split())
Li = lambda: list(map(int, input().split()))
Ls = lambda: list(map(str, input().split()))

########################################################
mod = 998244353
N = I()
A = Li()
s = Sl()

visit = [0] * N
ans_l = 1
for i in range(N):
    #Lで揃える
    if s[A[i]-1] == 'L':
        visit[A[i]-1] = 1
    elif s[A[i]-1] == 'R' and visit[A[i] % N] == 1:
        visit[A[i]-1] = 1
    elif s[A[i]-1] == '?':
        if visit[A[i] % N] == 1:
            ans_l *= 2
            ans_l %= mod
        visit[A[i]-1] = 1
    else:
        ans_l = 0
        break

visit = [0] * N
ans_r = 1
for i in range(N):
    #Rで揃える
    if s[A[i]-1] == 'R':
        visit[A[i]-1] = 1
    elif s[A[i]-1] == 'L' and visit[(A[i]-2)% N] == 1:
        visit[A[i]-1] = 1
    elif s[A[i]-1] == '?':
        if visit[(A[i]-2) % N] == 1:
            ans_r *= 2
            ans_r %= mod
        visit[A[i]-1] = 1
    else:
        ans_r = 0
        break

print((ans_l+ans_r)%mod)

