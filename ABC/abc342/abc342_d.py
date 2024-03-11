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

N = I()
A = Li()
ans = 0
check = [0] * (2*(10**5) + 1)

for i in range(N):
    check[A[i]] += 1

for i in range(2*(10**5) + 1):
    if check[i] >=2:
        ans += math.comb(check[i], 2) 

A = list(set(A))
A.sort()

for left in range(len(A)):
    if A[left] == 0:
        ans += check[0] * (N - check[0])
    else:
        num = A[left]
        soinsuu = factorization(num)
        search = 1
        for i in range(len(soinsuu)):
            if soinsuu[i][1] % 2 == 1:
                search *= soinsuu[i][0]
        cnt = 1
        search_start = search

        while search <= num:
            cnt += 1
            search = search_start * (cnt * cnt)

        while search <= A[-1]:
            ans += check[search] * check[num]
            cnt += 1
            search = search_start * (cnt * cnt)
print(ans)