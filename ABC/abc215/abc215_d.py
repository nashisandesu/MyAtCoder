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

N, M = Mi()
A = Li()
soinsuu = set()
for i in range(N):
    fac = factorization(A[i])
    for f in fac:
        soinsuu.add(f[0])

ans = [True] * (M+1)
for i in soinsuu:
    if 1 < i <= M and ans[i]:
        for j in range(i, M+1, i):
            ans[j] = False

result = []
for i in range(1, M + 1):
    if ans[i]:
        result.append(i)

print(len(result))
for i in result:
    print(i)