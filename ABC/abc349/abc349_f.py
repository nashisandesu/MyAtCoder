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
mod = 998244353
if M == 1:
    print((2 ** A.count(1) - 1) % mod)
    exit()

fac = factorization(M)
element = [a ** b for a, b in fac]
K = len(element)
cnt = [0] * (1<<K)
one_cnt = 0
for a in A:
    if a == 1:
        one_cnt += 1
    elif M % a == 0:
        bit = 0
        for i in range(K):
            bit <<= 1
            if a % element[i] == 0:
                bit += 1
        cnt[bit] += 1

dp = [0] * (1<<K)
dp[0] = 1

for i in range(1<<K):
    ndp = [0] * (1 << K)
    c = pow(2, cnt[i], mod) - 1 
    for j in range(1<<K):
        ndp[i | j] += dp[j] * c
        ndp[i | j] %= mod

        ndp[j] += dp[j]
        ndp[j] %= mod
    dp = ndp

print(dp[-1] * (2 ** one_cnt) % mod)