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
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

# from functools import cache
# @cache
# def f(x):
#     if x == 1:
#         return 0
#     elif x == 2:
#         return 1
#     small = x // 2
#     big = x - small
#     return f(big) + 1
    

N = I()
fac = factorization(N)

cnt = 0
for i in range(len(fac)):
    cnt += fac[i][1]

#これだけでいい
for ans in range(int(12 * math.log2(10)) + 1):
    if cnt <= 2 ** ans:
        print(ans)
        break
# print(f(cnt))